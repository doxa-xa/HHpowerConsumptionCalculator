from package.power_consuption import PowerConsumption
from package.lighting import Lighting
from package.media import Media
from package.heavy_consumers import HeavyConsumers
from package.household import Household

lighting = Lighting('lights',27)

lights_bill = lighting.get_bill(0.015,8)

print(lights_bill)

electronics = Media('Electronics', 11)

electronics_bill = electronics.get_bill(0.3,8)

print(electronics_bill)

fridge = HeavyConsumers('fridge')
oven = HeavyConsumers('oven')
stove = HeavyConsumers('stove')
boiler = HeavyConsumers('boiler')
dishwasher = HeavyConsumers('dishwasher')

frige_bill = fridge.get_bill(2,24)
oven_bill = oven.get_bill(2.5,2)
stove_bill = stove.get_bill(3,2)
boiler_bill = boiler.get_bill(3,2)
dishwasher_bill = dishwasher.get_bill(1.5,4)

home = Household()

home.set_new_room('kitchen')

home.add_to_room('kitchen',frige_bill)
home.add_to_room('kitchen',oven_bill)
home.add_to_room('kitchen',stove_bill)
home.add_to_room('kitchen',boiler_bill)
home.add_to_room('kitchen',dishwasher_bill)

print(home.get_room_bill('kitchen',30))
print(home.get_room_power_consumption('kitchen',30))






# print(frige_bill)
# print(oven_bill)
# print(stove_bill)
# print(boiler_bill)
# print(dishwasher_bill)


