"""Stage an explicitly reviewed static bundle; never modify monitoring data/services."""
from pathlib import Path, PurePosixPath
import argparse,hashlib,json,os,re,shutil,stat,tempfile,zipfile

ROOT=Path('/usr/local/share/may-monitor/themes')

def safe_member(name):
    value=PurePosixPath(name)
    return not name.startswith('/') and '\\' not in name and str(value)==name and not any(v in ('','..','.') for v in value.parts) and (name in ('komari-theme.json','preview.png','preview-v2.0.0.png') or name.startswith('dist/'))

def stage(asset,expected,root=ROOT):
    if not re.fullmatch('[a-f0-9]{64}',expected) or asset.is_symlink() or not asset.is_file() or not 0<asset.stat().st_size<=64*1024**2:
        raise ValueError('Invalid reviewed package or SHA-256')
    if hashlib.sha256(asset.read_bytes()).hexdigest()!=expected:raise ValueError('Package SHA-256 differs')
    # The CLI has a fixed destination. Root injection is limited to imported
    # disposable-filesystem validation; it is not a command-line parameter.
    root.mkdir(parents=True,mode=0o755,exist_ok=True)
    for p in (root,*root.parents):
        info=p.lstat()
        if p.is_symlink() or not p.is_dir() or info.st_uid!=0 or info.st_mode&0o022:raise ValueError('Unsafe staging directory')
    temporary=Path(tempfile.mkdtemp(prefix='.staging-',dir=root));temporary.chmod(0o755)
    try:
        files={};total=0
        with zipfile.ZipFile(asset) as archive:
            members=archive.infolist()
            if len(members)>10000:raise ValueError('Too many theme members')
            seen=set()
            for member in members:
                name=member.filename.rstrip('/') if member.is_dir() else member.filename
                if not (safe_member(name) or member.is_dir() and name=='dist') or name in seen or stat.S_ISLNK(member.external_attr>>16):raise ValueError('Unsafe or duplicate archive member')
                seen.add(name)
                if member.is_dir():continue
                total+=member.file_size
                if member.file_size>16*1024**2 or total>256*1024**2:raise ValueError('Theme exceeds extraction bounds')
                output=temporary/name;output.parent.mkdir(parents=True,mode=0o755,exist_ok=True)
                for directory in output.parents:
                    if directory==root:break
                    directory.chmod(0o755)
                with archive.open(member) as source,output.open('xb') as target:shutil.copyfileobj(source,target,65536)
                output.chmod(0o644);files[name]=hashlib.sha256(output.read_bytes()).hexdigest()
        manifest=json.loads((temporary/'komari-theme.json').read_text(encoding='utf-8'))
        if manifest.get('short')!='GlassmorphismEnhanced' or not (temporary/'dist/index.html').is_file():raise ValueError('Unexpected May Status theme identity')
        configuration=manifest.get('configuration',{})
        if configuration.get('type')!='managed' or not isinstance(configuration.get('data'),list):raise ValueError('Reviewed theme requires a managed settings schema')
        lock=json.dumps({'schema':1,'short':manifest['short'],'files':dict(sorted(files.items()))},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
        pin=hashlib.sha256(lock).hexdigest();destination=root/pin
        if destination.exists() or destination.is_symlink():raise ValueError('This reviewed revision is already staged; verify it instead of overwriting')
        (temporary/'may-theme.lock.json').write_bytes(lock);(temporary/'may-theme.lock.json').chmod(0o644)
        temporary.rename(destination)
        return {'schema':1,'staged':True,'short':manifest['short'],'version':manifest.get('version'),'theme_lock_sha256':pin,'package_sha256':expected,'files':len(files),'service_restarted':False,'next':'Select ConfigureTheme in May Deploy with this lock SHA-256; activation has its own component backup and recovery.'}
    finally:
        # Only this invocation's unique staging directory can be cleaned up.
        if temporary.exists():shutil.rmtree(temporary)

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('package',type=Path);parser.add_argument('sha256');args=parser.parse_args()
    if os.name!='posix' or os.geteuid()!=0:raise ValueError('Run staging as root on the May server')
    print(json.dumps(stage(args.package.resolve(),args.sha256),ensure_ascii=False))
if __name__=='__main__':main()
