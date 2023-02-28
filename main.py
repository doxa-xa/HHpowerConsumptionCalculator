from household_calculator.power_consuption import PowerConsumption
from household_calculator.lighting import Lighting
from household_calculator.media import Media
from household_calculator.heavy_consumers import HeavyConsumers
from household_calculator.household import Household
from household_calculator.exports import Save

lighting = Lighting('lights',27)

lights = lighting.get_appliance(0.015,8)

print(lights)

electronics = Media('Electronics', 11)

media = electronics.get_appliance(0.3,8)

print(media)

fridge = HeavyConsumers('fridge')
oven = HeavyConsumers('oven')
stove = HeavyConsumers('stove')
boiler = HeavyConsumers('boiler')
dishwasher = HeavyConsumers('dishwasher')

frige_bill = fridge.get_appliance(2,24)
oven_bill = oven.get_appliance(2.5,2)
stove_bill = stove.get_appliance(3,2)
boiler_bill = boiler.get_appliance(3,2)
dishwasher_bill = dishwasher.get_appliance(1.5,4)

home = Household()

home.set_new_room('kitchen')

home.add_to_room('kitchen',frige_bill)
home.add_to_room('kitchen',oven_bill)
home.add_to_room('kitchen',stove_bill)
home.add_to_room('kitchen',boiler_bill)
home.add_to_room('kitchen',dishwasher_bill)

kitchen_consumption = home.get_room('kitchen')

Save.to_csv(kitchen_consumption,'Kitchen.csv')
Save.to_json(kitchen_consumption,'Kitchen.json')
print(home.get_room_bill('kitchen',30))
print(home.get_room_power_consumption('kitchen',30))




# print(frige_bill)
# print(oven_bill)
# print(stove_bill)
# print(boiler_bill)
# print(dishwasher_bill)


