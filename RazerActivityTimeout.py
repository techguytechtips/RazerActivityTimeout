from openrazer.client import DeviceManager
from time import sleep, time
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener

devman = DeviceManager()
print("Found {} Razer devices".format(len(devman.devices)))
devicesOff = False
timer = time()
def setDevices(value):
    for device in devman.devices:
        if device.type == "mouse":
            device.brightness = value
            device.fx.misc.logo.brightness = value
            device.fx.misc.scroll_wheel.brightness = value
        else:
            device.brightness = value


def on_press(key):
    global timer
    global devicesOff
    timer = time()
    if devicesOff:
        setDevices(100)
        devicesOff = False

def on_move(x, y):
    global timer
    global devicesOff
    timer = time()
    if devicesOff:
        setDevices(100)
        devicesOff = False


KeyboardListener(on_press=on_press).start()
MouseListener(on_move=on_move).start()


while(True):
    #print(time() - timer, end='\r')
    if time() - timer > 25:
        timer = time()
        if not devicesOff:
             setDevices(0)
        devicesOff = True



