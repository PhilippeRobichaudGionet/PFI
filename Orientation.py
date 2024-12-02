import threading
import time
from icm20948 import ICM20948
import numpy as np
imu = ICM20948()

class Orient:
        
    def __init__(self):
        self.next = True
        self.StateThread = threading.Thread(target=self.Execute)
        #Louka Janelle
        self.Precedent = []
        self.TempsPrecedent = time.perf_counter()
        self.AngleX = 0
        self.MYList = []
        self.MZList = []
        ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()
        self.precendentGx = gx
        self.Precedent.append(gx)

    def Start(self):
        self.Initiate()
        self.StateThread.start()