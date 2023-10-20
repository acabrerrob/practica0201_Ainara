name = input('Introduzca el nombre del artículo ')
price = float (input ('Introduzca el precio del producto '))
units = int (input ('Introduzca el número de unidades '))

totalPrice = price * units

formatPrice = "{:010,.2f}".format(price)
formatUnits = "{:03d}".format(units)
formatTotalPrice = "{:,.2f}".format(totalPrice)

print('El nombre del producto es: ', name)
print('El precio unitario es de: ', formatPrice, '€')
print('El número de unidades: ', formatUnits, 'uds')
print('El coste total es de: ', formatTotalPrice, '€')