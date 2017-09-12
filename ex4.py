#it means there are 100 cars
cars=100
#it means each car can carry 4 people
space_in_a_car=4
#the number represendent there are 30 drivers
drivers=30
#and the count of passengers is 90
passengers=90
#the number of cars is more than drivers, so the cars without dribers is just cars-drivers
cars_not_driven=cars-drivers
#since the reason above, the cars with driver is just the number of drivers 
cars_driven=drivers
#it means the capacity of the cars which has l driver to drive
carpool_capacity=cars_driven*space_in_a_car
#it means how many passengers we shuold put into each car today.
average_passengers_per_car=passengers/cars_driven 


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transprot", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car." 
