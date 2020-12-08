try:
    import psutil,fileinput,sys,os,time
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
        with open("autocontroller.ini", "r") as f:
            allLines = f.readlines()
            settingName = []
            settingSetTo = []
            for x in allLines:
                a = x.split("=")
                settingName.append(a[0])
                settingSetTo.append(a[1])
            try:
                return settingSetTo[settingName.index(nameOfSetting)].strip("\n")
            except:
                input(f"ERROR : Could not find setting called {nameOfSetting} in 'autocontroller.ini'. Press Enter to continue anyways.")
                return None

    with open("autocontrollerText.txt","r") as f:
        for x in f.readlines():
            print(x.strip("\n"))
    print("")
    
    fallout3PrefsFileLocation = getFromINI("prefsFileLocation").strip()
    # Here you could put your own checks
    print("Checking if steam link is connected... (aka if 'steam_monitor.exe' is running)")
    steamLinkIsConnected = checkIfProcessRunning("steam_monitor.exe")
    print("Is steam link connected? :",steamLinkIsConnected)

    if steamLinkIsConnected:
        replaceAll(fallout3PrefsFileLocation,"bDisable360Controller=1","bDisable360Controller=0")
        print("I changed bDisable360Controller to 0 (Controller support is now ON)")
    else:
        replaceAll(fallout3PrefsFileLocation,"bDisable360Controller=0","bDisable360Controller=1")
        print("I changed bDisable360Controller to 1 (Controller support is now OFF)")
    
    print("Starting game in 1 secound...")
    time.sleep(1)
    os.startfile("FalloutLauncher2.exe")
except Exception as e:
    input("ERROR! : " + str(e))