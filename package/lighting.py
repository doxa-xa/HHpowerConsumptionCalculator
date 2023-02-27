from package.power_consuption import PowerConsumption

class Lighting(PowerConsumption):
    _bulbs = 0
    _name =''
        #constructor
    def __init__(self, appliance_name):
        self._name = appliance_name

    def set_bulbs(self,bulbs):
        self._bulbs = bulbs

    def get_bill(self):
        if self._power == 0 or self._working_time == 0:
            print('Plese enter appliance power[kW] & usual working time [h]')
            return 0
        else:
            return {
                'type': type(self),
                'appliance': self._name, 
                'power consumption':self._power * self._working_time * self._bulbs * self._pricePerkWh,
                'bulbs':self._bulbs
                }