def count_to(count):
	"""Our iterator implementation"""
	
	#Our list
	numbers_in_japanese = ["一", "二", "三", "四", "五"]

	#Our built-in iterator
	#Creates a tuple such as (1, "一")
	iterator = zip(range(count), numbers_in_japanese)
	
	#Iterate through our iterable list
	#Extract the Japanese numbers
	#Put them in a generator called number
	for position, number in iterator:
		
		#Returns a 'generator' containing numbers in Japanese
		yield number
#Let's test the generator returned by our iterator
for num in count_to(3):
	print("{}".format(num))
	
for num in count_to(4):
    print("{}".format(num))
	