import gpiozero

class robot:

    def __init__(self):
        self.vitesse = 1
        self.IN1 = gpiozero.DigitalOutputDevice(6)
        self.IN2 = gpiozero.DigitalOutputDevice(5)
        self.IN3 = gpiozero.DigitalOutputDevice(15)
        self.IN4 = gpiozero.DigitalOutputDevice(14)
        self.ENA = gpiozero.PWMOutputDevice(13)
        self.ENB = gpiozero.PWMOutputDevice(18)
        self.IRG = gpiozero.LineSensor(23)
        self.IRD = gpiozero.LineSensor(24)

    def Avancer(self):
        self.IN1.on()
        self.IN2.off()
        self.ENA.value = self.vitesse
        self.IN3.on()
        self.IN4.off()
        self.ENB.value = self.vitesse

    def Reculer(self):
        self.IN1.off()
        self.IN2.on()
        self.ENA.value = self.vitesse
        self.IN3.off()
        self.IN4.on()
        self.ENB.value = self.vitesse

    def Freiner(self):
        self.IN1.on()
        self.IN2.on()
        self.ENA.value = self.vitesse
        self.IN3.on()
        self.IN4.on()
        self.ENB.value = self.vitesse
    
    def avancerTournerGauche(self):
        self.IN1.on()
        self.IN2.on()
        self.ENA.value = self.vitesse
        self.IN3.on()
        self.IN4.off()
        self.ENB.value = self.vitesse

    def avancerTournerDroite(self):
        self.IN1.on()
        self.IN2.off()
        self.ENA.value = self.vitesse
        self.IN3.on()
        self.IN4.on()
        self.ENB.value = self.vitesse

    def TournerGauche(self):
        self.IN1.off()
        self.IN2.on()
        self.ENA.value = self.vitesse
        self.IN3.on()
        self.IN4.off()
        self.ENB.value = self.vitesse

    def TournerDroite(self):
        self.IN1.on()
        self.IN2.off()
        self.ENA.value = self.vitesse
        self.IN3.off()
        self.IN4.on()
        self.ENB.value = self.vitesse
    
    def UpdateVit(self):
        self.ENA.value = self.vitesse
        self.ENB.value = self.vitesse