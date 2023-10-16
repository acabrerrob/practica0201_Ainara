nombre= input('Introduzca su nombre completo')
nuevastr=''

print(nombre.lower())
print(nombre.upper())

splitnombre=nombre.split() #separo cada letra

for x in range(splitnombre):
    nuevastr+= x[0]

print(nuevastr.upper())
