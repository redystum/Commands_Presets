from json import load, dump

def exist(file_path, name):
    f = open(file_path, "r")
    data = load(f)
    f.close()
    data.pop("preset_name")
    for i in data:
        if i not in name:
            continue
        else:
            return True 
    return False

def print_data(file_path):
    f = open(file_path, "r")
    data = load(f)
    f.close()
    if len(data) == 1:
        print("\nThere are no presets")
        return False

    data.pop("preset_name")
    for i in data:
        print(i)
        for ii in data[i]:
            for iii in ii:
                print(f"     {data[f'{i}'][0][f'{iii}']}")


def add(file_path, filename):
    print("Presset creator:\n")
    print("Just enter the name and write the command you would like to run when the preset is called.\nExample => Name: PS, Command: start photoshop")

    print("\nIMPORTANT!!! To have several commands type a comma to separate them\nExample => Command: start chrome,start notepad,start discord\n")

    name = input("Preset Name: ")
    name_ = [f'{name}']

    config = ['config','customize','config-json','customize-json']
    if name in config:
        print("This name are reserved for program settings.")
        return

    if exist(file_path, name_) == True:
        print("This preset already exist")
        return

    cmd = input("Command: ").split(",")


    print(f"OK, the preset is being created, please wait...\n")

    f = open(file_path, "r")
    data = load(f)
    f.close()
    f = open(file_path, "w")

    data[name] = []

    ii=1
    for i in cmd:

        if ii == 1:
            commands = {f'cmd{ii}': f'{i}'}
        else:
            new_cmd = {f'cmd{ii}': f'{i}'}
            commands.update(new_cmd)

        ii += 1

    data[name].append(commands)

    dump(data, f, indent=4)

    f.close()

    print(f"DONE! To use it just type \"{filename} {name}\" on cmd!")


def rm(file_path):
    print("Remove a presset:\n")


    if print_data(file_path) == False:
        print("\nTo create a preset choose the add option in the customizer menu.")

    print("\nEnter the name of the preset do you want to remove")
    print("\nIMPORTANT!!! To remove several presets type comma to separate them\nExample => remove: gaming,study\n")

    cmd = input("remove: ").split(",")

    if exist(file_path, cmd) == False:
        print("This preset does not exist, to create a preset choose the add option in the customizer menu")
        return

    f = open(file_path, "r")
    data = load(f)
    f.close

    for i in cmd:
        data.pop(f"{i}")

    f = open(file_path, "w")

    dump(data, f, indent=4)

    f.close()

    print(f"DONE! The preset are removed successfully!")


def change(file_path):
    print("Edit a preset:")

    if print_data(file_path) == False:
        print("\nTo create a preset choose the add option in the customizer menu.")
        return

    print("\nEnter the name of the preset do you want to edit")
    cmd = input("Edit: ")
    cmd_ = [f'{cmd}']

    if exist(file_path, cmd_) == False:
        print("This preset does not exist, to create a preset choose the add option in the customizer menu")
        return

    f = open(file_path, "r")
    data = load(f)
    f.close()
    data_ = dict(data)

    print(f"\nThe commands in {cmd} are: \n")

    data_.pop("preset_name")
    for i in data_[f'{cmd}']:
        for ii in i:
            print(f"     {data_[f'{cmd}'][0][f'{ii}']}")    

    print(
    """
    What you want?
    Add a command => command: add
    Remove a command => command: remove
    Customize a command => command: custom
    """)
    choise = input("=> ")

    add = ["add", "+"]
    rm = ["rm", "-", "remove"]
    change = ["change", "custom", "customize", "edit"]
    exit_programm = ["exit", "quit"]

    if choise in add:

        print("\nIMPORTANT!!! To add several commands type a comma to separate them\nExample => Command: start chrome,start notepad\n")

        command = input("Command to add: ").split(",")

        x = len(data[f'{cmd}'][0])

        for i in command:
            new_cmd = {f'cmd{x+1}': f'{i}'}
            data[f'{cmd}'][0].update(new_cmd)

            x += 1

        f = open(file_path, "w")
        dump(data, f, indent=4)
        f.close()

        print(f"DONE! The command was successfully added !")

    elif choise in rm:

        f = open(file_path, "r")
        data = load(f)
        f.close()
        data_ = dict(data)

        print(f"\nThe commands in {cmd} are: \n")

        data_.pop("preset_name")
        x = 1

        print("   Number : Command\n   ----------------")
        for i in data_[f'{cmd}']:
            for ii in i:
                print(f"        {x} : {data_[f'{cmd}'][0][f'{ii}']}")    
                x += 1

        print("\nIMPORTANT!!! To remove several commands type comma to separate them\nExample => remove: 2,5\n")

        command = input("Command number to remove: ").split(",")

        for i in command:
            if f'cmd{i}' not in data[f'{cmd}'][0]:
                print(f"The command number {i} does not exists")
                return
            else:
                continue

        origin = dict(data)
        data.pop(f'{cmd}')
        ii = 1
        first = 1
        for i in origin[f'{cmd}'][0]:
            if str(ii) in command:
                first += 1
                pass
            else:
                comd = origin[f'{cmd}'][0][f'cmd{ii}']
                if ii == first:
                    commands = {f'cmd{ii-first+1}': f'{comd}'}
                else:
                    new_cmd = {f'cmd{ii-first+1}': f'{comd}'}
                    commands.update(new_cmd)

            ii += 1 

        try:
            data[f'{cmd}'] = []
            data[f'{cmd}'].append(commands)
        except:
            print("Error. Probably you are removing all commands, to do this remove the entire preset")
            return

        f = open(file_path, "w")
        dump(data, f, indent=4)
        f.close()

        print(f"DONE! The command was successfully removed!")

        


    elif choise in change:
        f = open(file_path, "r")
        data = load(f)
        f.close()
        data_ = dict(data)

        print(f"\nThe commands in {cmd} are: \n")

        data_.pop("preset_name")
        x = 1

        print("   Number : Command\n   ----------------")
        for i in data_[f'{cmd}']:
            for ii in i:
                print(f"        {x} : {data_[f'{cmd}'][0][f'{ii}']}")    
                x += 1

        command = input("Command number to edit: ")

        try:
            int(command)
        except:
            print(f"{command} is not a command number!")
            return

        if f'cmd{command}' not in data[f'{cmd}'][0]:
            print(f"The command number {command} does not exists")
            return
        else:
            pass

        print("Write the command you want to overwrite")
        new_command = input("command: ")

        f = open(file_path, "r")
        data = load(f)
        f.close()

        data[f'{cmd}'][0][f'cmd{command}'] = new_command

        f = open(file_path, "w")
        dump(data, f, indent=4)
        f.close()

        print(f"DONE! The command was successfully edited!")


    elif choise in exit_programm:
        return
    else:
        print("Sorry, this command does not exist")