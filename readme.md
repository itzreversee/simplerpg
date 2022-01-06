<p align="center"> <image src="srpg-uitest.svg" height=136/> <p/>
<p align="center"> a python game, made from scratch. </center>
<p align="center">
  <image src="https://img.shields.io/github/last-commit/reversee-dev/simplerpg/stable?style=flat-plastic"/>
  <image src="https://img.shields.io/github/repo-size/reversee-dev/simplerpg?style=flat-plastic"/>
  <image src="https://img.shields.io/github/stars/reversee-dev/simplerpg?style=social"/>
  <image src="https://img.shields.io/badge/python-3.10-blueviolet?style=flat-plastic"/>
  <image src="https://img.shields.io/badge/version-uitest-ff69b4?style=flat-plastic"/>
  <image src="https://img.shields.io/badge/stable-ff6ba2?style=flat-plastic"/>
</p>

### Version uitest | Edge
To open UI Test, install requirements using ```python3 -m pip install -r requirements.txt``` and then run ```python3 uitest.py```. This will create new pygame window with sample ui, and working buttons.  

## NOTE
From now on development of simplerpg-stable/unstable will be paused.   
It will be only continued on ```uitest``` branch, the only updates that ```stable``` will recieve, are small patches for bugs, that would lead to game crashing / softlocking / beeing unplayable.  
This state also applies to modloader, and will be removed upon uitest beeing stable.   
**This also marks a new era for the game, as it will be relying on ```pygame``` and ```pygame_ui```! Thank you for reading, the rest is optional.**  

Auto Installer for packages is **already done in stable launcher** and will be enabled in the future on stable branch.  
If you wish to enable it earlier, here are the instructions:
* download latest stable build 
* open ```lib/randomthings.py``` and set ```game.enforceModules``` to ``True``
* open ```launcher.py``` and set ```modules``` to **list** of modules. eg. ```modules = [pygame, pygame_ui]```
* you also need to set imports inside ```try, except``` below modules to catch if user already installed required modules

Also when you just enable ```enforceModules``` without changing anything else, it will install and import ```climage```, which will display srpg logo inside launcher! I bet you didn't notice when you were reading source code for some reason ( good luck on that btw ).
