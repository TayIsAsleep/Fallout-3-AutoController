try:
    import psutil,fileinput,sys,os,time
    from pyglet.input import get_joysticks as getJoysticks 
    def checkIfProcessRunning(processName):
        '''
        Check if there is any running process that contains the given name processName.
        '''
        for proc in psutil.process_iter(): # Iterate over the all the running process
            try: # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False
    def replaceAll(file,searchExp,replaceExp):
        '''
        Replaces words in a text file with other words.
        '''
        for line in fileinput.input(file, inplace=1):
            if searchExp in line:
                line = line.replace(searchExp,replaceExp)    
            sys.stdout.write(line)
    def getFromINI(nameOfSetting):
        '''
        Gets a setting from the autocontroller.ini file, and returns the value next to it
        '''
        global settingName,settingSetTo
        if nameOfSetting in settingName:
            a = settingSetTo[settingName.index(nameOfSetting)]
            if a.lower() == "true":
                return True
            if a.lower() == "false":
                return False
            return a
        return None
    def setControllerSupportTo(trueOrFalse):
        '''
        Does what it says on the tin. Requires 'prefFileLocation' to be set.
        '''
        global prefFileLocation
        if trueOrFalse:
            replaceAll(prefFileLocation,"bDisable360Controller=1","bDisable360Controller=0")
            print("Controller support is now set to ON")
        else:
            replaceAll(prefFileLocation,"bDisable360Controller=0","bDisable360Controller=1")
            print("Controller support is now set to OFF")

    # Prints out ASCII text and version number
    with open("autocontrollerText.txt","r") as f:
        for x in f.readlines():
            print(x.strip("\n"))
    print("(v0.9.2)\n")
    
    # Loads ini file
    settingName,settingSetTo=[],[]
    with open("autocontroller.ini", "r") as f:
        for x in f.readlines():
            if "=" in x and not (x.startswith("#") or x.strip() == ""):
                a = x.split("=")
                settingName.append(a[0])
                settingSetTo.append(a[1].strip("\n"))

    # Checks for debugmode
    debugMode = getFromINI("debug")
    debugModeOn = False
    if debugMode != None:
        debugModeOn = debugMode

    # Gets the location of the 'FalloutPrefs.ini' file from 'autocontroller.ini'
    prefFileLocation = getFromINI("prefsFileLocation").strip()

    # Checks if prefFileLocation is set correctly, and that it ends with "FalloutPrefs.ini"
    if prefFileLocation == r"C:\Users\EXAMPLE_USERNAME\Documents\My Games\Fallout3\FalloutPrefs.ini" or not prefFileLocation.endswith("FalloutPrefs.ini"):
        input("ERROR! : 'prefsFileLocation' was not set correctly in 'autocontroller.ini'. Check your ini file!")

    # Here you could put your own checks:
    doCheckSteamLink = getFromINI("checkForSteamLink")
    doCheckController = getFromINI("checkForController")

    # Check if SteamLink is connected to computer
    steamLinkConnected = False
    if doCheckSteamLink:
        print("Checking if Steam Link is connected...")
        steamLinkConnected = checkIfProcessRunning("steam_monitor.exe")
        if steamLinkConnected:
            print("Steam Link is connected.\n")
        else:
            print("Steam Link is not connected.\n")
    
    # Check if a controller is connected to computer
    controllersConnected = False
    if doCheckController:
        print("Checking if any controllers are connected to the computer...")
        controllersConnected = len(getJoysticks()) > 0
        if controllersConnected:
            print("One or more controllers detected.\n")
        else:
            print("No controllers detected.\n")

    if doCheckController == False and doCheckSteamLink == False:
        print("\nAll checks are off, will not change any settings.")
    else:
        setControllerSupportTo((doCheckSteamLink and steamLinkConnected) or (doCheckController and controllersConnected))
        
    # Launches FalloutLauncher2.exe
    nameOfExe = getFromINI("originalLauncherName").strip()
    waitTime = getFromINI("waitTime")
    if waitTime == None:
        waitTime = 1
    else:
        waitTime = int(waitTime.strip())
    if waitTime > 0:
        print(f"\nStarting {nameOfExe} in {waitTime} secound...")
        time.sleep(waitTime)
    if debugModeOn:  
        input("\nDEBUG MODE IS ON. PRESS ENTER TO LAUNCH GAME LIKE NORMAL.")
    os.startfile(nameOfExe)

except Exception as e:
    input("GENERAL ERROR! : " + str(e))