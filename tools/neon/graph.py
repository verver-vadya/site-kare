# 2. Скелет букв (осевая линия) и его ветки: branches.json и branches.png с номерами веток.
#    python3 tools/neon/graph.py  (нужны numpy, scipy, scikit-image, Pillow)
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
import numpy as np, json
from PIL import Image, ImageDraw
from skimage.morphology import skeletonize
sk=skeletonize(np.array(Image.open('glyphs.png').convert('L'))<128)
H,W=sk.shape
pts=set(zip(*np.nonzero(sk)))
N=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def nb(p): return [(p[0]+a,p[1]+b) for a,b in N if (p[0]+a,p[1]+b) in pts]
def prune_and_trace(pts):
    deg={p:len(nb(p)) for p in pts}
    nodes={p for p in pts if deg[p]!=2}
    # cluster adjacent node pixels
    seen=set(); branches=[]
    for n in nodes:
        for q in nb(n):
            if q in nodes: continue
            key=(n,q)
            if key in seen: continue
            path=[n,q]; prev=n; cur=q
            while cur not in nodes:
                nx=[r for r in nb(cur) if r!=prev and r not in path[-3:]]
                if not nx: break
                prev,cur=cur,nx[0]; path.append(cur)
            seen.add((path[-1],path[-2])); seen.add(key)
            branches.append(path)
    return branches,deg
branches,deg=prune_and_trace(pts)
# remove spurs: branch with an endpoint (deg1) and length<60
for it in range(3):
    rm=[b for b in branches if len(b)<70 and (deg[b[0]]==1 or deg[b[-1]]==1)]
    for b in rm:
        for p in b:
            if deg.get(p,0)<=2 or p in (b[0],b[-1]) and deg[p]==1: pts.discard(p)
    branches,deg=prune_and_trace(pts)
# drop tiny duplicate branches
branches=[b for b in branches if len(b)>3]
print(len(branches))
im=Image.open('glyphs.png').convert('RGB'); d=ImageDraw.Draw(im)
cols=[(230,25,75),(60,180,75),(0,130,200),(245,130,48),(145,30,180),(70,240,240),(240,50,230),(210,245,60),(0,128,128),(170,110,40),(128,0,0),(0,0,128),(128,128,0)]
out=[]
for i,b in enumerate(branches):
    c=cols[i%len(cols)]
    d.line([(p[1],p[0]) for p in b],fill=c,width=9)
    m=b[len(b)//2]; d.text((m[1]+12,m[0]),str(i),fill=c,font_size=60)
    out.append([[int(p[1]),int(p[0])] for p in b])
im.resize((1500,1171)).save('branches.png')
json.dump(out,open('branches.json','w'))
for i,b in enumerate(out): print(i,len(b),b[0],b[-1])
