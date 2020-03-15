class Engine:
    def __init__(self, redline:int, torqueCurve):
        '''
        Creates an Engine object.
        
        :param redline: Maximimum RPM the engine can run at
        :param torqueCurve: Function that returns torque in Nm given RPM
        '''

        self.redline = redline
        self._torque = torqueCurve
    
    @staticmethod
    def FromEnglishUnits( redline, torqueCurve):
        return Engine(redline, lambda x: torqueCurve(x) / 0.738)

    def Torque(self, rpm, throttle):
        return self._torque(rpm) * throttle

    def Power(self, rpm, throttle):
        return self.Torque(rpm, throttle) * rpm / 9.5488

    def EnglishTorque(self, rpm, throttle):
        '''
        Returns engine torque in ftlb

        :param rpm: Engine speed in RPM
        '''

        return self.Torque(rpm, throttle) * 0.738
    
    def HorsePower(self, rpm, throttle):
        return self.EnglishTorque(rpm, throttle) * rpm / 5252

class Transmission:
    def __init__(self, gearRatios:list, finalGearRatio):
        self.speeds = len(gearRatios) - 1
        self.currentGear = 0
        self.gears = [x*finalGearRatio for x in gearRatios]

    def CurrentRatio(self):
        return self.gears[self.currentGear]
    
    def CurrentOutputRPM(self, rpm):
        return rpm / self.CurrentRatio()

    def UpShift(self):
        if self.currentGear < self.speeds:
            self.currentGear += 1
        else:
            self.currentGear = self.speeds
    
    def DownShift(self):
        if self.currentGear > 0:
            self.currentGear -= 1
        else:
            self.currentGear = 1

class Drivetrain():
    def __init__(self, engine:Engine, transmission:Transmission):
        self.engine = engine
        self.transmission = transmission
        self.transmission.currentGear = 0

    def Torque(self, rpm, throttle):
        return self.engine.Torque(rpm, throttle) * self.transmission.CurrentRatio()