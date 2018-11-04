#Prueba del metodo de division con el error previsto de 0
def division(num1, num2):
    try: num1 / num2
    except ZeroDivisionError:
        print('Error: No se puede dividir entre 0')
    else:
        return num1 / num2

resultado = division(num1=6, num2=3)
resultado2 = division(num1=6, num2=0)
print (f' El resultado de la division es: {resultado}')
print (f' El resultado de la division es: {resultado2}')