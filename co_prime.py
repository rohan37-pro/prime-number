class prime:

	def number_list(number):
		num_list = []
		for i in range(2,number+1):
			if number%i == 0:
				num_list.append(i)
		return num_list


	def check_coprime(num1,num2):
		num1_list = prime.number_list(num1)
		num2_list = prime.number_list(num2)
		coprime = True
		for i in num1_list:
			if i in num2_list:
				coprime = False
				break

		if coprime == True:
			print(f'number {num1} and {num2} are coprime')
		else:
			print(f"sorry broo!!!! \nnumber {num1} and {num2} are not co-prime")


while True:
	mode = input("what do you want check co-prime(c)/quit(q) : ")
	if mode == 'c':
		num1 = int(input("enter 1st number : "))
		num2 = int(input("enter 2nd number : "))
		
		prime.check_coprime(num1,num2)

	if mode == "q":
		break