# The variable "car" is set to the int 100.
cars = 100
# The variable "space_in_a_car" is set to the float 4.0.
space_in_a_car = 4
# The variable "drivers" is set to the int 30.
drivers = 30
# The variable "passengers" is set to the int 90.
passengers = 90
# The variable cars_not_driven is set to the result of "cars" minus "drivers"
cars_not_driven = cars - drivers
# The variable "cars_driven" is set to the variable "drivers"
cars_driven = drivers
# The variable "carpool_capacity" is set to "cars_driven" times "space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car
# The variable "average_passengers_per_car" is set to "passengers" devided by "cars_driven"
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avaiable."
print "There are only", drivers, "drivers avaiable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
