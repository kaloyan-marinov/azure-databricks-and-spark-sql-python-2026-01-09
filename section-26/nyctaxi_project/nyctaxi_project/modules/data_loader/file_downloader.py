import urllib.request
import os
import shutil


def download_file(url: str, dir_path: str, local_path: str) -> None:
    os.makedirs(
        os.path.dirname(dir_path),
        exist_ok=True,
    )

    with urllib.request.urlopen(url) as response, open(local_path, "wb") as out_file:
        # Open a connection and stream the remote file
        shutil.copyfileobj(
            response,
            out_file,
        )
