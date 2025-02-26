import os
import sys
import json
import hashlib
from zipfile import ZipFile

dir = os.getcwd()

repo = sys.argv[1]
branch = sys.argv[2]

for i in os.listdir(f"{dir}//mods"):
    print(f"https://raw.githubusercontent.com/{repo}/refs/heads/{branch}/mods/{i}")

with open('modrinth.index.json', 'w') as file:
    mrjson = {
        "formatVersion": "1",
        "game": "minecraft",
        "versionId": branch,
        "name": "Test mrpack",
        "files": [],
        "dependencies": {
            "minecraft": "1.20.1",
            "forge": "47.3.0"
        }
    }
    for i in os.listdir(f"{dir}//mods"):

        hash_func = hashlib.new("sha1")
        with open(f"mods/{i}", 'rb') as file:
            while chunk := file.read(8192):  # Read the file in chunks of 8192 bytes
                hash_func.update(chunk)
        sha1 = hash_func.hexdigest()

        hash_func = hashlib.new("sha512")
        with open(f"mods/{i}", 'rb') as file:
            while chunk := file.read(8192):  # Read the file in chunks of 8192 bytes
                hash_func.update(chunk)
        sha512 = ""

        filejson = {
            "path": f"mods/{i}",
            "hashes": {
                "sha1": sha1,
                "sha512": sha512
            },
            "downloads": [
                f"https://raw.githubusercontent.com/{repo}/refs/heads/{branch}/mods/{i}"
            ],
            "fileSize": os.path.getsize(f"{dir}//mods//{i}")
        }

        mrjson["files"].append(filejson)

    output = json.dumps(mrjson, indent=4)
    file.write(output)

with ZipFile('pack.mrpack', 'w', zipfile.ZIP_DEFLATED) as pack:
    pack.write("modrinth.index.json")