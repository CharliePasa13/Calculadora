def test_suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def calculadora():
    print('Seleccione una operación')
    print('1.Suma')
    print('2.Resta')
    print('3.Multiplicación')
    print('4.División')

def start():
    calculadora()

    seleccion = input('Digite la operacion seleccionada: ')
    assert 1 == seleccion
    opciones = ('1','2','3','4')

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

    otra = input('Desea realizar otra operacion? S/N: ')
    if otra == ('s' or 'S'):
        start()
    else:
        print('Gracias por usar la calculadora, hasta luego!')
        exit()


start()

