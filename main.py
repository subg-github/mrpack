import os
import sys

dir = os.getcwd()

repo = sys.argv[1]
branch = sys.argv[2]

for i in os.listdir(f"{dir}//mods"):
    print(f"https://raw.githubusercontent.com/{repo}/refs/heads/{branch}/mods/{i}")

with open('pack.mrpack', 'w') as file:
    for i in os.listdir(f"{dir}//mods"):
        file.write(f"https://raw.githubusercontent.com/{repo}/refs/heads/{branch}/mods/{i}")