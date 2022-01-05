# Commands_Presets
A program to create sets of commands to be run when it is called.

# How to use
Chage the .exe name for anything you want and put the file on System32 or another location that the computer assumes can be called by name only.
After this just type the name the file on CMD and "config" as a argument to start creating a command preset. \
`preset config`

# Example
You call your file "preset" and have a preset named "programming" with the commands :
  `start chrome`
  `start code`
  `python3`
  `wsl`
  
To run all this commands just type: 
```
preset programming
```

# Help
**Commands** \
`[File_name] [Preset_name]` => start a preset

From here on I will assume the file with the name "preset".

`preset config` => open a preset configuration \
`preset config-json` => open the json file with all the created presets \

**To create a preset** \
`preset config` \
`add` \
`[preset name]` \
`[command1],[command2],[etc.]`

**To remove a preset** \
`preset config` \
`remove` \
`[preset name]` 

**To edit a preset** \
`preset config` \
`edit` \
`[preset name]` \
`[command_number_to_edit]` \
`[new_command1],[new_command2],[etc.]`


