
class prime:

	def __init__(self,number):
		self.not_prime = True
		while self.not_prime == True:
			self.not_prime = self.check(number)
			if self.not_prime == True:
				number -= 1

		self.large_prime = number
		

	def check(self,number):
		if number%2==0:
			return True
		for i in range(3,int(number**(1/2))+1,2)	:
			if number%i==0:
				return True
		else:
			return False



if __name__ == "__main__":
	number_ = int(input("enter a number : "))
	prime_ = prime(number_)
	print(f"largest prime is {prime_.large_prime}")