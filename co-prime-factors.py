import time

class factor:
	"""this programme is for finding the co-prime factors of a number
	if n = p * q  then p and q must be a co-prime number
	here we take n as a input, p and p are our output

	"""

	def __init__(self):
		self.number = input("enter a number : ")
		self.start = time.time()
		if self.number != "quit":
			self.co_prime_factor = []
			factor.check_factor(self,int(self.number))		

	def number_list(self,number):
		num_list = []
		for i in range(2,int(number**(1/2))+1):
			if number%i == 0:
				num_list.append(i)
				num_list.append(number//i)
		num_list.append(number)
		return num_list

	def check_coprime(self,num1,num2):
		num1_list = self.number_list(num1)
		num2_list = self.number_list(num2)
		coprime = True
		for i in num1_list:
			if i in num2_list:
				coprime = False
				break
		if coprime == True:
			self.co_prime_factor.append((num1,num2))

	def check_factor(self,num):
		for i in range(2,int(num**(1/2))+1):
			if num%i == 0 :
				self.check_coprime(i,num//i)

print("you can type 'quit' to exit")
while True:
	co_primes  = factor()
	if co_primes.number == 'quit':
		break
	print(f"all co-prime factors of {co_primes.number} are \n{co_primes.co_prime_factor}")
	print(f"time taken = {time.time() - co_primes.start}secs..")
