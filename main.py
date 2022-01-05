from os import path
from sys import argv, exit
import customize, start_preset

__author__ = "redystum"
__github__ = "https://github.com/redystum"

filename = path.splitext(path.basename(__file__))[0]
file_path = "startup_custom_presets\config.json"

try:
    args = str(argv[1])
except:
    print(f"Error: Please specify a argument. Example: {filename} preset1. If you dont have any preset type {filename} config")
    exit()

if args == "":
    print(f"Error: Please specify a argument. Example: {filename} preset1. If you dont have any preset type {filename} config")
    exit()

print("Opening " + args)

if args == "customize" or args == "config":
    customize.main(filename, file_path)

else:
    start_preset.main(filename, args, file_path)
