
from lib.libsave import *
from lib.libinput import getch
from lib.randomthings import *
from lib.console import *
import time, sys, os, json

clearConsole()

# create default save file if not found
if not (os.path.isfile("s0.pkl")) or not os.path.isfile("s0_seed.pkl") or not os.path.isfile("s0_sstock.pkl"):
    from new_save import createDefaultSaveFile
    createDefaultSaveFile()

if game.debugPrints: print("\nLoading default save file: \"s0.pkl\"")
player = smanager.load("s0.pkl") # load player save data to local variable

if game.enforceModules == True: # if game modules are enforced in lib/randomthings.py
    install_action(game.enforcedModulesList)

def settings(): # settings menu
    while True:
        out("\nSettings:")
        out(" - 1 - Update", 'green')
        out(" - 2 - Delete save file", 'green')
        out(" - q - Back", 'green')
        out(" - r - Restart", 'green')
        a = getch()
        if a == "q": return;
        if a == "r": exit();
        if a == "1":
            ota.update_interface()
        if a == "2":
            os.remove('s0_seed.pkl')
            os.remove('s0_sstock.pkl')
            os.remove('s0.pkl')
            out("\nSave file deleted!", "red")
            exit()

def mega_reload():
    import sys
    import lib.console; import lib.libbattle; import lib.libdraw; import lib.libentity; import lib.libinput; import lib.libmagic; import lib.libsave; import lib.randomthings; import lib.worldcore
    del sys.modules['lib.console']; del sys.modules['lib.libbattle']; del sys.modules['lib.libdraw']
    del sys.modules['lib.libentity']; del sys.modules['lib.libinput']; del sys.modules['lib.libmagic']
    del sys.modules['lib.libsave']; del sys.modules['lib.randomthings']; del sys.modules['lib.worldcore']
    # import all the essential libraries
    from lib.console import out, list
    from lib.libinput import getch
    from lib.libsave import smanager
    from lib.randomthings import install_action, whatOS, clearConsole, whatOS, game
    return True

def scanGameScenarios(): # scan game scenarios
    scenarios = [] 
    f = None
    path = 'scenarios/' # path to scenarios
    dirs = os.listdir(path) # list of directories in path
    for d in dirs: # iterate through directories
        files = os.listdir("scenarios/"+d+"/") # list of files in directory
        for f in files: # iterate through files
            if f.endswith('.json'): # if file is json
                scenarios.append(f) # add file to list
    return scenarios # return list of scenarios

def parseGameScenario(scenario): # parse game scenario
    import json # import json 
    c = 4
    if whatOS() == "unix": c = 5
    j = open("scenarios/"+scenario[:len(scenario) - c]+"/"+scenario) # open scenario
    data = json.load(j) # load json
    return data # return data

def loadGameScenario(scenario): # load game scenario
    c = 4
    if whatOS() == "unix": c = 5
    if game.debugPrints: out("\nLoading scenario: "+scenario, 'green') # print debug info if specified in lib/randomthings.py
    sys.path.insert(1, 'scenarios/'+scenario[:len(scenario) - c]+'/') # inster path of scenario to sys.path
    from scenario import a # import scenario as if it was in same folder, because specified in sys.path
    status = a.game() # run scenario - class "a" function "game"
    return status

class pager: # pager class
    def getPage(scenarios, page): # get page
        # put 9 scenarios per page 
        # and return list of scenarios in page
        page +=1 # page starts at 1
        if page == 1: # if page is 1
            spp = scenarios[:9] # get first 9 scenarios
        else: # if page is not 1
            spp = scenarios[(page-1)*9:page*9] # get page scenarios
        return spp # return page

