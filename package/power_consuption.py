#parent class for any house hold appliances. 
#There are severeal child classes in the package 
#You can use this to inherit the primary logic if you need anyting more specific

class PowerConsumption:
    # constart for domestic use of power consumption in Bulgaria
    # you can change it with the setter
    _pricePerkWh = 0.21

    #constructor
    def __init__(self,appliance_name):
        self._name = appliance_name

    #price per kWh setter
    def set_pricePerkWh(self,price):
        price = self._pricePerkWh

    #price per kWh getter
    def get_pricePerkWh(self):
        return self._pricePerkWh
    
    # returns a dictionary of the household appliance  
    def get_bill(self, power, work_time):
        power_consumption = power*work_time
        return {'appliance': self._name, 
                'power consumption': power_consumption,
                'amount': power_consumption*self._pricePerkWh}

