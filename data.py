
class Drive:
    def __init__(self,name,d_type,state,power,dcvoltage):
        self.name = name
        self.d_type = d_type
        self.state = state
        self.power = power
        self.dcvoltage = dcvoltage
    
    def getName(self):return self.name
    def getType(self):return self.d_type
    def getState(self):return self.state
    def getPower(self):return self.power
    def getDcVoltage(self):return self.power
        

class PLCConnection:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port