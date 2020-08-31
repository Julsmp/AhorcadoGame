"""
------
QUÉ ME FALTA POR HACER:
- Poner nivel de dificultad, para tener más o menos intentos
-  3 medio 5 facil 9"""


#Definimos las variables
Palabras=[] #Lista

#Módulos importados
import random
import sys #para finalizar
import re #importando el módulo "re"

#Definimos el funcionamiento de arranque
def arranque():
    print("")
    print("")
    print("¿Qué quieres hacer?")
    print("----------------------------")
    print("- Escribe 1 para cargar palabras")
    print("- Escribe 2 jugar")
    print("- Escribe 3 para eliminar palabras de la lista")
    print("- Escribe 4 para cerrar el programa")
    print("----------------------------")
    mensaje = input("¿Qué quieres hacer?: ")

    #Le decimos qué queremos que pase en el arranque
    if Palabras: #Si la lista de palabras no está vacia
        if mensaje == "1":
            añadir_palabras()
        elif mensaje == "2":
            progresoDelJuego()
        elif mensaje == "4":
            print("Programa finalizado")
            sys.exit(0)
        elif mensaje == "3":
            eliminar_palabras()
        else:
            print("Respuesta no válida. Por favor, selecciona una respuesta correcta.")
            arranque()
    else:
        if mensaje == "1":
            añadir_palabras()
        elif mensaje == "3":
            print("")
            print("No puedes eliminar palabras porque no hay ninguna palabra cargada en el juego.")
            print("")
            arranque()
        elif mensaje == "4":
            print("Programa finalizado")
            sys.exit(0)
        else: 
            print("")
            print("¡No corras tanto!")
            print("--> Antes de jugar, debes cargar las palabras <--")
            print("")
            arranque()

#Definimos la función 1 para cargar palabras
def añadir_palabras():
    print("")
    print()
    print("----")
    print("¡Vamos!")
    print("Añade las palabras para que juguemos.")
    print("Una vez hayas finalizado, escribe 'Fin' para dejar de añadir palabras")
    print("")
    palabra=""
    while palabra != "fin":
        palabra = input("- Añade una palabra: ")
        if len(palabra) <= 2: #si tiene menos de 3 carácteres
            print("")
            print("(⩾﹏⩽)")
            print("No es válido. La palabra debe contener al menos 3 letras")
            print("")
        elif re.search ("[!@#$%&/¡]", palabra): #caracteres alfanum.
            print("")
            print("◔_◔ ")
            print("Tienes que escribir una palabra....")
            print("Obviamente, no se pueden introducir caracteres no alfanuméricos.")
            print()
        elif re.search ("[0-9]", palabra): #si tiene numeros
            print("")
            print("ఠ_ఠ  ")
            print("¿Acaso me intentas poner a prueba?")
            print("Tienes que escribir una palabra....")
            print("¡LOS NUMEROS NO VALEN!")
            print()
        elif re.search (" ", palabra): #si tiene espacios
            print("")
            print("ಥ﹏ಥ")
            print("Tienes que escribir una palabra...")
            print("¿Porqué escribes espacios...? Por favor, juguemos bien... :(")
            print()
        elif "SOLUCION" == palabra.upper():
            print("")
            print("¡UPS! Lo siento, esta palabra está reservada para el avance del juego. Por favor, introduce otra palabra.")
            print()
        elif palabra.upper() != "FIN":
            palabra_upper = palabra.upper() #mayus
            Palabras.append(palabra_upper) #añadir la palabra mayus
        else:
            if Palabras:
                print("")
                print("¡Has añadido correctamente las siguientes palabras!") 
                print(Palabras)
                print("")            
                arranque() #volvemos a llamar al arranque
            else:
                print("")
                print("(҂◡_◡)")
                print("¡Ojo, que al final no has añadido ninguna palabra...")
                arranque()
            
#Funcion GameOVER
def GameOver():
    print("   ___                                  ___   __    __ .____  .___  ")
    print(" .'   \    ___  , _ , _     ___       .'   `. |     |  /      /   \ ")
    print(" |        /   ` |' `|' `. .'   `      |     |  \    /  |__.   |__-' ")
    print(" |    _  |    | |   |   | |----'      |     |   \  /   |      |  \  ")
    print("  `.___| `.__/| /   '   / `.___,       `.__.'    \/    /----/ /   \ ")
    print("")
    print("Vuelve a intentárlo")
    print("")

#Funcion Win
def ganar():
    print(" _______  _______  __       __    ______  __   _______       ___       _______   _______     _______. __ ")
    print("|   ____||   ____||  |     |  |  /      ||  | |       \     /   \     |       \ |   ____|   /       ||  |    ")
    print("|  |__   |  |__   |  |     |  | |  ,----'|  | |  .--.  |   /  ^  \    |  .--.  ||  |__     |   (----`|  |    ")
    print("|   __|  |   __|  |  |     |  | |  |     |  | |  |  |  |  /  /_\  \   |  |  |  ||   __|     \   \    |  |   ")
    print("|  |     |  |____ |  `----.|  | |  `----.|  | |  '--'  | /  _____  \  |  '--'  ||  |____.----)   |   |__|    ")
    print("|__|     |_______||_______||__|  \______||__| |_______/ /__/     \__\ |_______/ |_______|_______/    (__)  ")

