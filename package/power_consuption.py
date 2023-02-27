class PowerConsumption:
    _pricePerkWh = 0.21
    _working_time = 0
    _power = 0
    _bill = 0

    def __init__(self,appliance_name):
        self._name = appliance_name
    def set_appliance(self, power,working_time):
        power = self._power
        working_time = self._worikng_time

    def get_bill(self):
        if self._power == 0 or self._working_time == 0:
            print('Plese enter appliance power')
            return 0
        else:
            return {'appliance': self._name, 'power consumption':self._power * self._working_time * self._pricePerkWh}

