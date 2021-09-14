class prime:

	def check_prime(self,num):
		for i in range(2,num):
			if num%i == 0:
				print(f"sorry broo!!!! \nthe number {num} is not a prime number")
				break
		else:
			print(f"number {num} is prime ###~~~")




while True:
	mode = input("select -  check prime(p)/quit(q) : ")
	if mode == 'p':
		num = int(input("enter a number : "))
		prime123 = prime()
		prime123.check_prime(num)

	if mode == "q":
		break
