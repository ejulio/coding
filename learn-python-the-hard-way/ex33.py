def generate_numbers(max, step):
	i = 0
	numbers = []
	while i < max:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	return numbers
	
def print_numbers(numbers):
	print "The numbers: "
	for num in numbers:
		print num
		
print_numbers(generate_numbers(10, 2))
print_numbers(generate_numbers(15, 3))