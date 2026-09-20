# PICO SET UP

hold down the `BOOTSEL` button and plug in the cable at the same time to activate. The Pico `RPI-RP2` Should open.

# MICRO PYTHON

Install MicroPython for RaspberryPI Pico here:

```
https://micropython.org/download/RPI_PICO_W/
```

Donwload the `latest .uf2 firmware`. Move the `.uf2` file to the `RPI-RP2` Pico folder and wait a few seconds. The
`RPI-RP2` folder should automatically disappear, this means the firmware has been installed.


# VS CODE TOOLS

In VS code, Go to VS code extensions, with `CTRL+SHIFT+X` or navigate with the mouse to the left. Search `MicroPico` and install
the extension by `Paulober`.

# RECONNECT THE PICO

Pull the cable out of the pico and plug it back in without holding the bootsel buttom this time. It wont be obivous that windows detects it. To be sure the pico is detected, you can go to Windows `Device Manager` and expand the `PORTS (COM & LPT)` drop down. The pico should appear there with a name similar to `USB Serial Device (COM5)`. You can also unplug the pico with the drop down menu open to see what disappears, which will indicate that the one that disappeared is the pico.

# CONFIGURE VS CODE MICROPYTHON

In VS code, press `CTRL+SHIFT+P` to open VS code preferences, and type `MicroPico`, Choose `MicroPico: Initialize MicroPico Project`.
This should open the MicroPico terminal, and create some configuration files in the workspace directory. That MicroPico terminal
is a on the raspberryPI. It is usefull for individual commands.

# UPLOADING CODE

Create any python file, for example, run in power shell `code main.py`, and save it with `CTRL+S`. Paste this code in:

```
import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)

print("Pico has booted!")

while True:
    led.toggle()
    print("Heartbeat")
    time.sleep(2)
```

Then press `CTRL+SHIFT+P` and search `MicroPico: Upload File To Board`. You can then run that file in the
MicroPython terminal with by running `import FILE_NAME`. so if you uploaded a file called `main.py`, you can run it on the board with `import main`.

To check what files are on the board run:
```
import os
print(os.listdir())
```
This will show a list of all the files on the pico directory.

# RUNNING ON BOOT
main.py is supposed to run on boot when you plug the pico in to a computer.

For some reason the micropico extension on vscode will actually interupt the picos boot file.
This causes prints to not appear in the terminal and loops to break, essentially soft resetting the pico.

The files will only run properly on boot if you plug the pico in with vs code closed, or the micrpico extension is disabled.

Alas all code is written by people and people are kinda stupid.

# PuTTY


If you want to view the terminal outputs of the picos boot scripts, you can use an external service called PuTTY. 

## Step 1
You can install PuTTY here:
```
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
```

Install the 64-bit windows installer, and click next on all the default installation configurations.

## Step 2
Identify the COM port of the Pico, this can be viewed in the device manager under `PORTS (COM & LPT)` when the pico is connected. For my pico it was `COM5`

## Step 3
Plug the pico in and Launch PuTTY.

## Step 4
In the PuTTY Config, under session, select `Serial` as the conneciton type and change the serial line
to your COM port, for me it was `COM5`. Then change the speed to 115200. Then click open.

## Step 5
Enjoy the onboard terminal and all its prints. You can use this terminal like normal.