<p align="center"> <image src="srpg.svg" height=136/> <p/>
<p align="center"> a python game, made from scratch. </center>
<p align="center">
  <image src="https://img.shields.io/github/last-commit/reversee-dev/simplerpg/stable?style=flat-plastic"/>
  <image src="https://img.shields.io/github/repo-size/reversee-dev/simplerpg?style=flat-plastic"/>
  <image src="https://img.shields.io/github/stars/reversee-dev/simplerpg?style=social"/>
  <image src="https://img.shields.io/badge/python-3.10-blueviolet?style=flat-plastic"/>
  <image src="https://img.shields.io/badge/v2.3a-ff6ba2?style=flat-plastic"/>
</p>

### Version v2.3 | Stable
To open the launcher, run ```python3 launcher.py``` in your terminal!  

To Mod stuff, check out [modloader](https://github.com/reversee-dev/srpg-modloader), and [modrepo](https://github.com/reversee-dev/srpg-modrepo)!   
You can also create your own mods! ~~The wiki will soon be updated!~~ wiki will not be updated anymore. check out ~~[this](https://reversee-dev.github.io/simplerpg/) (under construction)~~ nah this not good, probably will come back to wiki  

### Quick Instruction
 * q, w, e - action 1, 2 ,3 
 * r - Action 4 ( often back / exit )
 * t, y - other actions that aren't currently implemented / will be implemented in mods or future updates
 * capital Z or X will exit game if not using getch() as input
 * When HP is 0, you lose.

## NOTE ABOUT FUTURE
don't read crossed text... i'm to lazy to write ui for this game :)  

~~From now on development of simplerpg-stable/unstable will be paused.~~  
~~It will be only continued on ```uitest``` branch, the only updates that ```stable``` will recieve are be small patches for bugs, that would lead to game crashing / softlocking / beeing unplayable.~~  
~~This state also applies to modloader, and will be removed upon uitest beeing stable.~~  
~~**This also marks a new era for the game, as it will be relying on ```pygame``` and ```pygame_ui```! Thank you for reading, the rest is optional.**~~  

Auto Installer for packages is **already done in stable launcher** so you can mess around with it!   
If you wish to enable it earlier, here are the instructions:
* download latest stable build 
* open ```lib/randomthings.py``` and set ```game.enforceModules``` to ``True``
* open ```launcher.py``` and set ```modules``` to **list** of modules. eg. ```modules = [pygame, pygame_ui]```

Also when you just enable ```enforceModules``` without changing anything else, it will install and import ```climage```, which will display srpg logo inside launcher! I bet you didn't notice when you were reading source code for some reason ( good luck on that btw ).

### Versions
 * Launcher Update ( v2.3a ) - May 29, 2022 **- > [download]() (latest)**
 * Ai & World Update ( v2.2a ) - January 6, 2022 **- > [download](https://github.com/reversee-dev/simplerpg/releases/tag/2.2a-stable)**
 * Quick Fixes ( v2.1a ) - January 5, 2022 **- > [download](https://github.com/reversee-dev/simplerpg/releases/tag/2.1a-stable)**
 * Village Core ( v2a ) - December 14, 2021 **- > [download](https://github.com/reversee-dev/simplerpg/releases/tag/2a-stable)**
 * Battle Engine ( v1.4a-unstable ) - November 21, 2021 **- > [download](https://github.com/reversee-dev/simplerpg/releases/tag/1.4a-unstable)**
### Branches
 * stable - Most stable branch, it is where the release are made!
 * unstable - not so stable, but playable ( i think )
 * edge - don't touch that! it is broken all the time - **NOT CREATED YET** 
 * *test - eg. villagetest, it is testing branch for some major things that aparently need entirely diffrent code, and then i will have trouble merging it into unstable... 
