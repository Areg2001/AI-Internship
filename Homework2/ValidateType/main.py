"""Main module"""

from person import Person

person1 = Person()

person1.age = 15                               #correct
person1.height = 1.4                           #correct
person1.tags = ["Tall man", "So smart"]        #correct
person1.favorite_foods = ["Egg", "Fish"]       #correct

print(person1.age)
print(person1.height)
print(person1.tags)
print(person1.favorite_foods)

person1.age = 1.3                   #incorrect
person1.height = 1                  #incorrect
person1.tags = "Tall"               #incorrect
person1.favorite_foods = "Fish"     #incorrect