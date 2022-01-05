from os import mkdir, system
from json import load, dump
import json_changes

def main(filename, file_path):

    def create_file():
        f = open(file_path, "x")
        data = {}
        data['preset_name'] = []
        data['preset_name'].append({
            'cmd1': 'Example:',
            'cmd2': 'start chorme',
            'cmd3': 'other command'
        })
        dump(data, f, indent=4)
        f.close()


    def print_data(data):
        data.pop("preset_name")
        for i in data:
            print(i)
            for ii in data[i]:
                for iii in ii:
                    print(f"     {data[f'{i}'][0][f'{iii}']}")


    try:
        mkdir("startup_custom_presets")
    except:
        pass

    try:
        f = open(file_path, "r")
    except:
        create_file()
        f = open(file_path, "r")

    data = load(f)

    f.close()

    if len(data) == 1:

        print("\nThere are no presets")

    else:
        print_data(data)


    print(
    """
    What you want?
    Add a preset => command: add
    Remove a preset => command: remove
    Customize a preset => command: custom
    """)
    choise = input("=> ")

    add = ["add", "+"]
    rm = ["rm", "-", "remove"]
    change = ["change", "custom", "customize", "edit"]
    exit_programm = ["exit", "quit"]

    if choise in add:
        system("cls")
        json_changes.add(file_path, filename)
    elif choise in rm:
        system("cls")
        json_changes.rm(file_path)
    elif choise in change:
        system("cls")
        json_changes.change(file_path)
    elif choise in exit_programm:
        return
    else:
        print("Sorry, this command does not exist")