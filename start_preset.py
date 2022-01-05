from os import system, startfile, path
from json import load

def main(filename, args, file_path):
    if args == "customize-json" or args == "config-json":
        path_ = path.abspath(file_path)
        startfile(f"{path_}")

    else:

        f = open(file_path, "r")
        data = load(f)
        f.close()
        data.pop("preset_name")

        for i in data:
            if i == args:
                for ii  in data[args][0]:
                    cmd = data[args][0][f'{ii}']
                    try:
                        system(f'{cmd}')
                    except:
                        print("One of the commands did not work, check if you typed it correctly. Tip: Test you command on cmd to see if works")

                return

            else:
                pass

        print(f"The preset \"{args}\" does not exist, to create a preset type {filename} config")