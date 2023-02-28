class PowerConsumption:
    _pricePerkWh = 0.21

    def __init__(self,appliance_name):
        self._name = appliance_name

    def set_pricePerkWh(self,price):
        price = self._pricePerkWh

    def get_pricePerkWh(self):
        return self._pricePerkWh

    def get_bill(self, power, work_time):
        power_consumption = power*work_time
        return {'appliance': self._name, 
                'power consumption': power_consumption,
                'amount': power_consumption*self._pricePerkWh}

