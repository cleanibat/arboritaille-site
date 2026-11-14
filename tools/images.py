# Génère les variantes web des photos : JPEG optimisé 1600 px + WebP 1600 px (hero) et 800 px (cartes/galeries).
import glob,os
from PIL import Image, ImageOps
os.makedirs('img/w',exist_ok=True)
for f in sorted(glob.glob('img/*.jpg')):
    n=os.path.splitext(os.path.basename(f))[0]
    im=ImageOps.exif_transpose(Image.open(f)).convert('RGB')
    w,h=im.size
    for width,suffix in ((1600,''),(800,'-800')):
        if w>width: im2=im.resize((width,round(h*width/w)),Image.LANCZOS)
        else: im2=im
        im2.save(f'img/w/{n}{suffix}.webp','WEBP',quality=78,method=6)
    im.resize((1600,round(h*1600/w)),Image.LANCZOS).save(f,'JPEG',quality=80,optimize=True,progressive=True) if w>1600 else im.save(f,'JPEG',quality=80,optimize=True,progressive=True)
    print(n,w,h,'->',os.path.getsize(f)//1024,'Ko jpg,',os.path.getsize(f'img/w/{n}.webp')//1024,'Ko webp,',os.path.getsize(f'img/w/{n}-800.webp')//1024,'Ko webp800')
