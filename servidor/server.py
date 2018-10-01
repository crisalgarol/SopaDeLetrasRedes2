#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
import datetime
import Resultado
import socket
import random

#Diccionario que almacena el concepto y sus palabras asociadas
conceptos = {}
conceptos['educacion'] = {"escuela","salon","horarios","algebra","alumno","aprender","arte","biblios","libreta","biologia","calculo","examen","ciencia","colegio"}
conceptos['fiesta'] = {"globos", "dulces", "pinata", "pastel", "velas", "refresco", "musica", "baile", "postre", "comida", "gorros", "luces", "alcohol", "botana"}
conceptos['parque'] = {"arboles", "niños", "juegos", "columpios", "payasos", "vendedores", "perros", "comida", "ardillas", "palomas", "baile", "musica", "bicicleta", "personas"}
conceptos['matematicas'] = {"suma", "resta", "logico", "division", "integral", "derivada", "ecuacion", "conjunto", "espacios", "graficas", "funciones", "teoremas", "logica", "infinito"}
conceptos['jorge'] = {"hola", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo","uno", "dos", "tres", "cuatro", "cinco", "mundo"}

palabrasAnagrama = {}
palabrasAnagrama['cincoLetras'] = {"ebano", "abeja","oveja","ebria","ebrio","echad", "echan", "echar", "echas", "echen", "edita", "edito", "educa", "educo", "habas", "haber", "habia", "habil", "macho", "manco", "obvio", "pahua", "vacas", "queja", "quedo", "quepo", "caber", "rosas"}
palabrasAnagrama['seisLetras'] = {"baboso","fachas","gaceta", "habito","ibamos", "labios", "labora", "nachas", "nachos", "obesos", "quemar", "rabano", "sabado", "sabila", "tabaco","tabano", "ulcera", "escoba", "anillo", "asalto", "arruga", "azteca", "chisme", "asesor", "ingles", "juzgar"}
palabrasAnagrama['sieteLetras'] = {"cuchara", "ventana", "tabique", "damasco", "habitat", "habitar", "laboral", "macabeo","macario", "obispos","pachuca", "quebrar", "tabasco","tampico", "tempura", "estorba", "cintura", "acetato", "acomodo", "acolito", "adornar", "aerosol", "ahijado"}
#Modalidad del juego Concepto o Anagrama"
modalidad = ""
#Dificultad del juego, facil intermedio o dificil. Concepto tiene ""
dificultad = ""
#Almacena el nombre del usuario para el ranking
usuario = ""
#Fechas de control del tiempo de usuario
tiempoInicio = datetime.datetime.now()
tiempoFin = datetime.datetime.now()
#Almaceno en una lista el ranking
ranking = []
tiempo = 0

def devolverListaAnagrama():
    listaPalabras = []
    palabrasObtenidas = []
    stringPalabras = ""

    opcion = random.randrange( 5 + random.randrange(3))

    if opcion == 5:
        palabrasObtenidas = list(palabrasAnagrama['cincoLetras'])
    elif opcion == 6 :
        palabrasObtenidas = list(palabrasAnagrama['seisLetras'])
    else:
        palabrasObtenidas = list(palabrasAnagrama['sieteLetras'])
        

    while len(listaPalabras) < 15 :
        numR = random.randrange(len(palabrasObtenidas))
        if palabrasObtenidas[numR] not in listaPalabras :
            listaPalabras.append(palabrasObtenidas[numR])

    counter = 0
    for i in listaPalabras:
        stringPalabras += i 

        if (counter+1) != len(listaPalabras):
            stringPalabras += ","
        
        counter += 1
    
    return stringPalabras

def obtenerConceptoRandom():
    palabrasObtenidas = []    
    opcion = random.randrange(random.randrange(4) + 1)
    stringPalabras = ""

    if opcion == 1:
        palabrasObtenidas = conceptos['educacion']
        stringPalabras = "educacion:"
    elif opcion == 2:
        palabrasObtenidas = conceptos['fiesta']
        stringPalabras = "fiesta:"
    elif opcion == 3:
        palabrasObtenidas = conceptos['parque']
        stringPalabras = "parque:"
    else:
        palabrasObtenidas = conceptos['matematicas']
        stringPalabras = "matematicas:"

    counter = 0
    palabrasObtenidas = conceptos['jorge']

    for i in palabrasObtenidas:
        stringPalabras += i 

        if (counter+1) != len(palabrasObtenidas):
            stringPalabras += ","
        
        counter += 1


    return stringPalabras
    
def devolverRanking():
    cadenaRanking = ""
    counter = 0

    for i in ranking:
        cadenaRanking += "Usuarioo:" + str(i.usuario.split("\n")) + ","
        cadenaRanking += "Modalidad:" + str(i.modalidad) + ","
        cadenaRanking += "Dificultad:" + str(i.dificultad) + ","
        cadenaRanking += "Tiempo:" + str(i.tiempo)
        cadenaRanking += "_"
        print(cadenaRanking)

        counter += 1

    return cadenaRanking


def main():
    os.system("clear")
    #Crear el socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind( ('10.100.66.219',7881) )
    #s.bind( ('127.0.0.1',7881) )

    s.listen(1)

    print("Se ha iniciado el servidor esperando conexiones entrantes")
    
    #Esperar las multiples conexiones

    while True:

        conexion, direccion  = s.accept()
        print('Nueva conexion establecida con: ' + str((direccion)))
        
        #Recibir los datos enviados por el cliente
        mensajeRecibido = conexion.recv(1024)
        print("Se recibio: " + mensajeRecibido )

        #Realizar las comparaciones
        #Primero se necesita pedir un nuevo juego
        if("nuevo" in mensajeRecibido):
            modalidad = ""
            dificultad = ""
            usuario = ""
            conexion.sendall("ok")
            os.system('clear')

        elif("usuario" in mensajeRecibido):
            usuario = mensajeRecibido.split(":")[1] #Envias usuario:nombreusuario
            print("usuario rcibidooo: " + usuario)
            usuario = usuario.split("\n")[0]
            print("usuario compuesto: " + usuario)
            conexion.sendall("ok")

        elif("concepto" in mensajeRecibido):
            modalidad = "concepto"
            dificultad = "ninguna"
            conexion.sendall("ok")

        #Parte de la conexion con el anagrama 
        elif("anagrama" in mensajeRecibido):
            modalidad = "anagrama"
            conexion.sendall("ok")
        
        elif "palabras" in mensajeRecibido:
            if "anagrama" in modalidad:
                conexion.sendall(devolverListaAnagrama())
            else:
                conexion.sendall(obtenerConceptoRandom())


        elif("facil" in mensajeRecibido or "intermedio" in mensajeRecibido or "dificil" in mensajeRecibido):
            dificultad = mensajeRecibido
            conexion.sendall("ok")

        #Parte general
        elif( "iniciar" in mensajeRecibido ):
            tiempoInicio = datetime.datetime.now()
            print("Tiempo Inicio: ")
            print(tiempoInicio)
            conexion.sendall("ok")

        elif "tiempoFinal" in mensajeRecibido:
            tiempoFin = datetime.datetime.now()
            tiempo = 0

            if (tiempoFin.hour - tiempoInicio.hour) == 0:
                tiempo = tiempoFin.minute - tiempoInicio.minute
            else:
                tiempo = (tiempoFin.hour-tiempoInicio.hour)*60 
                if tiempoFin.minute-tiempoInicio.minute < 0:
                    tiempo += (tiempoFin.minute-tiempoInicio.minute)*-1
            
            conexion.sendall(str(tiempo))

        elif("puntuaciones" in mensajeRecibido):
            tiempoFin = datetime.datetime.now()
            tiempo = 0

            if (tiempoFin.hour - tiempoInicio.hour) == 0:
                tiempo = tiempoFin.minute - tiempoInicio.minute
            else:
                tiempo = (tiempoFin.hour-tiempoInicio.hour)*60 
                if tiempoFin.minute-tiempoInicio.minute < 0:
                    tiempo += (tiempoFin.minute-tiempoInicio.minute)*-1
            
            nuevoJugador = Resultado.Resultado(modalidad, dificultad, usuario, tiempo)
            ranking.append(nuevoJugador)

            conexion.sendall(devolverRanking())

        else:
            conexion.sendall("Error")
            continue
            
            
            
        conexion.close()
    
    

main()