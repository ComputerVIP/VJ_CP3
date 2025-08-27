# VJ_CP3

## Project Desc.
---

This is my school repo! 


## Installation
---

Not used for this class


## Execution and Usage
---

Paragraph describing how to use this program.  
![image](**<relative path here>**) Note, image has to be in repository.  


## Used Tech
---
This project will require MSYS2, MYSY64, and FLTK.

+ FLTK
`https://www.fltk.org/software.php` 

+ MSYS2 and MSYS64
`https://www.msys2.org`  


After this, you must configure your terminal to run through MSYS2, I did this through VSCODE, the steps for this follow:

+ Find the path of your mingw64.exe  
Should be here:
```bash
C:\msys64\mingw64.exe
```

+ Add to VS Code terminal profiles
Files > Preferences > Settings, then enter in the searchbar:
`terminal.integrated.profiles.windows`

+ Edit settings.json
Click the edit settings.json button and add:
```json
"MSYS2": {
            "path": "C:\\msys64\\usr\\bin\\bash.exe",
            "args": [
                "-li"
            ],
            "env": {
                "MSYSTEM": "MINGW64"
            }
        }
```

+ Set default to MINGW64
Add this to settings.json as well:
```json
"terminal.integrated.defaultProfile.windows": "MSYS2"
```

+ Run terminal
Once you do that, run: 
```bash
pacman -S mingw-w64-x86_64-gcc
```
Check to make sure it is there with:
```bash
g++ --version
```

+ Install FLTK (A second time)
```bash
pacman -S mingw-w64-x86_64-fltk
```

+ Go to current directory
```bash
cd /c/folder_name/project_folder
```

+ Compile app
If no .exe exists:
```bash
g++ project_name.cpp -o name_to_compile_as `fltk-config --cxxflags --ldflags`
```
f it does exist, skip this step

+ Run code
```bash
./name_of_file.exe
```

This should allow it to run, do note, it also will run regular .cpp files with this configuration.

## Current Features
---

+ Main feature one

+ Main feature two

+ Main feature three  


## Contributions
---
Steps of how to allow others to contribute, NOT USED FOR CLASS


## Contributers
---

+ Person who helped with the project, what they did

+ Person who helped with the project, what they did

+ Person who helped with the project, what they did

+ Person who helped with the project, what they did  


## Author's Information
---
Short paragraph about author (EACH member of the group has one)
Includes contact information


## Change log
---
Shows the version, updates, and fixes, NOT USED FOR CLASS


## License
---
What types of permissions, NOT USED FOR CLASS