class ota:
    logfile: str
    plosc = 'nochk'
    def mklog(): 
        import datetime
        now = datetime.datetime.now()
        string_builder = now.strftime('%d-%m-%Y_%H-%M-%S')
        string_builder += '-ota.log'
        with open(string_builder, 'w') as f:
            f.write('START OTA LOG on '+now.strftime('%H-%M-%S'))
        ota.logfile = string_builder
    def log(s):
        import datetime
        now = datetime.datetime.now()
        string_builder = now.strftime('%H-%M-%S')
        string_builder += ' > '
        string_builder += str(s)
        with open(ota.logfile, 'a') as f:
            f.write('\n'+string_builder)
    def update_interface():
        pkg_url, nver, status = ota.check()
        if status == 'newest': out(' Already running newest version! Let\'s play! ')
        if status == 'available': out(' A newer version is available (' + nver + ')')
        if status == 'ahead': out(' Woah! You are ahead of time! newest version is ' + nver + ', but you have a newer one!')
        if status == 'unstable': out(' You are riding at the edge! Stay safe!')
        sb = 'Do you'; 
        if not status == 'available': sb += ' still'
        sb += ' want to update? (y/n)'
        out(sb)
            
        uinp = getch()
        if not uinp.lower() == 'y': return
        pkg_loc = ota.download(pkg_url, nver)
        ota.apply(pkg_loc)
            
        out('You may need to relaunch to avoid any problems!')
        out('trying mega_reload', 'red')
        try:
            mega_reload()
        except Exception as e:
            out('MEGA RELOAD EROR: ' + str(e))
    def check():
        ota.log('checking newest version')
        import requests
        version_url = 'https://raw.githubusercontent.com/reversee-dev/simplerpg/stable/ota_version'
        
        newest_version = requests.get(version_url).content.decode().replace('\n',''); 
        compare_ver = float(newest_version[:-1])
        #                   https://github.com/reversee-dev/simplerpg/releases/download/2.2a-stable/srpg.meta
        package_url_base = 'https://github.com/reversee-dev/simplerpg/releases/download/'
        package_url = package_url_base + newest_version + '-stable/update.ota'
        
        if compare_ver == float(game.version):
            ota.log('status: newest')
            status = 'newest'
        elif compare_ver > float(game.version):
            ota.log('status: available')
            status = 'available'
        elif compare_ver < float(game.version):
            if game.stable == True:
                ota.log('status: ahead')
                status = 'ahead'
            if game.stable == False:
                ota.log('status: unstable')
                status = 'unstable'
        else:
            print(status)
            exit()
            status = 'unknown'
                
        return package_url, newest_version, status
    def download(url, ver):
        import requests
        local_filename = 'package_' + ver + '.ota'
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=512): 
                    f.write(chunk)
        return local_filename
    def apply(pkg, force=False):  
        ota.log('start applying from package: ' + str(pkg))
        from hashlib import sha256
        import shutil
        import re
        
        try: os.remove('ota_temp/*') 
        except: pass
        if not os.path.exists(os.curdir + '/ota_temp'):
            ota.log('ota temp not found, creating...')
            os.makedirs(os.curdir + '/ota_temp')
        if not os.path.exists(os.curdir + '/ota_backup'):
            ota.log('ota backup not found, creating...')
            os.makedirs(os.curdir + '/ota_backup')
        
        # unzip ota
        import zipfile
        with zipfile.ZipFile(pkg, 'r') as zip:
            zip.extractall(os.path.join(os.curdir + '/ota_temp'))
        
        ota.log('checking version...')
        try: 
            import ota_temp.lib.randomthings as ip
            ipv = ip.game.version
        except ImportError:
            ipv = 'Unknown'
        out("Current version: " +str(game.version), 'green')
        out("New version: " + ipv, 'yellow')
        if force:
            out(' Do you want to continue? (y/n) ')
            inp = getch()
            if not inp.lower() == 'y': return False
        
        current_file_hashes = {}
        new_file_hashes = {}
        new_files = []
        existing_files = []
        exclude = ['.git', '.github', '__pycache__']
        
          # check for new files
        ota.log('checking for existing files')
        for subdir, dirs, files in os.walk(os.curdir + '/ota_temp'):
            dirs[:] = [d for d in dirs if d not in exclude]
            for file in files:
                new = os.path.join(os.curdir, subdir, file)
                old = '.' + new[12:]
                nold = re.sub(r'simplerpg.*-stable', '', old)
                if os.path.exists(nold):
                    existing_files.append(new)
                    ota.log('file ' + file + ' already exists, adding to list of existing files')
                else:
                    new_files.append(new)
                    ota.log('file ' + file + ' does not exist, adding to list of new files')
        # check what files were changed -> [list]
            # installed
        ota.log('processing hashes from current installation,\n\treading every 512 bytes')
        for subdir, dirs, files in os.walk(os.curdir):
            for file in files:
                hsh = sha256()
                full_file_path = os.path.join(subdir, file) 
                with open(full_file_path, 'rb') as f:
                    for byte_block in iter(lambda: f.read(512), b""):
                        hsh.update(byte_block)
                hsh_ = hsh.hexdigest()         
                ota.log('File: ' + full_file_path + ' -> ' + str(hsh_))
                current_file_hashes[full_file_path] = hsh_
             
             # new
        ota.log('processing hashes from update package,\n\treading every 512 bytes')
        for subdir, dirs, files in os.walk(os.curdir + '/ota_temp'):
            for file in files:
                hsh = sha256()
                full_file_path = os.path.join(subdir, file) 
                with open(full_file_path, 'rb') as f:
                    for byte_block in iter(lambda: f.read(512), b""):
                        hsh.update(byte_block)
                hsh_ = hsh.hexdigest()         
                ota.log('File: ' + full_file_path + ' -> ' + str(hsh_))
                new_file_hashes[full_file_path] = hsh_
        
        
        # this ./ota_temp\simplerpg-2.3a-stable\launcher.py
        # to   ./ota_temp\launcher.py
        # find 'simplerpg-2.3a-stable
        # rm   [:-1]
        
        for file in new_files:
            nfile = file[13:]
            ota.log('Moving NEW file - ' + nfile)
            try: shutil.move(file, nfile)    
            except: out('Failed to move file ' + nfile)
            
        for file in existing_files:
            nfile = file[13:]
            file_c = '.\\' + nfile
            file_n = './ota_temp\\' + nfile
            # backup
            ota.log('Backing up ' + nfile)
            shutil.copy(nfile, 'ota_backup/')
            try:
                if new_file_hashes[file_n] == current_file_hashes[file_c]:
                    ota.log('File: ' + nfile + ' is already at its newest version')
                else:
                    ota.log('Moving NEW file - ' + file + ' -> ' + nfile)
                    try: shutil.move(file, nfile)
                    except: out('Failed to move file ' + nfile)
            except KeyError:
                continue
        return
        
