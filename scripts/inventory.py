"""Read-only file inventory. No uploads, annotation parsing or image-level claims."""
import argparse,csv,hashlib,os
from pathlib import Path

def inventory(root,out,hash_files=False):
    root=Path(root).expanduser().resolve();out=Path(out).expanduser().resolve()
    if not root.is_dir():raise ValueError('Data root must be an existing directory')
    out.parent.mkdir(parents=True,exist_ok=True)
    total=0
    with out.open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['relative_path','extension','bytes','sha256','status'])
        # Do not follow directory symlinks or publish any inventory automatically.
        for directory,dirs,files in os.walk(root,followlinks=False):
            dirs[:]=sorted(d for d in dirs if not Path(directory,d).is_symlink() and d not in {'.git','__pycache__'})
            for name in sorted(files):
                p=Path(directory,name)
                if p.is_symlink() or p.resolve()==out:continue
                digest='';size='';status='ok'
                try:
                    size=p.stat().st_size
                    if hash_files:
                        h=hashlib.sha256()
                        with p.open('rb') as f:
                            for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
                        digest=h.hexdigest()
                except OSError as e:status=type(e).__name__
                writer.writerow([str(p.relative_to(root)),p.suffix.lower(),size,digest,status]);total+=1
    return total

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',default=os.environ.get('WELD_DATA_ROOT'))
    parser.add_argument('--out',default='data/private/inventory.csv')
    parser.add_argument('--hash',action='store_true',help='Read all file bytes; can be slow on a large corpus')
    args=parser.parse_args()
    if not args.root:parser.error('Set WELD_DATA_ROOT or pass --root')
    print('Inventory rows:',inventory(args.root,args.out,args.hash))
    print('Files are not independent welds; verify image/annotation roles separately.')
