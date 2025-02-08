# PhasTimer
A timer for Phasmophobia, take time from using smudgesticks till the hunt begins.

DISCLAIMER: I dont have money for a certificate, which means that when you try to run the app for the first time you will have to click "More info" and then click "Run anyways".

If you dont trust the application you can build it yourself or read through the code in this repo.

### Download:
https://github.com/zhiftyDK/phastimer/releases/tag/PhasTimer

### Changing keybind and color:
When running the app for the first time a config.ini file will be generated:
```
[DEFAULT]
keybind = r
color = #32CD32
```
* Default keybind is r (The current version of PhasTimer can only do single key binds. YOU CANT DO: ctrl+r etc.)
* Default color is lime green (Takes any hex color value)

When the config.ini file is configured to you liking, then you should just be able to open Phasmophobia and PhasTimer.

### Build the .exe yourself:
Build command:
```bash
pyinstaller main.py --onefile --noconsole --add-data="stopwatch.ico;images" --icon=stopwatch.ico --name=PhasTimer
```