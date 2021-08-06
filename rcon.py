import socket
import struct
from random import randint

class MessageType:
    INVALID_AUTH = -1
    RESPONSE = 0
    COMMAND = 2
    LOGIN = 3

class RconException(Exception):
    pass

class Rcon:
    socket = None 

    def __init__(self, host: str, port: int, password: str):
        self.host = host
        self.port = port 
        self.password = password

    def __call__(self, command: str):
        self.send(MessageType.COMMAND, f'/{command}')

    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, type, value, tb):
        self.disconnect()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.send(MessageType.LOGIN, self.password)

    def disconnect(self):
        if self.socket is not None:
            self.socket.close()
            self.socket = None

    def read(self, length: int):
        data = b''
        while len(data) < length:
            data += self.socket.recv(length - len(data))
        return data

    def send(self, type: int, data: str):
        if self.socket is None:
            raise RconException('Connect before sending data.')
        id = randint(0, 2147483647)
        packet_data = struct.pack("<ii", id, type) + data.encode('utf8') + b"\x00\x00"
        packet = struct.pack("<i", len(packet_data))
        self.socket.send(packet + packet_data)

        in_msg = ""
        in_length, = struct.unpack("<i", self.read(4))
        in_data = self.read(in_length)

        if not in_data.endswith(b"\x00\x00"):
            raise RconException('Invalid data')

        in_type, in_req_id = struct.unpack("<ii", in_data[:8])
        if in_type == MessageType.INVALID_AUTH:
            raise RconException('Bad login.')
        
        in_msg = in_data[8:-2].decode("utf8")
        return in_msg