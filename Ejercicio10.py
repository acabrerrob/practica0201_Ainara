list = input('Introduzca la lista de la compra separando cada artículo por comas')

splitlist = list.split(',') 

for listItem in  splitlist:
    print(listItem)