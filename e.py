from abc import ABC, abstractmethod

class SmartDevice(ABC):
    @abstractmethod
    def operate(self):
        pass

class Light(SmartDevice):
    def operate(self):
        print("Light turned ON")

class Fan(SmartDevice):
    def operate(self):
        print("Fan started")

# Example
devices = [Light(), Fan()]
for d in devices:
    d.operate()
