from itertools import cycle
#https://www.registrocivil.cl/PortalOI/Manuales/Validacion_de_Run.pdf

def verificador_run(Run):
    num_Run,verificador = Run.split('-')

    if verificador.lower() == 'k':
        verificador = 10

    Run_inverso = map(int,reversed(str(num_Run)))
    factores = cycle(range(2,8))

    S = sum(i*n for i, n in zip(Run_inverso,factores))
    Ri = S % 11
    Rf = 11 - Ri

    if Rf == 11:
        Rf = 0

    if Rf == int(verificador):
        print(Rf)
        print(verificador)
        return True
    else:
        return False

Run = input('Ingresar rut con el \'-\' : ')
valido = verificador_run(Run)

if valido == True:
    print('\nEl rut es valido')
else:
    print('\nEl rut no es valido')