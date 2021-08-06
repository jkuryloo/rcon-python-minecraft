from rcon import Rcon

rcon = Rcon('127.0.0.1', 25575, 'qwert')

with rcon:
    rcon('say hello')