from package.power_consuption import PowerConsumption

class Media(PowerConsumption):
    #constants
    _voltage = 5 #typucal phone charger voltage
    _current = 2 #typical phone charger current
    _cosfi = 0.96 #simulates the cosine of the phase angle ~ 90° 
    _category = 'media'
    _charging_time = 1.5

    #constructor
    def __init__(self, appliance_name, chargers=0):
        self._name = appliance_name
        self._chargers = chargers

    def change_default_charging_time(self,time):
        self._charging_time = time

    def get_bill(self, power, work_time):
        chargers_consumption = round((self._voltage * self._current * self._cosfi)/1000 ,2)
        power_consumption = round(power*work_time, 2)
        return {
            'type': self._category,
            'appliance': self._name, 
            'chargers consumption':chargers_consumption* self._chargers * self._charging_time,
            'power_consumption':round(power_consumption + chargers_consumption, 2),
            'amount':round(power_consumption * self._pricePerkWh ,2)
        }
    

