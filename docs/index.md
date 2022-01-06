<p align="center"> <image src="srpg.svg" height=136/> <p/>
<p align="center"> a python game, made from scratch. </p>
<p align="center">
  <image src="https://img.shields.io/github/last-commit/reversee-dev/simplerpg/stable?style=flat-plastic"/>
  <image src="https://img.shields.io/github/repo-size/reversee-dev/simplerpg?style=flat-plastic"/>
  <image src="https://img.shields.io/github/stars/reversee-dev/simplerpg?style=social"/>
  <image src="https://img.shields.io/badge/python-3.10-blueviolet?style=flat-plastic"/>
  <image src="https://img.shields.io/badge/version-2.2a-ff69b4?style=flat-plastic"/>
  <image src="https://img.shields.io/badge/stable-ff6ba2?style=flat-plastic"/>
</p>

<p>Welcome traveler to this simple rpg game built with python!<br/>Its point is to make a stable rpg game engine with using as little external packages as possible! <br /> </p> 
<h2>Download</h2>
<p>Here are all version for downloads (github releases):</p><br />
<li>Ai & World Update ( v2.2a ) - January 6, 2022 <strong>- > <a href="https://github.com/reversee-dev/simplerpg/releases/tag/2.2a-stable">download</a> (latest) </strong></li>
<li>Quick Fixes ( v2.1a ) - January 5, 2022 <strong>-  <a href="https://github.com/reversee-dev/simplerpg/releases/tag/2.1a-stable">download</a></strong></li>
<li>Village Core ( v2a ) - December 14, 2021 <strong>- &gt; <a href="https://github.com/reversee-dev/simplerpg/releases/tag/2a-stable">download</a></strong></li>
<li>Battle Engine ( v1.4a-unstable ) - November 21, 2021 <strong>- &gt; <a href="https://github.com/reversee-dev/simplerpg/releases/tag/1.4a-unstable">download</a></strong>

    
<h2>NOTE ABOUT FUTURE</h2>
<p>From now on development of simplerpg-stable/unstable will be paused.</p>
<p> It will be only continued on <code>uitest</code> branch, the only updates that <code>stable</code> will recieve are small patches for bugs, that would lead to game crashing / softlocking / beeing unplayable.</p></br>
<p>This state also applies to modloader, and will be removed upon uitest beeing stable.</p>
<p><strong>This also marks a new era for the game, as it will be relying on <code>pygame</code> and <code>pygame_ui</code> Thank you for reading, rest is optional.</strong></p></br></br>

<p>Auto Installer for packages is **already done in stable launcher** and will be enabled in the future on stable branch.</p>  </br>
<p>If you wish to enable it earlier, here are the instructions:</p></br>
<li>download latest stable build </li>
<li>open <code>lib/randomthings.py</code> and set <code>game.enforceModules</code> to <code>True</code></li>
<li>open <code>launcher.py</code> and set <code>modules</code> to <strong>list</strong> of modules. eg. <code>modules = [pygame, pygame_ui]</code></li>
<li>you also need to set imports inside <code>try, except</code> below modules to catch if user already installed required modules</li></br>

<p>Also when you just enable <code>enforceModules</code> without changing anything else, it will install and import <code>climage</code> which will display srpg logo inside launcher! I bet you didn't notice when you were reading source code for some reason ( good luck on that btw ).</p>


<h2>Branches</h2>
<li>stable - Most stable branch, it is where the release are made!</li>
<li>unstable - not so stable, but playable ( i think ) - <strong>NOT CREATED YET</strong></li>
<li>edge - don&#39;t touch that! it is broken all the time - <strong>NOT CREATED YET</strong> </li>
<li>*test - eg. villagetest, it is testing branch for some major things that aparently need entirely diffrent code, and then i will have trouble merging it into unstable... </li>

<h3 id="soon-more-">Soon, more!</h3>
