import PyLidar3
import math
import time
import cv2
import numpy as np

class Lidar:

    def __init__(self):
        self.port = "/dev/ttyUSB0"
        self.Obj = PyLidar3.YdLidarX4(self.port)

    def StartScan(self):
        data = self.Obj.StartScanning()
        return data

    def StopScan(self):
        self.Obj.StopScanning()
        self.Obj.Disconnect()


    def Dessiner(self, image, lidar_data, center=None, scale=1):
        if center is None:
            center = (image.shape[1] // 2, image.shape[0] // 2)

        for i in range(360):
            angle = math.radians(i)
            distance = lidar_data.get(i, 0)

        # Ensure distance is within a reasonable range
            if distance < 0 or distance > 1200:  # Adjust 1200 to match your scale
                continue

        # Calculate the x, y coordinates
            x = int(center[0] - distance * math.sin(angle)  * scale)
            y = int(center[1] + distance * math.cos(angle) * scale)
            print(f"Angle: {i}, Distance: {lidar_data.get(i, 0)}, Point: ({x}, {y})")

        # Draw the point if within bounds
            if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
                cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

        return image
    
    def WarningObstacle(self, lidar_data):
        warn = False

        for i in range(180):
            distance = lidar_data.get(i, 0)

            if distance < 0 or distance > 1200:
                warn = True
        
        return warn
