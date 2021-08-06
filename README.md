# Minecraft Rcon - python

## General info
Simple python script made using sockets, to connect with Minecraft server using RCON.

## Setup
Clone the repository
```
git clone https://github.com/jkuryloo/rcon-python-minecraft.git
```
Create new python file, and import Rcon class, then initialize the class with your server info
```python
from rcon import Rcon
rcon = Rcon('127.0.0.1', 25575, 'qwerty')
```
Use the script using 'with'
```python
#example.py
from rcon import Rcon
rcon = Rcon('127.0.0.1', 25575, 'qwerty')
with rcon:
  rcon('say hello')
```
or
```python
from rcon import Rcon
rcon = Rcon('127.0.0.1', 25575, 'qwerty')
rcon.connect()
rcon('say hello')
rcon.disconnect()
```
