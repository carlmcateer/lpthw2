## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
    pass

## Dog is-a object and is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a object and is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object.
class Person(object):

    def __init__(self, name):
        ## Person has-a name.
        self.name = name

        ## Person has-a pet of some kind.
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a Object
class Fish(object):
    pass

## Salmon is-a Object and is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Object and is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a Pet called Satan
mary.pet = satan

## frank is-a Employee, frank has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a Pet called Rover
frank.pet = rover

## Fliper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
