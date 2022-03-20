import os 
os.system("cls")

intentos=3
contador=0

usuario="angie"
contraseña="anbermo"

lista=[]

a = input("Por favor, ingrese su usuario: ").lower()

while a != usuario:
    print("\nEL usuario no es correcto")
    a=input("Por favor, ingrese de nuevo su usuario: ")

b = input("\nPor favor, ingrese su contraseña: ")
while intentos>0:
    intentos=intentos-1 
    
    if b != contraseña:
        print("Su contraseña no es correcta")
        b=input("Por favor, ingrese de nuevo su contraseña: ")
        break

    while True:
        if b==contraseña:  
            print("""\nBienvenido al cajero automatico de la region: 
        1.Depositar dinero a la cuenta
        2.Sacar dinero de la cuenta
        3.Ver saldo
        4.Salir""")
            opcion=input("\nPor favor, escoja una opcion: ")

            comprobar=opcion.isdigit()
            if comprobar==True:
                if opcion=="1":
                    print("\nDigite la cantidad de dinero que desea depositar: ")
                    deposito=input()
                    veridepo=deposito.isdigit() 
                    if veridepo==True:
                        deposito=int(deposito)
                        contador=contador+deposito  
                        lista.append(["\nSu movimiento fue de:" ,deposito]) 
                        print("\nSu saldo actual es de:", contador)
                    else:
                        print("\nEl monto que desea depositar es incorrecto")
                        
                if opcion=="2":
                    print("\nDigite la cantidad de dinero que desea retirar: ")
                    retiro=input()
                    veridepo=retiro.isdigit()    
                    if veridepo==True:
                        
                        retiro=int(retiro)
                        if retiro%1000==0:
                            if retiro<contador:
                                contador=contador-retiro  
                                lista.append(["\nSu movimiento fue de:" ,retiro]) 
                                print("\nSu saldo actual es de: ", contador)
                            else:
                                print("\nNo cuentas con los fondos necesarios")
                        else:
                            print("\nLa cantidad que desea retirar es incorrecta")
                    else:
                        print("\nLa cantidad es incorrecta")

                if opcion=="3":
                    print("\nSu saldo es de: ", contador)
                    for x,y in lista:
                        print(x,y)
                if opcion=="4":
                    print("\nGracias por utilizar nuestro cajero")
                    exit()
            else:
                print("\nEsta opcion no se encuentra disponible")

print("\nEl sistema se bloqueo, solo puede ingresar la contraseña tres veces")

 




    



