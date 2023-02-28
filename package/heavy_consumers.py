from package.power_consuption import PowerConsumption
# used for heavy power consumers in the household: ovens,stoves,boilers, washing mashines, dryers. etc.
class HeavyConsumers(PowerConsumption):
    _category = 'Heavy power consumers'
        #constructor
    def __init__(self, appliance_name):
        self._name = appliance_name

    # returns a dictionary of the household appliance  
    def get_bill(self, power, work_time):
        power_consumption = power*work_time
        return {'type': self._category,
                'appliance': self._name, 
                'power consumption': power_consumption,
                'amount': power_consumption*self._pricePerkWh}
