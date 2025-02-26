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

    with open(f"mods/{i}", 'rb') as file:
        sha1 = hashlib.file_digest(f, "sha1")

    with open(f"mods/{i}", 'rb') as file:
        sha512 = hashlib.file_digest(f, "sha512")

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

with open('modrinth.index.json', 'w') as file:
    file.write(output)

with ZipFile('pack.mrpack', 'w') as pack:
    pack.write("modrinth.index.json")