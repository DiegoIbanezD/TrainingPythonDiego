if __name__ == '__main__':

	Exercise_List = ["Bool", "Loop"]

	Check_List = []

	def Exercise_Bool(what):
		result = False
		x = 2
		y = 3
		output = (x == y)
		if output == False:
			result = True
			Check_List.append(what)
		print(f'Result is {result}')

	print("Which Exercise do you want to Check?")

	for i in Exercise_List:
		print(i)


	def Evaluation_Process():
		Corrector_Choice = input()

		if Corrector_Choice == Exercise_List[0]:
			print(f'Let\'s run Exercise {Corrector_Choice}')
			Exercise_Bool(Corrector_Choice)
		elif Corrector_Choice == Exercise_List[1]:
			print(f'Sorry didn\'t do Exercise {Corrector_Choice}')
		else:
			print("Process ended")

		if Check_List:
			for i in Check_List:
				print("Check List: " + i)
		else:
			print('Check List is empty')

	Evaluation_Process()
