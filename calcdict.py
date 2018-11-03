def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

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