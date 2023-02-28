from household_calculator.power_consuption import PowerConsumption
# used for frequently used household electronics like: TV, soud systems, PC, phones, tablets, etc.
# usually low voltage DC chargables

class Media(PowerConsumption):
    #constants
    _voltage = 5 #typucal USB phone charger voltage
    _current = 2 #typical USB phone/tablet charger current
    _cosfi = 0.96 #simulates the cosine of the phase angle ~ 90° 
    _category = 'media'
    _charging_time = 1.5 # average charging time [hours] for typical phone, tablet, battery pack etc.

    #constructor - the default number of chargables is 0 you can update
    #at will with the constructor`s second public parameter 
    def __init__(self, appliance_name, chargers=0):
        self._name = appliance_name
        self._chargers = chargers

    # setter for charging time - changes default charging time 
    def change_default_charging_time(self,time):
        self._charging_time = time

    # returns a dictionary of the household appliance  
    def get_appliance(self, power, work_time):
        chargers_consumption = round((self._voltage * self._current * self._cosfi)/1000 ,2)
        power_consumption = round(power*work_time, 2)
        return {
            'type': self._category,
            'appliance': self._name, 
            # will be 0 if you dont specify chargers in the constructor
            'chargers consumption':chargers_consumption* self._chargers * self._charging_time, 
            'power_consumption':round(power_consumption + chargers_consumption, 2),
            'amount':round(power_consumption * self._pricePerkWh ,2)
        }
    

