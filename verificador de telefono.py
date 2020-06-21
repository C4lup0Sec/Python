'''  introducir un numero de telefono de longitud de 13 caracteres con la siguente estructura
(81)8345-9824

'''
def num_tel():
    a=str(input("Ingrese su numero telefonico: "))
    list(a)
    int(a[1])
    int(a[2])
    int(a[4])
    int(a[5])
    int(a[6])
    int(a[7])
    int(a[9])
    int(a[10])
    int(a[11])
    int(a[12])
    if a[0]!="(":
        print("Un digito no es valido")
        num_tel()
    elif a[3]!=")":
        print("Un digito no es valido")
        num_tel()
    elif a[8]!="-":
        print("Un digito no es valido")
        num_tel()
    else:
        print("su numero es correcto\n")  
        b=int(input("si deseas ingresar otro numero ingrese 1, sino ,ingresa otro numero "))  
        if b==1:
            num_tel()
num_tel()