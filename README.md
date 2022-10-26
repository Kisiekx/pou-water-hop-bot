# PouWaterHopBot 💦
##### This project was made in June 2020

This bot plays the waterhop minigame in Pou. This was my very first project in python and a lot can be improved here, but I am not into python at all, maybe when I will get bored in the future I will polish this project. 

<p align="center">
<img  src="https://s4.gifyu.com/images/ezgif-3-f7529caec9.gif" width="400" height="400"  />
</p>

<p align="center"> <i> This is showcase of the first version that worked </i></p>

### How to use

Make sure you have python 3.5 or above installed and python-pip. You can use the command ```pip install -r requirements.txt``` to install the required packages.

Download any emulator, or use ADB to run Pou on it.

You can then run the script using ```python farmer.py``` or ```python main-optimized.py```. Read section below to see what are the differences between them.

To exit, press `G`

### Features

#### Farmer
1) User friendly - setup menu
1) Collect coins
2) Collect clocks (additional time)
3) Idle mode (auto restart)

#### Optimized
1) Script focused on best performance and score (when using you need to adjust windows resolution in script config)

### How it works

The script takes a screenshot of the game window, isolates the Hop two tiles away from Pou and if there is nothing, Pou jumps one tile and then two tiles, if there is Hop, Pou jumps two tiles.

If you are using ```farmer.py```, script also looks for powerups and collects them if possible. At the end it shows you how many coins it had got.

### Disclaimer

This script is for educational purposes only. I am not responsible for any damage or loss that may happen as a result of using this script.
