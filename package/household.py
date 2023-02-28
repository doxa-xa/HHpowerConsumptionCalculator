class Household:
    _household = {}
    # creates a household room for power consumers data dictionaries
    def set_new_room(self,room_name):
        self._household[room_name] =[]
    #removes a household room with the power consumers in it
    def remove_room(self,room_name):
        del self._household[room_name]
    #adds power consumers to the room
    def add_to_room(self,room_name, consumer):
        self._household[room_name].append(consumer)
    #removes consumer from room
    def remove_from_room(self,room_name,consumer):
        del self._household[room_name][consumer]  
    # gets the bill of power consumption per room
    def get_room_bill(self,room_name):
        total = 0.0
        consumers = [consumer for consumer in self._household[room_name]]
        amount = [consumer['amount'] for consumer in consumers ]
        for bill in amount:
            total = total + bill

        return total
    

