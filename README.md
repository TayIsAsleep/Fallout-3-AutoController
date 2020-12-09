# Fallout 3 Auto Controller (F3AC)

This tool is for SteamLink Users that wants the game to switch controller support on when you are using your Link, and off when you aren't.

### How to use:

1. Set the correct path to your `FalloutPrefs.ini` file in `autocontroller.ini`.
2. Change the name of your current `FalloutLauncher.exe` to `FalloutLauncher2.exe`.
3. Copy all of the included files into your Fallout 3 Directory.
4. Run the game like normal trough Steam, or use the new `FalloutLauncher.exe` (You should see a command line before the game starts)

### QnA:

Q: How does it work?

A: F3AC runs before the actual launcher, and it checks if `steam_monitor.exe` is running (`steam_monitor.exe` seems to always be running when a SteamLink is connected) and if it is, it opens your `FalloutPrefs.ini` file, and replaces the line `bDisable360Controller=1` with `bDisable360Controller=0`, and then it boots up the game.

Q: Is this a virus?

A: No, it is not a virus. Odds are that virus detectors will warn you about the EXE file, because it doesn't want you to open random EXE files from the internet. If you don't trust me, then you could check the sourcecode, and use the make.bat file to create your own EXE file. This way you know for sure what is in the EXE.

Q: Does this work with Fallout : New Vegas?

A: With some slight modification, it should work, but I have not tested it yet.