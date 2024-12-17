import requests
from pathlib import Path

def download_to_local(url:str, out_path:Path, parent_mkdir:bool=True):
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path}must be valid pathlib. Path object")    
    if parent_mkdir:
        out_path.parent.mkdir(exist_ok=True, parents=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'Invalid url, Faild to download {url}: {e}')
        return False