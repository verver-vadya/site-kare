# 3. Собирает трубки из веток (номера веток смотреть на branches.png), сглаживает их, добавляет
#    чёрные концы у электродов, держатели и провода до спинки дивана на фото и пишет src/data/neon.ts.
#    python3 tools/neon/build.py
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import json, numpy as np
from scipy.ndimage import gaussian_filter1d
B=[np.array(b,float) for b in json.load(open('branches.json'))]
S=3000/1878  # raster px per font unit
def fu(a): return np.column_stack([a[:,0]/S-47, a[:,1]/S-1016])
R=lambda i: B[i][::-1]
cat=lambda *xs: np.vstack(xs)
tubes={
 'k1': cat(B[10], R(2)),
 'k2': cat(R(14), R(3)),
 'a':  cat(B[5], B[15], R(12)),
 'p1': cat(R(8), R(13), R(1)),
 'p2': B[0],
 'e':  cat(B[9], R(7)),
}
def resample(p, step=4.0):
    seg=np.linalg.norm(np.diff(p,axis=0),axis=1); keep=np.concatenate([[True],seg>1e-6]); p=p[keep]
    seg=np.linalg.norm(np.diff(p,axis=0),axis=1); s=np.concatenate([[0],np.cumsum(seg)])
    n=max(2,int(s[-1]/step)+1); t=np.linspace(0,s[-1],n)
    return np.column_stack([np.interp(t,s,p[:,0]),np.interp(t,s,p[:,1])])
def smooth(p, sigma=4):
    q=np.column_stack([gaussian_filter1d(p[:,0],sigma,mode='nearest'),gaussian_filter1d(p[:,1],sigma,mode='nearest')])
    q[0]=p[0]; q[-1]=p[-1]; return q
def rdp(p,eps):
    if len(p)<3: return p
    a,b=p[0],p[-1]; ab=b-a; L=np.linalg.norm(ab)
    d=np.abs(ab[0]*(p[:,1]-a[1])-ab[1]*(p[:,0]-a[0]))/L if L>0 else np.linalg.norm(p-a,axis=1)
    i=np.argmax(d)
    if d[i]>eps: return np.vstack([rdp(p[:i+1],eps)[:-1], rdp(p[i:],eps)])
    return np.array([a,b])
def dstr(p): return "M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in p)
def head(p, length):  # first `length` units of polyline
    seg=np.linalg.norm(np.diff(p,axis=0),axis=1); s=np.concatenate([[0],np.cumsum(seg)])
    k=np.searchsorted(s,length); return p[:max(2,k+1)]
out={'tubes':{}, 'blocks':[], 'boots':[], 'wires':[]}
ends={}
for name,raw in tubes.items():
    p=smooth(resample(fu(raw)))
    out['tubes'][name]=dstr(rdp(p,0.5))
    ends[name]=(p, p[0], p[-1])
# blockouts: (tube, which end, length, boot?)
spec=[('k1',0,38,1),('k1',1,38,1),('k2',0,38,1),('k2',1,38,1),('a',1,38,1),('p1',0,38,1),('p1',1,38,1),('e',1,38,1)]
boot={}
for name,end,L,b in spec:
    p=ends[name][0]; q=p if end==0 else p[::-1]
    out['blocks'].append(dstr(rdp(head(q,L),0.5)))
    if b:
        out['boots'].append([round(q[0][0],1),round(q[0][1],1)]); boot[(name,end)]=q[0]
def Y(Yo): return (Yo-800)/0.617678-1016
railTop, railBot, pillow = Y(1760), Y(1800), Y(1905)
def lead(pt, dx):
    x,y=pt; x2=x+dx
    a=f"M{x:.1f} {y:.1f} C{x+6:.1f} {y+(railTop-y)*0.35:.1f} {x2-4:.1f} {y+(railTop-y)*0.7:.1f} {x2:.1f} {railTop:.1f}"
    b=f"M{x2:.1f} {railBot:.1f} L{x2+1:.1f} {pillow:.1f}"
    return [a,b]
def sag(p,q,k=0.28):
    m=(p+q)/2; L=np.linalg.norm(q-p); c=m+np.array([0,L*k+30])
    return f"M{p[0]:.1f} {p[1]:.1f} Q{c[0]:.1f} {c[1]:.1f} {q[0]:.1f} {q[1]:.1f}"
W=out['wires']
W.append(sag(boot[('k1',0)],boot[('k2',0)]))
W.append(sag(boot[('k2',1)],boot[('a',1)],0.18))
W+= lead(boot[('k1',1)],-6)
W+= lead(boot[('p1',0)],10)
W+= lead(boot[('p1',1)],4)
W+= lead(boot[('e',1)],-8)
json.dump(out,open('neon.json','w'),indent=0)
print({k:len(v) for k,v in out['tubes'].items()}, len(out['blocks']), out['boots'])

# src/data/neon.ts
import sys
dst = '../../src/data/neon.ts'
fmt = lambda xs: ",\n    ".join(f'"{x}"' for x in xs)
ts = f'''// Неоновая вывеска «Каре» в координатах надписи (те же, что у wordmark.ts): осевые линии стеклянных трубок,
// чёрные концы у электродов, держатели и провода. Собрано скриптами tools/neon/ — руками не править.
export const neon = {{
  tubes: [
    {fmt(out['tubes'].values())},
  ],
  blocks: [
    {fmt(out['blocks'])},
  ],
  boots: {json.dumps([[float(a), float(b)] for a, b in out['boots']])},
  wires: [
    {fmt(out['wires'])},
  ],
}};
'''
open(dst, 'w').write(ts)
