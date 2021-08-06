from rcon import Rcon

rcon = Rcon('127.0.0.1', 25575, 'qwerty')

with rcon:
    rcon('say hello')