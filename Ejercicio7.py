#pedir correo, mostrar todo igual pero despues del @ceu.es
mail = input('Introduzca su correo electrónico ')

splitmail = mail.split('@')

print(splitmail[0]+'@ceu.es')