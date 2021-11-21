def main():
	average_n = calc_average()
	determine_grade()

def calc_average():
	n1 = int(input('Введите 1 оценку: '))
	n2 = int(input('Введите 2 оценку: '))
	n3 = int(input('Введите 3 оценку: '))
	n4 = int(input('Введите 4 оценку: '))
	n5 = int(input('Введите 5 оценку: '))
	return 'Средниий балл от 5 оценок равен:', (n1+n2+n3+n4+n5) / 5

def determine_grade():
	if average_n > 4.5:
		print('Ваша оцена A', 'Ваш средний балл'+str(average))
	elif average > 3.5:
		print('Ваша оцена B', 'Ваш средний балл'+str(average))
	elif average > 2.5:
		print('Ваша оцена C', 'Ваш средний балл'+str(average))

main()