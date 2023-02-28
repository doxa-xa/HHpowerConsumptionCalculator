from household_calculator.power_consuption import PowerConsumption
# used for household lighting enter the number of light sources (bulbs) in a room or a household

class Lighting(PowerConsumption):
    _category = 'lighting'

    #constructor
    def __init__(self, appliance_name, bulbs):
        self._name = appliance_name
        self._bulbs = bulbs
    # returns a dictionary of the household appliance   
    def get_appliance(self,power,work_time):
        power_consumption = power * work_time * self._bulbs
        return {
            'type': self._category,
            'appliance': self._name, 
            'bulbs':self._bulbs,
            'power consumption':round(power_consumption, 2),
            'amount':round(power_consumption * self._pricePerkWh ,2)
            }