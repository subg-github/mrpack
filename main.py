import os

dir = os.getcwd()

print(os.listdir(f"{dir}//mods"))

with open('pack.mrpack', 'w') as file:
    file.write(os.listdir(f"{dir}//mods"))