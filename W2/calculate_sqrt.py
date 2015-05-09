#Kakali Mahapatra
#calculate suare root of a number

def main():
	import math
	print("Calculate square root of a range of numbers")
	x = eval(input("Please enter your first whole number: "))
	y = eval(input("Please enter your second whole number: "))
	print("Number: ", "square root: ")
	sqrt = 0
	for number in range(x,y+1):
		sqrt = math.sqrt(number)
		print(number,"     ", sqrt)
		
main()
