from package.power_consuption import PowerConsumption

class AirConditioning(PowerConsumption):
    _heeting = 0
    _cooling = 0
    _name = ''
        #constructor
    def __init__(self, appliance_name):
        self._name = appliance_name

    def set_power_output(self,heeting,cooling):
        self._heeting = heeting
        self._cooling = cooling

    def get_bill(self):
        if self._power == 0 or self._working_time == 0:
            print('Plese enter appliance power[kW] & usual working time [h]')
            return 0
        elif self._heeting == 0 or self._cooling:
            print('Plese enter heeting & cooling output [kW]')
        else:
            return {
                'type': type(self),
                'appliance': self._name, 
                'power consumption':self._power * self._working_time * self._pricePerkWh,
                'output':{
                'heeting':self._heeting,
                'cooling':self._cooling}}
