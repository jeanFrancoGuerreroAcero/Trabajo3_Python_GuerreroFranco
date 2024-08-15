import json

##json de menu
def abrirMenu():
    miJSON=[]
    with open('./menu.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def GuardaditoMenu(miData):
    with open("./empleados.json","w") as outfile:
        json.dump(miData,outfile)

def guardarMenu():
    try:
        with open("menu.json","r") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return []

#json de pagos
def abrirPagos():
    miJSON=[]
    with open('./pagos.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def GuardaditoPagos(miData):
    with open("./empleados.json","w") as outfile:
        json.dump(miData,outfile)

def guardarPagos():
    try:
        with open("pagos.json","r") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return []

#json de pedidos
def abrirPedidos():
    miJSON=[]
    with open('./pedidos.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def GuardaditoPedidos(miData):
    with open("./pedidos.json","w") as outfile:
        json.dump(miData,outfile)

def guardarPedidos():
    try:
        with open("pedidos.json","r") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return []


pedidoos=guardarPedidos()
menuu=guardarMenu()
pagoos=guardarPagos()


print("-----------------------------")
print("--BIENVENIDO A POLIPOLLITOS--")
print("-----------------------------")
print("")
booleano=True
while booleano:
    ##mostrar menu al cliente 
    print("ESTE ES NUESTRO MENU")
    print("")
    mostrarMenu=abrirMenu()
    for i in mostrarMenu:
        print("|",i["categoria"])
        print("|NOMBRE :",i["nombre"])
        print("|PRECIO :",i["precio"])
        print("-------------------")
    print("")

    ##pedirle al cliente que opcion desea realizar
    print("----------------------------")
    print("1. ENTRADA")
    print("2. PLATO FUERTE")
    print("3. BEBIDA")
    queDesea=input("QUE DESEA ORDENAR SEÑ@R: ")

    if queDesea=="1":
        print("")
        print("QUE VA A ORDENAR DE LA SECCION DE ENTRADA")
        mostrarMenu=abrirMenu()
        contador=0
        for i in mostrarMenu:
            if i["categoria"]=="entrada":
                contador=contador+1
                print(contador)
                print("|",i["categoria"])
                print("|NOMBRE :",i["nombre"])
                print("|PRECIO :",i["precio"])
                print("-------------------")
        print("")
        entrada="entrada"
        pedidoGuardar=abrirPedidos()
        queVaApedir=input("QUE DESEA PEDIR?: ")
        print("-Juan Perez")
        print("-Maria Lopez")
        print("-Carlos Gomez")
        print("-Ana Martinez")
        print("-Andres Gomez")
        queCliente=input("QUE CLIENTE ERES: ")
        print("va a pagar ya? ")
        espera=input("si/no: ")
        if espera=="si":
            pagar="pagado"
        if espera=="no":
            pagar="sin pagar"
        
        if queVaApedir=="1":
            pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"entrada",
                        "nombre":"Empanadas Mini",
                        "precio": 9000,
                        "estado":pagar
            }
            pedidoos.append(pedidoAñadido)
            GuardaditoPedidos(pedidoos)
        if queVaApedir=="2":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"entrada",
                        "nombre":"Papas Fritas",
                        "precio": 5000,
                        "estado":pagar
            }
        if queVaApedir=="3":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"entrada",
                        "nombre":"Dedos de Queso",
                        "precio": 11000,
                        "estado":pagar
            }
             
        if queVaApedir=="4":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"entrada",
                        "nombre":"Tostada Francesa",
                        "precio": 10000,
                        "estado":pagar
            }
    if queDesea=="2":
        print("")
        print("QUE VA A ORDENAR DE LA SECCION DE PLATO FUERTE")
        mostrarMenu=abrirMenu()
        contador=0
        for i in mostrarMenu:
            if i["categoria"]=="plato_fuerte":
                contador=contador+1
                print(contador)
                print("|",i["categoria"])
                print("|NOMBRE :",i["nombre"])
                print("|PRECIO :",i["precio"])
                print("-------------------")
        print("")
        entrada="entrada"
        pedidoGuardar=abrirPedidos()
        queVaApedir=input("QUE DESEA PEDIR?: ")
        print("-Juan Perez")
        print("-Maria Lopez")
        print("-Carlos Gomez")
        print("-Ana Martinez")
        print("-Andres Gomez")
        queCliente=input("QUE CLIENTE ERES: ")
        print("va a pagar ya? ")
        espera=input("si/no: ")
        if espera=="si":
            pagar="pagado"
        if espera=="no":
            pagar="sin pagar"
        
        if queVaApedir=="1":
            pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"plato_fuerte",
                        "nombre":"Pasta Bolognesa",
                        "precio": 35000,
                        "estado":pagar
            }
            pedidoos.append(pedidoAñadido)
            GuardaditoPedidos(pedidoos)

        if queVaApedir=="2":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"plato_fuerte",
                        "nombre":"Hamburguesa",
                        "precio": 28000,
                        "estado":pagar
            }
             pedidoos.append(pedidoAñadido)
             GuardaditoPedidos(pedidoos)
        if queVaApedir=="3":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"plato_fuerte",
                        "nombre":"Pollo al Curry",
                        "precio": 30000,
                        "estado":pagar
            }
             pedidoos.append(pedidoAñadido)
             GuardaditoPedidos(pedidoos)     
        if queVaApedir=="4":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"plato_fuerte",
                        "nombre":"Lechona",
                        "precio": 25000,
                        "estado":pagar
            }
             pedidoos.append(pedidoAñadido)
             GuardaditoPedidos(pedidoos)
        if queVaApedir=="5":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"plato_fuerte",
                        "nombre":"Arroz al Wok",
                        "precio": 20000,
                        "estado":pagar
            }
             pedidoos.append(pedidoAñadido)
             GuardaditoPedidos(pedidoos)


    if queDesea=="3":
        print("")
        print("QUE VA A ORDENAR DE LA SECCION DE BEBIDAS")
        mostrarMenu=abrirMenu()
        contador=0
        for i in mostrarMenu:
            if i["categoria"]=="bebida":
                contador=contador+1
                print(contador)
                print("|",i["categoria"])
                print("|NOMBRE :",i["nombre"])
                print("|PRECIO :",i["precio"])
                print("-------------------")
        print("")
        entrada="entrada"
        pedidoGuardar=abrirPedidos()
        queVaApedir=input("QUE DESEA PEDIR?: ")
        print("-Juan Perez")
        print("-Maria Lopez")
        print("-Carlos Gomez")
        print("-Ana Martinez")
        print("-Andres Gomez")
        queCliente=input("QUE CLIENTE ERES: ")
        print("va a pagar ya? ")
        espera=input("si/no: ")
        if espera=="si":
            pagar="pagado"
        if espera=="no":
            pagar="sin pagar"
        
        if queVaApedir=="1":
            pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"bebida",
                        "nombre":"Coca-Cola",
                        "precio": 3000,
                        "estado":pagar
            }
            pedidoos.append(pedidoAñadido)
            GuardaditoPedidos(pedidoos)

        if queVaApedir=="2":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"bebida",
                        "nombre":"Jugo Natural",
                        "precio": 5000,
                        "estado":pagar
            }
             pedidoos.append(pedidoAñadido)
             GuardaditoPedidos(pedidoos)
        if queVaApedir=="3":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"bebida",
                        "nombre":"Vino",
                        "precio": 8000,
                        "estado":pagar
            }
             pedidoos.append(pedidoAñadido)
             GuardaditoPedidos(pedidoos)     
        if queVaApedir=="4":
             pedidoAñadido={
                "cliente":queCliente,
                "items:"
                        "categoria":"bebida",
                        "nombre":"Cerveza",
                        "precio": 3500,
                        "estado":pagar
            }
             pedidoos.append(pedidoAñadido)
             GuardaditoPedidos(pedidoos)
             