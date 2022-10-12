#achivo por editar
salir=False
a=0
p=''
cont=0
cont1=0
cont2=0
while not salir:
    print ("==============")    
    print (" EDUCATE-ONLINE")
    print ("==============")
    print ("1. Programación: $250.000")
    print ("2. Bases de datos: $310.000")
    print ("3. Robotica: $280.000")
    print ("4. Salir")
    print ("==============")
    opcion=input("Elija un curso: ")
    if (opcion=="1"):
        cont=cont+1
        nombreCompleto = input("ingrese su nombre completo:")
        rut = input("ingrese su rut")
        cupon=input("¿Usted tiene algun cupón EDUCATE-ONLINE?")

        if cupon=="si":
            descuento=a*0.8
            cont1=cont1+1
            p='Programación'
        if cupon=="no":
            cont2=cont2+1
        else:
            print("opcion invalida")

    continue

    if (opcion=="2"):
        cont=cont+1
        nombreCompleto = input("ingrese su nombre completo:")
        rut = input("ingrese su rut")
        cupon=input("¿Usted tiene algun cupón EDUCATE-ONLINE?")

        if cupon=="si":
            descuento=a*0.8
            cont1=cont1+1
            p='Programación'
        if cupon=="no":
            cont2=cont2+1
        else:
            print("opcion invalida")
            
    continue

    if (opcion=="3"):
        cont=cont+1
        nombreCompleto = input("ingrese su nombre completo:")
        rut = input("ingrese su rut")
        cupon=input("¿Usted tiene algun cupón EDUCATE-ONLINE?")

        if cupon=="si":
            descuento=a*0.8
            cont1=cont1+1
            p='Programación'
        if cupon=="no":
            cont2=cont2+1
        else:
            print("opcion invalida")

    continue

    print("CLIENTE: "+nombreCompleto)
    print("Cantidad de cursos comprados: "+cont)
    print("Cantidad de cursos comprados con descuentos: "+cont1)
    print("Cantidad de cursos comprados sin descuentos: "+cont2)

    if (opcion=="4"):
        salir=True
    else:
        print ("Opcion invalida...Intente de nuevo")
        input("Presione Enter para continuar...!")