#Def 3 eliminar palabras
def eliminar_palabras():
    if Palabras: #Si la lista de palabras no está vacia
        print(Palabras)
        palabraeliminada = input("¡Vale! ¿Qué palabra quieres eliminar? ")
        palabraeliminada = palabraeliminada.upper()
        if palabraeliminada in Palabras:
            Palabras.remove(palabraeliminada)
            print("---")
            print("La siguiente palabra se ha eliminado con éxito: " + palabraeliminada)
            print("La lista de palabras para jugar ha quedado así:")
            print(Palabras)
            print("")
            print("")
            eliminarmas = input("¿Quieres eliminar más palabras? Escribe 'si' o 'no': ")
            eliminarmas = eliminarmas.upper()
            if eliminarmas == "SI":
                eliminar_palabras()
            if eliminarmas == "NO":
                arranque()
            else:
                print("No te entiendo.. Vamos a volver a probar.")
        else:
            print("")
            print("La palabra que has escrito no se encuentra en la lista, por favor, revisa la lista y escribe la palabra correctamente:")
            print("")
            eliminar_palabras()
    else: 
        arranque()

#Definimos la función 2 para jugar
def progresoDelJuego():
    #Variables
    Win = False
    letrasadivinadas=[]
    letrasintroducidas=[]
    intentos = 6
    letrasrestantes= 10
    vidas=""
    listaespacios=[]
    listaletras=[]

    #Escogiendo una palabra aleatoria de la lista
    aleatorio = random.choice(Palabras)
    pista = ["_ "]*len(aleatorio)

    #Bienvenida al juego
    print("")
    print("")
    print("¡Juguemos!")
    print("A continuación, pensaré en una palabra y tu tendrás que adivinarla, poniendo las letras hasta sacar la palabra.")
    print("Por cada fallo, pierdes una vida. Tienes 6 ❤.")
    print("Si crees que ya sabes la palabra, escribe 'SOLUCION' para introducir la palabra. ¡OJO! Si fallas, pierdes todos los intentos.")
    print("")
    print("")

    #imprimiendo las letras de la palabra
    print("")
    print("La palabra escogida es:")
    impresion = ""
    for i in aleatorio:
        impresion += "_ "
    print(impresion)

    #contabilizar las letras quedan por adivinar    
    letrastotales = len(aleatorio)
    print("")
    print("Por tanto tienes " + str(letrastotales) + " letras que deberás adivinar.")
    print("")

    #bucle de juego
    letrasrestantes = letrastotales

    while Win == False:
        if letrasrestantes == 0:
            ganar()
            print("La palabra era: " + aleatorio)
            arranque()
            Win == True
        else:
            #Introducir letra
            print("")
            letra= input("- Introduce una letra: ")
            letra = letra.upper() #mayus

            tupalabra = ""
            tupalabra += letra

            #Palabra completa para resolver
            if letra.upper() == "SOLUCION":
                print("")
                palabra = input("- Escribe la palabra: ")
                palabra = palabra.upper() #mayus
                if palabra == aleatorio:
                    ganar()
                    print("La palabra era: " + aleatorio)
                    print("")
                    arranque()
                    Win == True
                else:
                    GameOver()
                    print("La palabra era: " + aleatorio)
                    print("")
                    print("")
                    arranque()

            else:
                #Revisar si anteriormente ya había introducido esta letra.
                if letra in letrasintroducidas:
                    print("")
                    print("¡CUIDADO!")
                    print("Ya has introducido esta letra anteriormente.")
                    print("Por favor, revisa la siguiente lista con las letras que ya has introducido y sigue probando con otras letras.")
                    print(letrasintroducidas)
                    print("-----------------")

                elif len(letra) >= 2:
                    print("No válido. Por favor, escribe una letra o 'solucion' si crees que ya sabes la palabra.")

                elif " " in letra:
                    print("No valen los espacios.")

                else:   
                    if aleatorio.find(letra) >= 0:
                        #Letra acertada
                        countAciertos = aleatorio.count(letra) #contamos las veces que aparece la letra en la palabra

                        if countAciertos == 1:
                            print("¡Guay! La '" + letra + "' se ha encontrado "  + str(countAciertos) + " vez.")
                        else: 
                            print("¡Guay! La '" + letra + "' se ha encontrado "  + str(countAciertos) + " veces.")

                        letrasadivinadas.append(letra) #añadimos la letra a una lista con las adivinadas
                        letrasintroducidas.append(letra) #añadimos la letra a una lista con las introducidas


                        for c in re.finditer(letra, aleatorio, re.IGNORECASE):
                            pista[c.start():c.end()] = list(c.group())

                        for c in re.finditer(letra, aleatorio, re.IGNORECASE):
                            pista[c.start()] = c.group()

                        print("".join(pista))

                        letrasrestantes = int(letrasrestantes) - int(countAciertos)

                        print("")
                        print("Te quedan " + str(letrasrestantes) + " por adivinar" )

                    elif intentos == 1:
                        GameOver()
                        arranque()
                    else:
                        print("")
                        print("(҂⌣̀_⌣́)")
                        print("¡Vaya! No se ha encontrado la letra '" + letra + "' en la palabra")
                        print("Acabas de perder un ❤ ")
                        letrasintroducidas.append(letra) #añadimos la letra a una lista con las introducidas
                        intentos = int(intentos) - 1
                        vidas = "❤ " * (intentos)
                        print("Te quedan " + vidas)

#Intro del juego
print("")
print("----------------------")
print("Made by Julia Martínez")
print("----------------------")
print("----------------------")
print("")
print("----AHORCADO-----")
print("")
print("|----------------|--")
print("|                O  ")
print("|               -|- ")
print("|                /\ ")
print("|                   ")
print("--------------------")
print("")
print("¡Hola!")


#Ejecutamos la función de arranque
arranque()
