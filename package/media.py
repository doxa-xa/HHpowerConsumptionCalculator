from package.power_consuption import PowerConsumption
from random import random

class Media(PowerConsumption):
    _chargers = 0 #number of chargers
    _name =''
    #constants
    _voltage = 5 #typucal phone charger voltage
    _current = 2 #typical phone charger current
    _cosfi = random.random(0.9, 0.97) #simulates the cosine of the phase angle ~ 90° 

    #constructor
    def __init__(self, appliance_name):
        self._name = appliance_name

    def set_chargers(self, num):
        self._chargers = num

    def get_charging_consumption(self):
        chargers_consumption = self._chargers * self._voltage * self._current * self._cosfi
        return {
            'type': type(self),
            'appliance': self._name, 
            'power consumption':self._power * self._working_time * self._pricePerkWh,
            'chargers_consumption': chargers_consumption
        }