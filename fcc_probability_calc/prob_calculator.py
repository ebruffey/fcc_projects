#        __________              __________
#       /          \            /          \
#      /____{()}____\          /____{()}____\
#     |----|    |----|        |----|    |----|
#     |{()}|    |{()}|   VS   |{()}|    |{()}|
#     \ ~~ / $$ \ ~~ /        \ ~~ / $$ \ ~~ /
#      \  /  $$  \  /          \  /  $$  \  /
#       \/  $$$$  \/            \/  $$$$  \/
#       ||        ||            ||        ||
#  @MVM@ \________/              \________/ @MVM@
#       \ \//____/                \____\\/ /
#       / //                            \\ \
#       \//                              \\/

import copy
import random 

#class to hold the variables and do the experiments
class Hat: 

	#inititation bringing in all elements being whats in the hat
	def __init__(self, **all_elements):

		#create a list to hold each hat item
		self.contents = []

		for (key, val) in all_elements.items():
			#nested loop to loop through how many times each item 
			#occurs in the hat
			for number in range(val):
				#append to contents each occurence
				self.contents.append(key)

		print(self.contents)

	#method to draw a certain number of items from the hat
	def draw(self, amount):

		#list to hold which items were drawn
		drawn = []

		#check if the amount is greater than the contents
		#and if it is return the list
		if amount > len(self.contents):
			return self.contents

		#iterate through the range of the amount input
		for num in range(amount):
			#hold the random element popped from self.contents, pop
			#removes the element from the list
			holder = self.contents.pop(random.randrange(len(self.contents)))
			#then append the holder to the drawn list
			drawn.append(holder)	

		#doesnt work for some reason, i guess it doesnt remove from
		#the original list whereas above using pop it does
		#else:
			#drawn = random.sample(self.contents, amount)
			#self.contents =

		return drawn
		#for numb in range(amount):

	#defines the experiment and takes in  values
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

	#keeps track how many positive occurences
	pos_occur = 0

		#experiment loop
	for i in range(num_experiments):
			#create a deepcopy of the hat 
		hat_copy = copy.deepcopy(hat)
			#then create a list of the drawn items from that hat
		temp_drawn_list = hat_copy.draw(num_balls_drawn)

		breaker = True
			#then loop through the expected balls dict to compare
		for (key, val) in expected_balls.items():
			#then check if the count of the specific keys are 
			#less than the values in the expected
			if temp_drawn_list.count(key) < val:
				#if it is then we turn the boolean to false
				#and break out of the inner for loop
				breaker = False 
				break
		#if our breaker ended up being true then we
		#add one to the pos_occur
		if breaker:
			pos_occur += 1
	#return the probability!
	return pos_occur / num_experiments



