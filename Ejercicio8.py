price = input ('Introduzca el precio en euros con 2 decimales ')

splitprice = price.split('.')

print('Usted ha introducido ', splitprice[0], 'euros y ', splitprice[1], 'céntimos')