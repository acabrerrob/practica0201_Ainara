birth = input('Introduzca su fecha de nacimiento con el siguiente formato: dd/mm/aaaa ')

splitbirth = birth.split('/')

print('Usted nació el día ' + splitbirth[0] + ' del mes '+ splitbirth[1] + ' del año ' + splitbirth[2])