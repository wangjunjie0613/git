"""Collect minimal local resource metadata; no network requests or environment dump."""
import argparse,json,platform,subprocess,sys
from pathlib import Path

def report():
    result={'python':sys.version.split()[0],'platform':platform.system(),'gpu_status':'unchecked'}
    try:
        p=subprocess.run(['nvidia-smi','--query-gpu=name,memory.total,memory.free,driver_version','--format=csv,noheader'],capture_output=True,text=True,timeout=15)
        result['gpu_status']='ok' if p.returncode==0 else 'command_failed'
        if p.returncode==0:result['gpu_rows']=p.stdout.strip().splitlines()
        else:result['returncode']=p.returncode
    except (OSError,subprocess.TimeoutExpired) as e:result['gpu_status']=type(e).__name__
    result['note']='User server only; does not establish PyTorch compatibility or model performance.'
    return result

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--out',default='runs/environment.json');args=a.parse_args()
    out=Path(args.out);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Saved local environment report.')
