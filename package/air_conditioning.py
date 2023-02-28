from package.power_consuption import PowerConsumption
#used for the air conditioning: heeters, fans, AC units 
class AirConditioning(PowerConsumption):

    _category = 'Air Conditioning'

        #constructor
    def __init__(self, appliance_name):
        self._name = appliance_name

# to be implemented...