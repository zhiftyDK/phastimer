import os
import time
import keyboard
import threading
import tkinter as tk
import configparser
config = configparser.ConfigParser()

# Set default config if no config.ini file exists
config["DEFAULT"] = {
    "Keybind": "r",
    "Color": "#32CD32"
}

if not os.path.exists("config.ini"):
    with open("config.ini", "w") as configfile:
        config.write(configfile)

config.read("config.ini")

root = tk.Tk()
root.title("PhasTimer")
path_to_data = os.path.abspath(os.path.join(os.path.dirname(__file__),"images"))
root.iconbitmap(path_to_data+"\\stopwatch.ico")
root.attributes("-alpha",0.0)
top = tk.Toplevel(root)
top.overrideredirect(1) #removes border but undesirably from taskbar too (usually for non toplevel windows)
top.wm_attributes("-transparentcolor", root["bg"])
top.wm_attributes("-topmost", 1)
top.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

#toplevel follows root taskbar events (minimize, restore)
def onRootIconify(event): top.withdraw()
root.bind("<Unmap>", onRootIconify)
def onRootDeiconify(event): top.deiconify()
root.bind("<Map>", onRootDeiconify)

timer = tk.StringVar()
timerlabel = tk.Label(top, textvariable=timer, font=("System", 40, "bold"), fg="#32CD32", highlightthickness=0)
timerlabel.pack(side=tk.TOP, anchor=tk.NE, padx=30, pady=20)
timer.set("00.0")

timerStarted = False
def startTimer():
    seconds = 0
    while True:
        if not timerStarted:
            break
        seconds += 0.1
        timestring = time.strftime(f"%M:%S", time.gmtime(seconds))
        timestring = timestring.split("00:")[1] if "00:" in timestring else timestring[1:]
        timer.set(timestring + "." + str(seconds).split(".")[1][0])
        time.sleep(0.1)

def toggleTimer(e):
    global timerStarted
    if timerStarted:
        timerStarted = False
        timer.set("00.0")
    else:
        timerStarted = True
        t = threading.Thread(target=startTimer, args=())
        t.daemon = True
        t.start()

keyboard.on_press_key(config["DEFAULT"]["Keybind"], toggleTimer)

top.mainloop()