import os
import sys

dir = os.getcwd()

repo = f"{sys.argv[1]}/{sys.argv[2]}"

for i in os.listdir(f"{dir}//mods"):
    print(f"https://github.com/{repo}/mods/{i}")

with open('pack.mrpack', 'w') as file:
    for i in os.listdir(f"{dir}//mods"):
        file.write(f"https://github.com/{repo}/mods/{i}")