
class prime_factors:

	def __init__(self):
		self.number = int(input("enter a number : "))
		self.prime_list = []
		self.factor(self.number)

	def check_prime(self,number):
		prime = True
		for j in range(2,number):
			if number%j == 0:
				prime = False
				break
		else:
			self.prime_list.append(number)

	def factor(self,number):
		for i in range(2,number+1):
			if number%i == 0:
				self.check_prime(i)


if __name__ == '__main__':
	fact = prime_factors()
	print(f"prime factors are\n{fact.prime_list}")
