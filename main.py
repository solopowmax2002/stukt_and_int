class Pump:
    def pump_action(self):
        pass

class BasePump(Pump):
    def __init__(self, pump_type):
        self.type = pump_type

    def pump_action(self):
        print(self.type, "насос")

class PlungerPump(BasePump):
    def pump_action(self):
        print(self.type, "насос делает плунжерное движение")

class CentrifugalPump(BasePump):
    def pump_action(self):
        print(self.type,"насос вращается по центробежной схеме")

plunger_pump = PlungerPump("Плунжерный")
centrifugal_pump = CentrifugalPump("Центробежный")

pumps = [plunger_pump, centrifugal_pump]

for pump in pumps:
    pump.pump_action()