# check for ota
out('Checking for updates...')
ota.mklog()
try: 
    _, _, ota.plosc = ota.check()
    if ota.plosc == 'available': out('New version is available!')
    time.sleep(2)
except Exception as e:
    out('Exception: ' + str(e))
    out('Mirror propably unreachable or invalid installed version')
    time.sleep(1.5)

# pages variable
enablePages = None # disable pages
page_id = 0 # page id
page_ids = 0 # page ids

while True: # menu loop
    clearConsole() # clear console
    out(f"simpleRPG. version: "+ game.version + game.isStable())
    if "climage" in sys.modules: print(climage.convert('assets/srpgmini.png', is_unicode=True))  # logo  if module climage is installed
    
    scenarios = scanGameScenarios() # scan scenarios
    if len(scenarios) > 9: # if more than 9 scenarios
        enablePages = True # enable pages
        # get total pages
        page_ids = len(scenarios) // 9 # get total pages

    out("\nPress i for settings", 'white') # print settings tip
    if ota.plosc == 'available':
        out("Press u to update", 'green') # print settings tip
    
    spp = pager.getPage(scenarios, page_id)  # get page of scenarios
    out("\nScenarios:\n", 'white')
    
    for i in range(len(spp)): # iterate through scenarios
        name = parseGameScenario(spp[i])['name'] # get scenario name
        description = parseGameScenario(spp[i])['description'] # get scenario description
        name_color = parseGameScenario(spp[i])['name_color'] # get scenario name color
        description_color = parseGameScenario(spp[i])['description_color'] # get scenario description color
        out(f"  {i+1}. {name}", name_color) # print scenario name
        out(f"\t{description}", description_color) # print scenario name
    if enablePages: # IF ENABLED PAGES
        out(f"\nPage {page_id+1}/{page_ids+1}") # print page info
        out("Use w/e to change pages.", 'green') # print page info

    (menuinput) = getch() # getch, so dynamic type
    if (menuinput) == 4: continue # if enter is pressed, continue
    if (menuinput) == 'q': break # if q is pressed, break loop
    if (menuinput) == 'i': settings() # if i is pressed, settings menu
    if (menuinput) == 'u' and ota.plosc == 'available': ota.update_interface() # if i is pressed, settings menu
    if enablePages: # IF ENABLED PAGES
        if (menuinput) == 'w':  # if w is pressed
                if not page_ids > page_id:  # if page id is not greater than total pages
                    page_id -= 1 # decrease page id
        if (menuinput) == 'e': # if e is pressed
                if not page_ids <= page_id:     # if page id is not greater than total pages
                    page_id += 1 # increase page id

    maxPick = len(scenarios) # max pick
    #check if menuinput is int
    try: menuinput = int(menuinput) # try to convert to int
    except ValueError: continue # if not int, continue

    if menuinput > maxPick or menuinput < 1: continue # if menuinput is not in range, continue
    else: # if menuinput is in range
        status = loadGameScenario(spp[menuinput-1]) # load scenario
        input('Scenario exited: ' + str(status)) # wait for enter if scenario does not exit already


