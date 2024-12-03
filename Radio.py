#pour class Radio
import serial
import time


class radio:

    #initialization
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.port = '/dev/ttyACM0'
        self.ser.baudrate = 115200
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.timeout = 1
        self.ser.open()

    def obtenir_position(self):
        self.ser.write(b'lep\n')
        time.sleep(0.1)
        data = self.ser.readline().decode('utf-8')
        _, x, y, z, _ = data.split(',')
        return float(x), float(y), float(z) 