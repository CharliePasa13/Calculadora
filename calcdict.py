def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2

calc= {
    '+': suma,
    '-': resta,
    '*': multiplicacion,
    '/': division
}
def start():
    while True:
        select = input('> ')
        if select:
            try:
                (num1, op, num2) = select.split(' ')
                print('El resultado es:')
                print(calc [op](int(num1), int(num2)))
            except ZeroDivisionError:
                print('No se puede dividir entre 0')
            else:
                otra = input('Desea realizar otra operacion? S/N: ')
                if otra == ('s' or 'S'):
                    start()
                else:
                    print('Gracias por usar la calculadora, hasta luego!')
                    exit()
start()