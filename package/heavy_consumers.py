from package.power_consuption import PowerConsumption

class HeavyConsumers(PowerConsumption):
    _name = ''
        #constructor
    def __init__(self, appliance_name):
        self._name = appliance_name