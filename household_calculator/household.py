#used for grouping the household power consumers in rooms 
from household_calculator import exports
class Household:
    # static properties:
    _household = {}

    #returns the household dictionary with the current room lists
    def get_household(self):
        return self._household

    # creates a household room for power consumers data dictionaries
    def set_new_room(self,room_name):
        self._household[room_name] =[]

    #retuns current room list of power consumers
    def get_room(self,room_name):
        return self._household[room_name]

    #removes a household room with the power consumers in it
    def remove_room(self,room_name):
        del self._household[room_name]

    #adds power consumers to the room
    def add_to_room(self,room_name, consumer):
        self._household[room_name].append(consumer)

    #removes consumer from room
    def remove_from_room(self,room_name,consumer):
        for item in self._household[room_name]:
            if item['consumer'] == consumer:
                del self._household[room_name]
                break

    # gets the bill of power consumption per room per day 
    # add function second parameter in [days] to get weekly,montly yearly totals
    def get_room_bill(self,room_name,days=1):
        total = 0.0
        consumers = [consumer for consumer in self._household[room_name]]
        amount = [consumer['amount'] for consumer in consumers ]
        for bill in amount:
            total = total + bill

        return total*days
    
    # gets the power consumption per room per day 
    # add function second parameter in [days] to get weekly,montly yearly totals   
    def get_room_power_consumption(self,room_name,days=1):
        total = 0.0
        consumers = [consumer for consumer in self._household[room_name]]
        power_consumption = [consumer['power consumption'] for consumer in consumers ]
        for power in power_consumption:
            total = total + power

        return total*days
    

