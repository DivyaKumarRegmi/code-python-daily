#random module provides a way to generate random numbers and perform random operations

import random

#random.randint() returns a random integer between the specified range
random_integer=random.randint(1,10)
print(random_integer)

#shuffle() shuffles the elements of a list in place
my_list=[1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

#random.choice() returns a random element from a non-empty sequence
my_list=[1,2,3,4,5]
random_choice=random.choice(my_list)
print(random_choice)

#random.sample() returns a list of unique elements chosen from the specified sequence
my_list=[1,2,3,4,5]
random_sample=random.sample(my_list,3)
print(random_sample)

#random.random() returns a random float between 0 and 1
random_float=random.random()
print(random_float)

#random.uniform() returns a random float between the specified range
random_float=random.uniform(1,10)
print(random_float)

#random.seed() initializes the random number generator
random.seed(1)
random_integer=random.randint(1,10)
print(random_integer)

#random.randrange() returns a randomly selected element from the specified range
random_integer=random.randrange(1,10)
print(random_integer)

#random.getrandbits() returns a random integer with the specified number of bits
random_integer=random.getrandbits(3)
print(random_integer)

#random.getstate() returns the current state of the random number generator
state=random.getstate()
print(state)

#random.setstate() sets the state of the random number generator
random.setstate(state)
random_integer=random.randint(1,10)
print(random_integer)

#selecting a sample from a population
population=[1,2,3,4,5,6,7,8,9,10]
sample_size=3
sample=random.sample(population,sample_size)
print(sample)

