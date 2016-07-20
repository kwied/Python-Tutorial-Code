## Dog is-a animal
class Dog(Animal):

	def _init_(self, name):
		##Dog has a name
		self.name = name

## Cat is-a animal
class Cat(Animal):

	def _init_(self,name):
		## Cat has-a name
		self.name = name

## Person is-a object

	def _init_(self, name):
		##Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

##The person is-a employee
class Employee(Person):

	def _init_(self, name, salary):
		## hmm what is this? 
		super(Employee, self)._init_(name)
		## The person has-a salary
		self.salary = salary

## The fish is-a object
class Fish(object):
	pass

##Salmon is-a fish
	pass

## Halibut is a fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

##Satan is a cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary has-a pet
mary.pet = satan

## Frank is-a employee
frank = Employee("Frank, 120000)

## Frank has-a pet
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## crous is-a fish
crouse = Salmon()

## Hary is-a fish
harry = Halibut()
