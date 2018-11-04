#esto define el metodo de suma
def suma(num1, num2):
    return num1 + num2

#esto define el metodo de resta
def resta(num1, num2):
    return num1 - num2

#esto define el metodo de multiplicacion
def multiplicacion(num1, num2):
    return num1 * num2

#esto define el metodo de division
def division(num1, num2):
    return num1 / num2

#esto define el metodo de la calculador
def calculadora():
    print('Seleccione una operación:')
    print('1.Suma')
    print('2.Resta')
    print('3.Multiplicación')
    print('4.División')

#esto crea el metodo para que se repita
def start():
    calculadora()

#esta es la pregunta inicial
    seleccion = input('Digite el numero de la opción deseada: ')

#estas son la opciones a elegir
    opciones = ('1','2','3','4')

#si la seleccion se encuentra dentro de opciones pide digitar el primer valor sino da el error y pregunta si quiere volver a intentar
    if seleccion in opciones:
        num1 = float(input('Digite el primer valor: '))
        num2 = float(input('Digite el segundo valor: '))
    else:
        retry = input("Selección no válida. Volver a intentar? S/N: ")
        if retry == ('s' or 'S'):
            start()
        else:
            print('Gracias por usar la calculadora, hasta luego!')
            exit()

#esto define que metodo se llama al seleccionar los numeros asignados previamente
    if seleccion == '1':
        print(num1, '+', num2, '=', suma(num1,num2))
    elif seleccion == '2':
        print(num1, '-', num2, '=', resta(num1, num2))
    elif seleccion == '3':
        print(num1, '*', num2, '=', multiplicacion(num1, num2))
    elif seleccion == '4':
        try:
            num2 == 0
            print(num1, '/', num2, '=', division(num1, num2))
        except ZeroDivisionError:
            print('**Error!! No se puede dividir entre 0**')
        else:
            pass

#crea el loop para seguir ejecutando mas operaciones, sino simplemente termina el codigo
    otra = input('Desea realizar otra operacion? S/N: ')
    if otra == ('s' or 'S'):
        start()
    else:
        print('Gracias por usar la calculadora, hasta luego!')
        exit()


start()

