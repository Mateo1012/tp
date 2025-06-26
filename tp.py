import random
import threading
import json
import os
import time

# -----------------------------
# Excepción personalizada para el tiempo límite
class TiempoAgotado(Exception):
    pass

# -----------------------------
# Clase Pregunta
class Pregunta:
    def __init__(self, texto, opciones, respuesta_correcta, categoria, dificultad):
        self.texto = texto
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        self.categoria = categoria
        self.dificultad = dificultad

# -----------------------------
# Clase Jugador
# Clase base
class JugadorBase:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vidas = 3
        self.progreso = {
            cat: 0 for cat in ["Deportes", "Geografía", "Historia", "videojuegos", "Ciencia", "Entretenimiento"]
        }

    def ha_ganado(self):
        return all(nivel == 3 for nivel in self.progreso.values())

# Subclase para jugador individual
class JugadorIndividual(JugadorBase):
    def __init__(self, nombre):
        super().__init__(nombre)

# Subclase para jugador multijugador
class JugadorMultijugador(JugadorBase):
    def __init__(self, nombre):
        super().__init__(nombre)


# -----------------------------
# Decorador para registrar el turno
def log_turno(func):
    def wrapper(*args, **kwargs):
        print("\n🎲 Nuevo turno")
        resultado = func(*args, **kwargs)
        print("🔚 Fin del turno\n" + "-"*40)
        return resultado
    return wrapper

# -----------------------------
# Función para input con límite de tiempo
def input_con_tiempo(prompt, timeout=30):
    respuesta = [None]

    def obtener_input():
        respuesta[0] = input(prompt)

    hilo = threading.Thread(target=obtener_input)
    hilo.daemon = True
    hilo.start()
    hilo.join(timeout)
    if hilo.is_alive():
        raise TiempoAgotado()
    return respuesta[0]

# -----------------------------
# Base de datos de preguntas
preguntas = {
    "Deportes": {
        "facil": [],
        "intermedio": [],
        "dificil": []
    },
    "Geografía": {
        "facil": [],
        "intermedio": [],
        "dificil": []
    },
    "Historia": {
        "facil": [],
        "intermedio": [],
        "dificil": []
    },
    "Videojuegos": {
        "facil": [],
        "intermedio": [],
        "dificil": []
    },
    "Ciencia": {
        "facil": [],
        "intermedio": [],
        "dificil": []
    },
    "Entretenimiento": {
        "facil": [],
        "intermedio": [],
        "dificil": []
    }
}

# las preguntas 
for i in range(10):
  #Deportes:

  #Facil:
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿Quien ganó el mundial de fútbol 2022? (#{i+1})",
        opciones=["Argentina", "Francia", "Alemania", "Chile"],
        respuesta_correcta=0,
        categoria="Deportes",
        dificultad="facil"
    ))
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿Cuántos jugadores tiene un equipo de fútbol? (#{i+1})",
        opciones=["10", "11", "20", "22"],
        respuesta_correcta=1,
        categoria="Deportes",
        dificultad="facil"
    ))
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿En qué deporte se utiliza una raqueta y una pelota? (#{i+1})",
        opciones=["Golf", "Béisbol", "Tenis", "Boxeo"],
        respuesta_correcta=2,
        categoria="Deportes",
        dificultad="facil"
    ))
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿Qué deporte practica LeBron James? (#{i+1})",
        opciones=["Béisbol", "Tenis", "Atletismo", "Baloncesto"],
        respuesta_correcta=3,
        categoria="Deportes",
        dificultad="facil"
    ))
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿Qué país es famoso por ganar muchos torneos de fútbol? (#{i+1})",
        opciones=["Alemania", "Brasil", "España", "Argentina"],
        respuesta_correcta=1,
        categoria="Deportes",
        dificultad="facil"
    ))
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿En qué deporte se corre el Tour de Francia? (#{i+1})",
        opciones=["Automovilismo", "Atletismo", "Ciclismo", "Motociclismo"],
        respuesta_correcta=2,
        categoria="Deportes",
        dificultad="facil"
    ))
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿Qué parte del cuerpo no se puede usar en fútbol (excepto el portero)? (#{i+1})",
        opciones=["Cabeza", "Pierna", "Pecho", "Brazos"],
        respuesta_correcta=3,
        categoria="Deportes",
        dificultad="facil"
    ))
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el deporte que se practica en una piscina y con una pelota? (#{i+1})",
        opciones=["Waterpolo", "Natación", "Surf", "Ski acuático"],
        respuesta_correcta=0,
        categoria="Deportes",
        dificultad="facil"
    ))
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿En qué deporte se utilizan guantes y se golpea con los puños? (#{i+1})",
        opciones=["Karate", "Boxeo", "Rugby", "Hockey"],
        respuesta_correcta=1,
        categoria="Deportes",
        dificultad="facil"
    ))
    preguntas["Deportes"]["facil"].append(Pregunta(
        texto=f"¿Qué país organiza el Super Bowl? (#{i+1})",
        opciones=["Inglaterra", "México", "Estados Unidos", "Canadá"],
        respuesta_correcta=2,
        categoria="Deportes",
        dificultad="facil"
    ))

  #Intermedio:

    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿Cuántos sets necesita ganar un jugador para llevarse un partido en Wimbledon (hombres)? (#{i+1})",
        opciones=["2", "3", "4", "5"],
        respuesta_correcta=1,
        categoria="Deportes",
        dificultad="intermedio"
    ))
    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿En qué año se celebraron los primeros Juegos Olímpicos modernos? (#{i+1})",
        opciones=["1896", "1900", "1880", "1912"],
        respuesta_correcta=0,
        categoria="Deportes",
        dificultad="intermedio"
    ))
    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál es la duración oficial de un partido de baloncesto profesional (NBA)? (#{i+1})",
        opciones=["40 minutos", "48 minutos", "60 minutos", "90 minutos"],
        respuesta_correcta=1,
        categoria="Deportes",
        dificultad="intermedio"
    ))
    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿Qué piloto ha ganado más campeonatos de Fórmula 1 (hasta 2023)? (#{i+1})",
        opciones=["Ayrton Senna", "Sebastian Vettel", "Lewis Hamilton", "Michael Schumacher"],
        respuesta_correcta=2,
        categoria="Deportes",
        dificultad="intermedio"
    ))
    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿Qué país fue sede de los Juegos Olímpicos de 2016? (#{i+1})",
        opciones=["China", "Grecia", "Japón", "Brasil"],
        respuesta_correcta=3,
        categoria="Deportes",
        dificultad="intermedio"
    ))
    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿Qué selección ganó la Copa Mundial de la FIFA en 2010? (#{i+1})",
        opciones=["Alemania", "España", "Brasil", "Italia"],
        respuesta_correcta=1,
        categoria="Deportes",
        dificultad="intermedio"
    ))
    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿Qué deporte incluye movimientos como el ollie y el kickflip? (#{i+1})",
        opciones=["Snowboard", "Surf", "BMX", "Skateboarding"],
        respuesta_correcta=3,
        categoria="Deportes",
        dificultad="intermedio"
    ))
    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿Cuántos puntos vale un try en rugby? (#{i+1})",
        opciones=["5", "3", "6", "7"],
        respuesta_correcta=0,
        categoria="Deportes",
        dificultad="intermedio"
    ))
    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿Qué tenista femenino ganó más títulos de Grand Slam? (#{i+1})",
        opciones=["Steffi Graf", "Martina Navratilova", "Serena Williams", "Billie Jean King"],
        respuesta_correcta=2,
        categoria="Deportes",
        dificultad="intermedio"
    ))
    preguntas["Deportes"]["intermedio"].append(Pregunta(
        texto=f"¿Qué país ha ganado más medallas olímpicas en total? (#{i+1})",
        opciones=["Rusia", "Alemania", "China", "Estados Unidos"],
        respuesta_correcta=3,
        categoria="Deportes",
        dificultad="intermedio"
    ))

  #Dificil:

    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿En qué deporte se utiliza el término “albatros”? (#{i+1})",
        opciones=["Cricket", "Golf", "Rugby", "Hockey"],
        respuesta_correcta=1,
        categoria="Deportes",
        dificultad="dificil"
    ))
    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿Cuántos minutos dura un combate de boxeo profesional (título mundial, 12 asaltos)? (#{i+1})",
        opciones=["36", "30", "40", "45"],
        respuesta_correcta=0,
        categoria="Deportes",
        dificultad="dificil"
    ))
    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿Quién fue el primer campeón mundial de Fórmula 1 en 1950? (#{i+1})",
        opciones=["Juan Manuel Fangio", "Alberto Ascari", "Giuseppe Farina", "Stirling Moss"],
        respuesta_correcta=2,
        categoria="Deportes",
        dificultad="dificil"
    ))
    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿Qué selección ganó la primera Copa Mundial de la FIFA en 1930? (#{i+1})",
        opciones=["Argentina", "Brasil", "Uruguay", "Italia"],
        respuesta_correcta=2,
        categoria="Deportes",
        dificultad="dificil"
    ))
    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es el nombre del trofeo que se entrega al campeón de la NHL (hockey sobre hielo)? (#{i+1})",
        opciones=["Copa Stanley", "Copa Davis", "Trofeo Grey", "Copa Mundial"],
        respuesta_correcta=0,
        categoria="Deportes",
        dificultad="dificil"
    ))
    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿Qué boxeador terminó invicto con un récord de 50-0? (#{i+1})",
        opciones=["Myke Tyson", "Manny Pacquiao", "Muhammad Ali", "Floyd Mayweather Jr."],
        respuesta_correcta=3,
        categoria="Deportes",
        dificultad="dificil"
    ))
    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿Cuántos jugadores tiene un equipo de béisbol en el campo? (#{i+1})",
        opciones=["7", "9", "11", "10"],
        respuesta_correcta=1,
        categoria="Deportes",
        dificultad="dificil"
    ))
    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿Qué ciudad ha sido sede olímpica 3 veces? (#{i+1})",
        opciones=["Londres", "París", "Tokio", "Atenas"],
        respuesta_correcta=0,
        categoria="Deportes",
        dificultad="dificil"
    ))
    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿Qué jugadora de fútbol ganó 6 Balones de Oro (hasta 2023)? (#{i+1})",
        opciones=["Alex Morgan", "Megan Rapinoe", "Ada Hegerberg", "Alexia Putellas"],
        respuesta_correcta=3,
        categoria="Deportes",
        dificultad="dificil"
    ))
    preguntas["Deportes"]["dificil"].append(Pregunta(
        texto=f"¿Qué país fue el campeón de la Copa Mundial de Rugby 2023? (#{i+1})",
        opciones=["Inglaterra", "Nueva Zelanda", "Francia", "Sudáfrica"],
        respuesta_correcta=3,
        categoria="Deportes",
        dificultad="dificil"
    ))

#Geografía:

  #Facil:

    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el río más largo del mundo? (#{i+1})",
        opciones=["Amazonas", "Nilo", "Misisipi", "Yangtsé"],
        respuesta_correcta=0,
        categoria="Geografía",
        dificultad="facil"
    ))
    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿En qué continente está ubicado Egipto? (#{i+1})",
        opciones=["Asia", "Europa", "África", "Oceanía"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="facil"
    ))
    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿Qué país tiene la Torre Eiffel? (#{i+1})",
        opciones=["Inglaterra", "Italia", "Suiza", "Francia"],
        respuesta_correcta=3,
        categoria="Geografía",
        dificultad="facil"
    ))
    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿Cuál es la capital de España? (#{i+1})",
        opciones=["Sevilla", "Madrid", "Barcelona", "Valencia"],
        respuesta_correcta=1,
        categoria="Geografía",
        dificultad="facil"
    ))
    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿Qué océano baña las costas del este de Estados Unidos? (#{i+1})",
        opciones=["Atlántico", "Pacífico", "Índico", "Ártico"],
        respuesta_correcta=0,
        categoria="Geografía",
        dificultad="facil"
    ))
    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿Qué país tiene forma de bota? (#{i+1})",
        opciones=["Francia", "Portugal", "Italia", "Grecia"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="facil"
    ))
    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿En qué continente se encuentra Brasil? (#{i+1})",
        opciones=["América", "Asia", "África", "Europa"],
        respuesta_correcta=0,
        categoria="Geografía",
        dificultad="facil"
    ))
    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿Cuál de estos países es una isla? (#{i+1})",
        opciones=["Alemania", "Canadá", "Australia", "México"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="facil"
    ))
    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el desierto más grande del mundo? (#{i+1})",
        opciones=["Kalahari", "Gobi", "Atacama", "Sahara"],
        respuesta_correcta=3,
        categoria="Geografía",
        dificultad="facil"
    ))
    preguntas["Geografía"]["facil"].append(Pregunta(
        texto=f"¿Qué país tiene forma alargada y se extiende por el borde occidental de Sudamérica? (#{i+1})",
        opciones=["Argentina", "Colombia", "Perú", "Chile"],
        respuesta_correcta=3,
        categoria="Geografía",
        dificultad="facil"
    ))

  #Intermedio:

    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál es la capital de Canadá? (#{i+1})",
        opciones=["Toronto", "Vancouver", "Montreal", "Ottawa"],
        respuesta_correcta=3,
        categoria="Geografía",
        dificultad="intermedio"
    ))
    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿Qué cordillera atraviesa Sudamérica de norte a sur? (#{i+1})",
        opciones=["Alpes", "Andes", "Himalaya", "Apeninos"],
        respuesta_correcta=1,
        categoria="Geografía",
        dificultad="intermedio"
    ))
    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿Qué país africano tiene más población? (#{i+1})",
        opciones=["Sudáfrica", "Nigeria", "Egipto", "Etiopía"],
        respuesta_correcta=1,
        categoria="Geografía",
        dificultad="intermedio"
    ))
    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿Qué país tiene más fronteras terrestres con otros países? (#{i+1})",
        opciones=["Rusia", "Alemania", "China", "Brasil"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="intermedio"
    ))
    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál es el lago más grande de América del Sur? (#{i+1})",
        opciones=["Titicaca", "Poopó", "Argentino", "Maracaibo"],
        respuesta_correcta=3,
        categoria="Geografía",
        dificultad="intermedio"
    ))
    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿Qué país tiene el mayor número de islas en su territorio? (#{i+1})",
        opciones=["Noruega", "Filipinas", "Canadá", "Suecia"],
        respuesta_correcta=3,
        categoria="Geografía",
        dificultad="intermedio"
    ))
    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿En qué país se encuentra el monte Kilimanjaro? (#{i+1})",
        opciones=["Kenia", "Tanzania", "Sudán", "Uganda"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="intermedio"
    ))
    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál es la capital de Nueva Zelanda? (#{i+1})",
        opciones=["Wellington", "Hamilton", "Auckland", "Christchurch"],
        respuesta_correcta=0,
        categoria="Geografía",
        dificultad="intermedio"
    ))
    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿Qué océano está entre África y Australia? (#{i+1})",
        opciones=["Índico", "Atlántico", "Pacífico", "Ártico"],
        respuesta_correcta=0,
        categoria="Geografía",
        dificultad="intermedio"
    ))
    preguntas["Geografía"]["intermedio"].append(Pregunta(
        texto=f"¿Qué país limita con más países europeos? (#{i+1})",
        opciones=["Alemania", "Polonia", "Suiza", "Francia"],
        respuesta_correcta=0,
        categoria="Geografía",
        dificultad="intermedio"
    ))

  #Dificil:

    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es la capital de Kazajistán? (#{i+1})",
        opciones=["Almaty", "Taskent", "Astaná/Nursultán", "Bakú"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="dificil"
    ))
    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿Qué país tiene la mayor altitud media del mundo? (#{i+1})",
        opciones=["Suiza", "Bután", "Nepal", "Lesoto"],
        respuesta_correcta=3,
        categoria="Geografía",
        dificultad="dificil"
    ))
    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es el punto más bajo de América del Sur? (#{i+1})",
        opciones=["Salar de Uyuni (Bolivia)", "Laguna del Carbón (Argentina)", "Valle de la Luna (Chile)", "Lago Titicaca (Bolivia-Perú)"],
        respuesta_correcta=1,
        categoria="Geografía",
        dificultad="dificil"
    ))
    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es el país más joven del mundo? (#{i+1})",
        opciones=["Montenegro", "Kosovo", "Sudán del Sur", "Timor Oriental"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="dificil"
    ))
    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿Qué país tiene la mayor cantidad de volcanes activos? (#{i+1})",
        opciones=["Islandia", "Japón", "Indonesia", "México"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="dificil"
    ))
    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es el mar interior más grande del mundo? (#{i+1})",
        opciones=["Rojo", "De Aral", "Caspio", "De China Meridional"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="dificil"
    ))
    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿En qué país se encuentra el desierto de Dasht-e Kavir? (#{i+1})",
        opciones=["Arabia Saudita", "Irán", "India", "Afganistán"],
        respuesta_correcta=1,
        categoria="Geografía",
        dificultad="dificil"
    ))
    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es el país sin litoral más poblado del mundo? (#{i+1})",
        opciones=["Etiopía", "Uzbekistán", "Afganistán", "Azerbaiyán"],
        respuesta_correcta=0,
        categoria="Geografía",
        dificultad="dificil"
    ))
    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿Qué país tiene la ciudad capital situada a mayor altitud? (#{i+1})",
        opciones=["Bolivia", "Perú", "Ecuador", "Nepal"],
        respuesta_correcta=0,
        categoria="Geografía",
        dificultad="dificil"
    ))
    preguntas["Geografía"]["dificil"].append(Pregunta(
        texto=f"¿Cuál de estos países no tiene frontera con Brasil? (#{i+1})",
        opciones=["Colombia", "Venezuela", "Chile", "Perú"],
        respuesta_correcta=2,
        categoria="Geografía",
        dificultad="dificil"
    ))

#Historia:

  #Facil:

    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿Quién fue el primer presidente de Estados Unidos? (#{i+1})",
        opciones=["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
        respuesta_correcta=2,
        categoria="Historia",
        dificultad="facil"
    ))
    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿En qué país comenzó la Revolución Francesa? (#{i+1})",
        opciones=["Alemania", "Italia", "Francia", "Inglaterra"],
        respuesta_correcta=2,
        categoria="Historia",
        dificultad="facil"
    ))
    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿Qué gran imperio construyó las pirámides de Egipto? (#{i+1})",
        opciones=["Romano", "Persa", "Egipcio", "Babilónico"],
        respuesta_correcta=2,
        categoria="Historia",
        dificultad="facil"
    ))
    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿Quién lideró la resistencia india contra el dominio británico con métodos de no violencia? (#{i+1})",
        opciones=["Jawaharlal Nehru", "Subhas Chandra Bose", "Indira Gandhi", "Mahatma Gandhi"],
        respuesta_correcta=3,
        categoria="Historia",
        dificultad="facil"
    ))
    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿Qué acontecimiento histórico ocurrió el 12 de octubre de 1492? (#{i+1})",
        opciones=["Primera Guerra Mundial", "Descubrimiento de América", "Revolución Industrial", "Independencia de EE UU"],
        respuesta_correcta=1,
        categoria="Historia",
        dificultad="facil"
    ))
    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿Cuál fue el conflicto armado global entre 1939 y 1945? (#{i+1})",
        opciones=["Guerra de Vietnam", "Primera Guerra Mundial", "Guerra Fría", "Segunda Guerra Mundial"],
        respuesta_correcta=3,
        categoria="Historia",
        dificultad="facil"
    ))
    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿Qué civilización construyó Machu Picchu? (#{i+1})",
        opciones=["Inca", "Maya", "Azteca", "Tolteca"],
        respuesta_correcta=0,
        categoria="Historia",
        dificultad="facil"
    ))
    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿Quién fue el dictador de Alemania durante la Segunda Guerra Mundial? (#{i+1})",
        opciones=["Adolf Hitler", "Joseph Stalin", "Benito Mussolini", "Winston Churchill"],
        respuesta_correcta=0,
        categoria="Historia",
        dificultad="facil"
    ))
    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿Qué país lanzó las bombas atómicas sobre Hiroshima y Nagasaki? (#{i+1})",
        opciones=["Alemania", "Estados Unidos", "Japón", "Unión Soviética"],
        respuesta_correcta=1,
        categoria="Historia",
        dificultad="facil"
    ))
    preguntas["Historia"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el muro más famoso que separó una ciudad durante la Guerra Fría? (#{i+1})",
        opciones=["Londres", "Berlín", "Varsovia", "Moscú"],
        respuesta_correcta=1,
        categoria="Historia",
        dificultad="facil"
    ))

  #Intermedio:

    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿Qué imperio fue derrotado en la batalla de Waterloo? (#{i+1})",
        opciones=["Austrohúngaro", "Otomano", "Napoleónico", "Bizantino"],
        respuesta_correcta=2,
        categoria="Historia",
        dificultad="intermedio"
    ))
    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿En qué año cayó el Muro de Berlín? (#{i+1})",
        opciones=["1989", "1979", "1991", "1993"],
        respuesta_correcta=0,
        categoria="Historia",
        dificultad="intermedio"
    ))
    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿Quién fue el emperador romano durante la erupción del Vesubio en el año 79 d.C.? (#{i+1})",
        opciones=["Nerón", "Tito", "Calígula", "Claudio"],
        respuesta_correcta=1,
        categoria="Historia",
        dificultad="intermedio"
    ))
    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿En qué país comenzó la Revolución Industrial? (#{i+1})",
        opciones=["Francia", "Alemania", "Inglaterra", "Estados Unidos"],
        respuesta_correcta=2,
        categoria="Historia",
        dificultad="intermedio"
    ))
    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿Qué reina inglesa es conocida por su largo reinado en el siglo XIX? (#{i+1})",
        opciones=["Victoria", "Isabel 1", "María Estuardo", "Ana Bolena"],
        respuesta_correcta=0,
        categoria="Historia",
        dificultad="intermedio"
    ))
    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿Quién fue Simón Bolívar? (#{i+1})",
        opciones=["Rey de España", "Militar Español", "Dictador Chileno", "Libertador de América"],
        respuesta_correcta=3,
        categoria="Historia",
        dificultad="intermedio"
    ))
    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál fue la principal causa de la Primera Guerra Mundial? (#{i+1})",
        opciones=["La Invasión de Polonia", "El asesinato del archiduque Francisco Fernando", "La Revolución Rusa", "La caída del Imperio Otomano"],
        respuesta_correcta=1,
        categoria="Historia",
        dificultad="intermedio"
    ))
    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿En qué año se firmó la Declaración de Independencia de los Estados Unidos? (#{i+1})",
        opciones=["1776", "1789", "1812", "1791"],
        respuesta_correcta=0,
        categoria="Historia",
        dificultad="intermedio"
    ))
    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál fue el nombre del plan económico de ayuda a Europa tras la Segunda Guerra Mundial? (#{i+1})",
        opciones=["Truman", "Monroe", "Roosevelt", "Marshall"],
        respuesta_correcta=3,
        categoria="Historia",
        dificultad="intermedio"
    ))
    preguntas["Historia"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál fue el primer país en abolir la esclavitud? (#{i+1})",
        opciones=["Francia", "Haití", "Inglaterra", "Estados Unidos"],
        respuesta_correcta=1,
        categoria="Historia",
        dificultad="intermedio"
    ))

  #Dificil:

    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿Qué tratado puso fin a la Primera Guerra Mundial? (#{i+1})",
        opciones=["Yalta", "París", "Versalles", "Ginebra"],
        respuesta_correcta=2,
        categoria="Historia",
        dificultad="dificil"
    ))
    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿Quién fue el primer emperador del Sacro Imperio Romano Germánico? (#{i+1})",
        opciones=["Carlomagno", "Federico Barbarroja", "Otto 1", "Carlos 5"],
        respuesta_correcta=0,
        categoria="Historia",
        dificultad="dificil"
    ))
    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿En qué año fue ejecutado Luis XVI durante la Revolución Francesa? (#{i+1})",
        opciones=["1793", "1791", "1789", "1795"],
        respuesta_correcta=0,
        categoria="Historia",
        dificultad="dificil"
    ))
    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿Cuál fue la capital del Imperio Bizantino? (#{i+1})",
        opciones=["Roma", "Estambul", "Constantinopla", "Atenas"],
        respuesta_correcta=2,
        categoria="Historia",
        dificultad="dificil"
    ))
    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿Qué batalla marcó el fin del dominio musulmán en la península ibérica? (#{i+1})",
        opciones=["De las Navas de Tolosa", "De Lepanto", "De Covadonga", "Toma de Granada"],
        respuesta_correcta=3,
        categoria="Historia",
        dificultad="dificil"
    ))
    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿Qué dinastía gobernó China durante la construcción de la Gran Muralla en su forma inicial? (#{i+1})",
        opciones=["Tang", "Han", "Qin", "Song"],
        respuesta_correcta=2,
        categoria="Historia",
        dificultad="dificil"
    ))
    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿Qué imperio tenía como capital a Cuzco? (#{i+1})",
        opciones=["Azteca", "Inca", "Maya", "Tolteca"],
        respuesta_correcta=1,
        categoria="Historia",
        dificultad="dificil"
    ))
    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿Qué rey británico tuvo seis esposas? (#{i+1})",
        opciones=["Enrique 8", "Ricardo 3", "Eduardo 6", "Jorge 3"],
        respuesta_correcta=0,
        categoria="Historia",
        dificultad="dificil"
    ))
    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿En qué ciudad fue asesinada la archiduquesa Isabel de Austria, evento que inició la Primera Guerra Mundial? (#{i+1})",
        opciones=["Praga", "Sarajevo", "Viena", "Berlín"],
        respuesta_correcta=1,
        categoria="Historia",
        dificultad="dificil"
    ))
    preguntas["Historia"]["dificil"].append(Pregunta(
        texto=f"¿Qué país fue el primero en darle el voto a las mujeres? (#{i+1})",
        opciones=["Reino Unido", "Estados Unidos", "Nueva Zelanda", "Canadá"],
        respuesta_correcta=2,
        categoria="Historia",
        dificultad="dificil"
    ))

#Videojuegos:

  #Facil:

    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el fontanero más famoso de los Videojuegos? (#{i+1})",
        opciones=["Luigi", "Wario", "Mario", "Toad"],
        respuesta_correcta=2,
        categoria="Videojuegos",
        dificultad="facil"
    ))
    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿A que franquicia pertenece Charizard? (#{i+1})",
        opciones=["Digimon", "Pokémon", "Yu-Gi-Oh", "Monster Rancher"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="facil"
    ))
    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿Qué consola lanzó Nintendo antes de la Switch? (#{i+1})",
        opciones=["Wii", "Wii U", "GameCube", "DS"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="facil"
    ))
    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿¿Qué personaje de Videojuegos es conocido por recolectar anillos dorados? (#{i+1})",
        opciones=["Knuckles", "Crash", "Rayman", "Sonic"],
        respuesta_correcta=3,
        categoria="Videojuegos",
        dificultad="facil"
    ))
    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿Cuál de estos juegos es un shooter en primera persona? (#{i+1})",
        opciones=["Call of Duty", "FIFA", "The Sims", "Tetris"],
        respuesta_correcta=0,
        categoria="Videojuegos",
        dificultad="facil"
    ))
    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el objetivo principal en Minecraft? (#{i+1})",
        opciones=["Cocinar", "Conducir", "Construír y sobrevivir", "Cazar animales"],
        respuesta_correcta=2,
        categoria="Videojuegos",
        dificultad="facil"
    ))
    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿Qué princesa es frecuentemente rescatada por Mario? (#{i+1})",
        opciones=["Zelda", "Peach", "Daisy", "Luigi"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="facil"
    ))
    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿En qué consola nació el juego “The Legend of Zelda”? (#{i+1})",
        opciones=["Nintendo Switch", "Nintendo 64", "NES", "GameBoy"],
        respuesta_correcta=2,
        categoria="Videojuegos",
        dificultad="facil"
    ))
    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿Qué popular juego se basa en una “isla de batalla” donde solo uno sobrevive? (#{i+1})",
        opciones=["Fortnite", "Minecraft", "Among Us", "Roblox"],
        respuesta_correcta=0,
        categoria="Videojuegos",
        dificultad="facil"
    ))
    preguntas["Videojuegos"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el nombre del protagonista de la saga “The Legend of Zelda”? (#{i+1})",
        opciones=["Zelda", "Ganon", "Sheik", "Link"],
        respuesta_correcta=3,
        categoria="Videojuegos",
        dificultad="facil"
    ))

  #Intermedio:

    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿En qué videojuego aparece la corporación Umbrella? (#{i+1})",
        opciones=["Silent Hill", "Resident Evil", "Doom", "Left 4 Dead"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))
    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿Qué desarrolladora creó el juego “The Witcher 3”? (#{i+1})",
        opciones=["Bethesda", "BioWare", "CD Projekt RED", "Ubisoft"],
        respuesta_correcta=2,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))
    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿Cómo se llama el antagonista de la saga “Splatoon”? (#{i+1})",
        opciones=["Megan", "DJ Octavio", "Capitán Jibión", "Mar"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))
    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿Cómo se llama el planeta natal de los Metroids en la saga “Metroid”? (#{i+1})",
        opciones=["SR388", "Zebes", "Tallon 4", "Brinstar"],
        respuesta_correcta=0,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))
    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿Qué videojuego de Rockstar Games se sitúa en el Viejo Oeste? (#{i+1})",
        opciones=["Grand Theft Auto", "Red Dead Redemption", "Max Payne", "Bully"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))
    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿Qué año se lanzó la PlayStation 1? (#{i+1})",
        opciones=["1990", "1993", "1994", "1996"],
        respuesta_correcta=2,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))
    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿Qué juego de rol se desarrolla en el continente ficticio de Tamriel? (#{i+1})",
        opciones=["Dragon Age", "The Witcher", "Baldur's Gate", "The Elder Scrolls"],
        respuesta_correcta=3,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))
    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿Qué arma se usa para derrotar a Ganon en “Zelda: Ocarina of Time”? (#{i+1})",
        opciones=["Tridente", "Hoz del Tiempo", "Lanza del Fuego", "Espada Maestra"],
        respuesta_correcta=3,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))
    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿En qué fue ambientado el primer videojuego de la saga “Call of Duty”? (#{i+1})",
        opciones=["Segunda Guerra Mundial", "Primera Guerra Mundial", "Guerra de Vietnam", "Guerra del Golfo"],
        respuesta_correcta=0,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))
    preguntas["Videojuegos"]["intermedio"].append(Pregunta(
        texto=f"¿En qué juego puedes cazar monstruos gigantes y crear armas con sus partes? (#{i+1})",
        opciones=["Final Fantasy", "Skyrim", "Devil May Cry", "Monster Hunter"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="intermedio"
    ))

  #Dificil:

    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿Cómo se llama la inteligencia artificial antagonista en la saga Halo? (#{i+1})",
        opciones=["GladOs", "A.L.I.E", "Cortana", "Medicant Bias"],
        respuesta_correcta=3,
        categoria="Videojuegos",
        dificultad="dificil"
    ))
    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿Cuál fue el primer videojuego de la historia considerado un “battle royale”? (#{i+1})",
        opciones=["PUBG", "Fortnite", "H1Z1", "DayZ"],
        respuesta_correcta=0,
        categoria="Videojuegos",
        dificultad="dificil"
    ))
    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿En qué juego aparece el personaje “Pyramid Head”? (#{i+1})",
        opciones=["Resident Evil", "Outlast", "Silent Hill", "Dead Space"],
        respuesta_correcta=2,
        categoria="Videojuegos",
        dificultad="dificil"
    ))
    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿Qué estudio creó “Dark Souls”? (#{i+1})",
        opciones=["Capcom", "FromSoftware", "Square Enix", "Konami"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="dificil"
    ))
    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es el nombre real de la protagonista de la saga “Metroid”? (#{i+1})",
        opciones=["Samus Aran", "Sarah Aran", "Selina Maris", "Sandra Orion"],
        respuesta_correcta=0,
        categoria="Videojuegos",
        dificultad="dificil"
    ))
    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿Cuál fue el primer juego de Nintendo en usar gráficos en 3D? (#{i+1})",
        opciones=["Donkey Kong Country", "Star Fox", "Super Mario 64", "F-Zero"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="dificil"
    ))
    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿En qué entrega de “Final Fantasy” apareció por primera vez Sephiroth? (#{i+1})",
        opciones=["FF 5", "FF 7", "FF 9", "FF 10"],
        respuesta_correcta=1,
        categoria="Videojuegos",
        dificultad="dificil"
    ))
    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿Qué significa “MMORPG”? (#{i+1})",
        opciones=["Massive Multiplayer Online Role Playing Game", "Multi Military Online Role Playing Game", "Main Multiplayer Organized Role Playing Game", "Master Mode Online Role Playing Game"],
        respuesta_correcta=0,
        categoria="Videojuegos",
        dificultad="dificil"
    ))
    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿Cuál fue el primer videojuego en tener una secuela numérica directa? (#{i+1})",
        opciones=["Super Mario Bros.", "Pac-Man", "Donkey Kong", "Space Invaders"],
        respuesta_correcta=3,
        categoria="Videojuegos",
        dificultad="dificil"
    ))
    preguntas["Videojuegos"]["dificil"].append(Pregunta(
        texto=f"¿Cuál fue el primer juego que permitió guardar la partida con una batería interna en el cartucho? (#{i+1})",
        opciones=["Super Mario Bros.", "Final Fantasy", "The Legend of Zelda", "Mega Man"],
        respuesta_correcta=2,
        categoria="Videojuegos",
        dificultad="dificil"
    ))

#Ciencia:

  #Facil:

    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el planeta más cercano al Sol? (#{i+1})",
        opciones=["Tierra", "Marte", "Mercurio", "Venus"],
        respuesta_correcta=2,
        categoria="Ciencia",
        dificultad="facil"
    ))
    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Cuántos sentidos tiene el ser humano tradicionalmente? (#{i+1})",
        opciones=["4", "5", "6", "3"],
        respuesta_correcta=1,
        categoria="Ciencia",
        dificultad="facil"
    ))
    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Qué gas es esencial para la respiración humana? (#{i+1})",
        opciones=["Dióxido de carbono", "Nitrógeno", "Oxígeno", "Helio"],
        respuesta_correcta=2,
        categoria="Ciencia",
        dificultad="facil"
    ))
    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Qué líquido circula por nuestras venas y arterias? (#{i+1})",
        opciones=["Agua", "Sangre", "Jugo gástrico", "Linfa"],
        respuesta_correcta=1,
        categoria="Ciencia",
        dificultad="facil"
    ))
    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Qué parte del cuerpo humano bombea la sangre? (#{i+1})",
        opciones=["Corazón", "Pulmón", "Hígado", "Estómago"],
        respuesta_correcta=0,
        categoria="Ciencia",
        dificultad="facil"
    ))
    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el estado del agua a 100 grados Celsius? (#{i+1})",
        opciones=["Sólido", "Líquido", "Plasma", "Gaseoso"],
        respuesta_correcta=3,
        categoria="Ciencia",
        dificultad="facil"
    ))
    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Qué órgano permite respirar a los seres humanos? (#{i+1})",
        opciones=["Pulmón", "Riñón", "Corazón", "Estómago"],
        respuesta_correcta=0,
        categoria="Ciencia",
        dificultad="facil"
    ))
    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Qué astro da luz y calor a la Tierra? (#{i+1})",
        opciones=["Luna", "Marte", "Júpiter", "Sol"],
        respuesta_correcta=3,
        categoria="Ciencia",
        dificultad="facil"
    ))
    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Cómo se llama el proceso por el que las plantas producen su alimento? (#{i+1})",
        opciones=["Respiración", "Digestión", "Fotosíntesis", "Germinación"],
        respuesta_correcta=2,
        categoria="Ciencia",
        dificultad="facil"
    ))
    preguntas["Ciencia"]["facil"].append(Pregunta(
        texto=f"¿Qué animal es conocido por cambiar de color para camuflarse? (#{i+1})",
        opciones=["Camaleón", "Cangrejo", "Perro", "Elefante"],
        respuesta_correcta=0,
        categoria="Ciencia",
        dificultad="facil"
    ))

  #Intermedio:

    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál es la fórmula química del agua? (#{i+1})",
        opciones=["H2O", "CO2", "O2H", "HO2"],
        respuesta_correcta=0,
        categoria="Ciencia",
        dificultad="intermedio"
    ))
    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Qué parte de la célula contiene el material genético? (#{i+1})",
        opciones=["Ribosoma", "Mitocondria", "Núcleo", "Citoplasma"],
        respuesta_correcta=2,
        categoria="Ciencia",
        dificultad="intermedio"
    ))
    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Qué tipo de energía produce una central hidroeléctrica? (#{i+1})",
        opciones=["Nuclear", "Eléctrica", "Eólica", "Solar"],
        respuesta_correcta=1,
        categoria="Ciencia",
        dificultad="intermedio"
    ))
    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Cómo se llama el cambio de estado de sólido a gas directamente? (#{i+1})",
        opciones=["Fusión", "Evaporación", "Condensación", "Sublimación"],
        respuesta_correcta=3,
        categoria="Ciencia",
        dificultad="intermedio"
    ))
    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál es el hueso más largo del cuerpo humano? (#{i+1})",
        opciones=["Fémur", "Húmero", "Tibia", "Columna"],
        respuesta_correcta=0,
        categoria="Ciencia",
        dificultad="intermedio"
    ))
    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Qué científico desarrolló la teoría de la relatividad? (#{i+1})",
        opciones=["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"],
        respuesta_correcta=1,
        categoria="Ciencia",
        dificultad="intermedio"
    ))
    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Qué planeta tiene un gran anillo a su alrededor? (#{i+1})",
        opciones=["Neptuno", "Venus", "Saturno", "Marte"],
        respuesta_correcta=2,
        categoria="Ciencia",
        dificultad="intermedio"
    ))
    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Cómo se llama el órgano principal del sistema nervioso? (#{i+1})",
        opciones=["Estómago", "Corazón", "Médula espinal", "Cerebro"],
        respuesta_correcta=3,
        categoria="Ciencia",
        dificultad="intermedio"
    ))
    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Qué unidad se usa para medir la fuerza? (#{i+1})",
        opciones=["Julio", "Newton", "Pascal", "Voltio"],
        respuesta_correcta=1,
        categoria="Ciencia",
        dificultad="intermedio"
    ))
    preguntas["Ciencia"]["intermedio"].append(Pregunta(
        texto=f"¿Qué tipo de animal es un tiburón? (#{i+1})",
        opciones=["Mamífero", "Anfibio", "Reptil", "Pez"],
        respuesta_correcta=3,
        categoria="Ciencia",
        dificultad="intermedio"
    ))

  #Dificil:

    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es la partícula subatómica con carga negativa? (#{i+1})",
        opciones=["Electrón", "Protón", "Neutrón", "Quark"],
        respuesta_correcta=0,
        categoria="Ciencia",
        dificultad="dificil"
    ))
    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es el nombre del proceso por el cual las células se dividen para formar células hijas idénticas? (#{i+1})",
        opciones=["Meiosis", "Mitosis", "Osmosis", "Fotosíntesis"],
        respuesta_correcta=1,
        categoria="Ciencia",
        dificultad="dificil"
    ))
    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Qué científico propuso el principio de incertidumbre? (#{i+1})",
        opciones=["Niels Bohr", "Albert Einstein", "Werner Heisenberg", "Max Planck"],
        respuesta_correcta=2,
        categoria="Ciencia",
        dificultad="dificil"
    ))
    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Qué elemento químico tiene el símbolo W? (#{i+1})",
        opciones=["Zinc", "Mercurio", "Plata", "Tungsteno"],
        respuesta_correcta=3,
        categoria="Ciencia",
        dificultad="dificil"
    ))
    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Qué nombre recibe el punto más profundo de los océanos? (#{i+1})",
        opciones=["Fosa de las Marianas", "Fosa de Tonga", "Fosa de Puerto Rico", "Fosa de Java"],
        respuesta_correcta=0,
        categoria="Ciencia",
        dificultad="dificil"
    ))
    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Qué ley explica el comportamiento de los gases ideales? (#{i+1})",
        opciones=["Ley de Hooke", "Ley de Boyle-Mariotte", "Ley de Newton", "Ley de Ohm"],
        respuesta_correcta=1,
        categoria="Ciencia",
        dificultad="dificil"
    ))
    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Cuántos pares de cromosomas tiene el ser humano? (#{i+1})",
        opciones=["21", "46", "23", "22"],
        respuesta_correcta=2,
        categoria="Ciencia",
        dificultad="dificil"
    ))
    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Qué órgano produce la insulina en el cuerpo humano? (#{i+1})",
        opciones=["Hígado", "Riñón", "Bazo", "Páncreas"],
        respuesta_correcta=3,
        categoria="Ciencia",
        dificultad="dificil"
    ))
    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Cómo se llama el estado de la materia que se forma a temperaturas extremadamente bajas? (#{i+1})",
        opciones=["Plasma", "Condensado de Bose-Einstein", "Estado amorfo", "Sólido supercrítico"],
        respuesta_correcta=1,
        categoria="Ciencia",
        dificultad="dificil"
    ))
    preguntas["Ciencia"]["dificil"].append(Pregunta(
        texto=f"¿Qué científico descubrió la penicilina? (#{i+1})",
        opciones=["Louis Pasteur", "Robert Koch", "Alexander Fleming", "Marie Curie"],
        respuesta_correcta=2,
        categoria="Ciencia",
        dificultad="dificil"
    ))

#Entretenimiento:

  #Facil:

    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Qué personaje vive en una piña debajo del mar? (#{i+1})",
        opciones=["Mickey Mouse", "Bob Esponja", "Bugs Bunny", "Patricio"],
        respuesta_correcta=1,
        categoria="Entretenimiento",
        dificultad="facil"
    ))
    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el nombre del mago protagonista de la saga escrita por J.K. Rowling? (#{i+1})",
        opciones=["Frodo", "Percy Jackson", "Harry Potter", "Merlín"],
        respuesta_correcta=2,
        categoria="Entretenimiento",
        dificultad="facil"
    ))
    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Qué superhéroe tiene como identidad secreta a Peter Parker? (#{i+1})",
        opciones=["Superman", "Batman", "Iron Man", "Spider-Man"],
        respuesta_correcta=3,
        categoria="Entretenimiento",
        dificultad="facil"
    ))
    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Quién es el ratón más famoso de Disney? (#{i+1})",
        opciones=["Mickey Mouse", "Jerry", "Speedy Gonzales", "Stuart Little"],
        respuesta_correcta=0,
        categoria="Entretenimiento",
        dificultad="facil"
    ))
    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Qué princesa de Disney tiene un vestido amarillo? (#{i+1})",
        opciones=["Bella", "Ariel", "Cenicienta", "Aurora"],
        respuesta_correcta=0,
        categoria="Entretenimiento",
        dificultad="facil"
    ))
    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Qué animal es el amigo de Shrek? (#{i+1})",
        opciones=["Gato", "Burro", "Caballo", "León"],
        respuesta_correcta=1,
        categoria="Entretenimiento",
        dificultad="facil"
    ))
    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Cuál de estos personajes pertenece al universo Marvel? (#{i+1})",
        opciones=["Batman", "Flash", "Thor", "Linterna Verde"],
        respuesta_correcta=2,
        categoria="Entretenimiento",
        dificultad="facil"
    ))
    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Qué personaje dice “¡Hasta el infinito y más allá!”? (#{i+1})",
        opciones=["Woody", "Wall-E", "Mr. Increíble", "Buzz Lightyear"],
        respuesta_correcta=3,
        categoria="Entretenimiento",
        dificultad="facil"
    ))
    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Qué cantante es famosa por la canción “Shake it off”? (#{i+1})",
        opciones=["Ariana Grande", "Lady Gaga", "Taylor Swift", "Katy Perry"],
        respuesta_correcta=2,
        categoria="Entretenimiento",
        dificultad="facil"
    ))
    preguntas["Entretenimiento"]["facil"].append(Pregunta(
        texto=f"¿Cuál es el apellido de los hermanos famosos por sus películas cómicas mudas? (#{i+1})",
        opciones=["Marx", "Warner", "Coen", "Duffer"],
        respuesta_correcta=0,
        categoria="Entretenimiento",
        dificultad="facil"
    ))

  #Intermedio:

    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿Quién protagonizó la película Titanic junto a Kate Winslet? (#{i+1})",
        opciones=["Brad Pitt", "Leonardo DiCaprio", "Tom Hanks", "Johnny Depp"],
        respuesta_correcta=1,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))
    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál es el verdadero nombre del cantante conocido como “The Weeknd”? (#{i+1})",
        opciones=["Abel Tesfaye", "Shawn Mendes", "Jason Derulo", "Bruno Mars"],
        respuesta_correcta=0,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))
    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿Qué saga de películas tiene como protagonistas a los Skywalker? (#{i+1})",
        opciones=["Harry Potter", "El Señor de los Anillos", "Star Wars", "Star Trek"],
        respuesta_correcta=2,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))
    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿Qué actor interpreta a Iron Man en el Universo Cinematográfico de Marvel? (#{i+1})",
        opciones=["Chris Hemsworth", "Chris Evans", "Benedict Cumberbatch", "Robert Downey Jr."],
        respuesta_correcta=3,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))
    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿En qué país se originó el programa “El Chavo del 8”? (#{i+1})",
        opciones=["Colombia", "Argentina", "México", "Perú"],
        respuesta_correcta=2,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))
    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿Cómo se llama el mundo ficticio de la serie “Stranger Things”? (#{i+1})",
        opciones=["El Otro Lado", "Mundo Paralelo", "Upside Down", "Nether"],
        respuesta_correcta=2,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))
    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿Qué grupo lanzó el álbum “Abbey Road”? (#{i+1})",
        opciones=["The Beatles", "Queen", "The Rolling Stones", "Pink Floyd"],
        respuesta_correcta=0,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))
    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿Qué actriz interpreta a Hermione Granger en las películas de Harry Potter? (#{i+1})",
        opciones=["Natalie Portman", "Emma Watson", "Emma Stone", "Keira Knightley"],
        respuesta_correcta=1,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))
    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿Quién es el creador de la serie “Los Simpson”? (#{i+1})",
        opciones=["Seth MacFarlane", "Trey Parker", "Vince Gilligan", "Matt Groening"],
        respuesta_correcta=3,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))
    preguntas["Entretenimiento"]["intermedio"].append(Pregunta(
        texto=f"¿Cuál es el nombre real del rapero Eminem? (#{i+1})",
        opciones=["Curtis Jackson", "Marshall Mathers", "Sean Combs", "Calvin Broadus"],
        respuesta_correcta=1,
        categoria="Entretenimiento",
        dificultad="intermedio"
    ))

  #Dificil:

    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿Qué película ganó el Oscar a Mejor Película en 2020? (#{i+1})",
        opciones=["1917", "Parásitos", "Joker", "Once Upon a Time in Hollywood"],
        respuesta_correcta=1,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))
    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿Cuál es el nombre del dragón en la serie “Game of Thrones” que monta Daenerys? (#{i+1})",
        opciones=["Rhaegal", "Viserion", "Drogon", "Balerion"],
        respuesta_correcta=2,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))
    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿Quién compuso la banda sonora de “Interestelar”? (#{i+1})",
        opciones=["Hans Zimmer", "John Williams", "Ennio Morricone", "James Newton Howard"],
        respuesta_correcta=0,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))
    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿Qué director es famoso por sus películas con tramas no lineales como Pulp Fiction? (#{i+1})",
        opciones=["Quentin Tarantino", "Christopher Nolan", "Martin Scorsese", "David Flincher"],
        respuesta_correcta=0,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))
    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿Cómo se llama el planeta natal de Superman? (#{i+1})",
        opciones=["Vulcano", "Krypton", "Asgard", "Naboo"],
        respuesta_correcta=1,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))
    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿En qué año se estrenó la primera película de “El Señor de los Anillos”? (#{i+1})",
        opciones=["2000", "2001", "2002", "1999"],
        respuesta_correcta=1,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))
    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿Qué actriz ganó el Óscar por su papel en La La Land? (#{i+1})",
        opciones=["Emma Stone", "Natalie Portman", "Jennifer Lawrence", "Amy Adams"],
        respuesta_correcta=0,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))
    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿Qué banda sonora incluye la canción “My Heart Will Go On”? (#{i+1})",
        opciones=["Moulin Rouge", "Romeo y Julieta", "Notting Hill", "Titanic"],
        respuesta_correcta=3,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))
    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿Quién dirigió la trilogía original de Star Wars? (#{i+1})",
        opciones=["Steven Spielberg", "J.J. Abrams", "Ridley Scott", "George Lucas"],
        respuesta_correcta=3,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))
    preguntas["Entretenimiento"]["dificil"].append(Pregunta(
        texto=f"¿Qué serie tiene un episodio famoso llamado “Ozymandias”? (#{i+1})",
        opciones=["Better Call Saul", "The Sopranos", "The Wire", "Breaking Bad"],
        respuesta_correcta=3,
        categoria="Entretenimiento",
        dificultad="dificil"
    ))

# -----------------------------
# Funciones de juego

def obtener_dificultad(nivel):
    return ["facil", "intermedio", "dificil"][nivel]

def jugar_categoria(jugador, categoria):
    nivel_actual = jugador.progreso[categoria]
    if nivel_actual >= 3:
        print(f"✅ Ya ganaste la categoría {categoria}")
        return

    dificultad = obtener_dificultad(nivel_actual)
    if not preguntas[categoria][dificultad]:
        print(f"⚠️ No hay preguntas para {categoria} nivel {dificultad}")
        return

    pregunta = random.choice(preguntas[categoria][dificultad])

    print(f"\n📚 Categoría: {categoria} | Dificultad: {dificultad.upper()}")
    print(pregunta.texto)
    for i, opcion in enumerate(pregunta.opciones):
        print(f"{i + 1}. {opcion}")

    try:
        respuesta = input_con_tiempo("👉 Tu respuesta (1-4): ", timeout=30)
        if not respuesta or not respuesta.isdigit():
            raise ValueError
        if int(respuesta) - 1 == pregunta.respuesta_correcta:
            print("✅ ¡Correcto!")
            jugador.progreso[categoria] += 1
        else:
            print("❌ Incorrecto.")
            jugador.vidas -= 1
    except TiempoAgotado:
        print("⏰ Tiempo agotado.")
        jugador.vidas -= 1
    except ValueError:
        print("❌ Respuesta inválida.")
        jugador.vidas -= 1

def tirar_ruleta(jugador):
    categorias_disponibles = [cat for cat in jugador.progreso if jugador.progreso[cat] < 3]
    if not categorias_disponibles:
        return None
    return random.choice(categorias_disponibles)

@log_turno
def turno(jugador):
    if jugador.vidas <= 0:
        print("💀 Te quedaste sin vidas. ¡Game Over!")
        return False

    categoria = tirar_ruleta(jugador)
    if not categoria:
        print("🏆 ¡Felicitaciones! Ganaste todas las categorías.")
        return False

    print(f"🎡 La ruleta eligió: {categoria}")
    jugar_categoria(jugador, categoria)

    print(f"❤️ Vidas restantes: {jugador.vidas}")
    print("📈 Progreso:")
    for cat, nivel in jugador.progreso.items():
        print(f"  - {cat}: {nivel}/3")

    # ⏳ Pausa de 5 segundos antes del siguiente turno
    import time
    print("⏳ Esperando que la ruleta determine la categoria...")
    time.sleep(5)

    return True


# -----------------------------
# Guardado de resultados

def guardar_resultados(jugadores, archivo="resultados.json"):
    datos = []
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                datos = []

    for j in jugadores:
        datos.append({
            "nombre": j.nombre,
            "categorias_ganadas": sum(1 for nivel in j.progreso.values() if nivel == 3),
            "vidas_restantes": j.vidas,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)

# -----------------------------
# Modo multijugador
# -----------------------------
# Modo multijugador
def modo_multijugador():
    print("🎮 Modo MULTIJUGADOR")
    nombre1 = input("👤 Nombre del Jugador 1: ")
    nombre2 = input("👤 Nombre del Jugador 2: ")

    # Usamos la subclase con herencia
    jugador1 = JugadorMultijugador(nombre1)
    jugador2 = JugadorMultijugador(nombre2)

    jugadores = [(jugador1, "🔵"), (jugador2, "🔴")]

    turno_actual = 0

    while all(j.vidas > 0 for j, _ in jugadores):
        jugador, emoji = jugadores[turno_actual % 2]
        print(f"\n{emoji} Turno de: {jugador.nombre}")
        if not turno(jugador):
            break
        turno_actual += 1

    print("\n📊 Resultados finales:")
    for j, emoji in jugadores:
        categorias_ganadas = sum(1 for nivel in j.progreso.values() if nivel == 3)
        print(f"{emoji} {j.nombre}: {categorias_ganadas} categorías ganadas, {j.vidas} vidas restantes")

    guardar_resultados([jugador1, jugador2])  # Si tenés función para guardar


    # Determinar ganador
    j1, _ = jugadores[0]
    j2, _ = jugadores[1]

    j1_cat = sum(1 for nivel in j1.progreso.values() if nivel == 3)
    j2_cat = sum(1 for nivel in j2.progreso.values() if nivel == 3)

    if j1_cat > j2_cat:
        print(f"\n🏆 ¡{j1.nombre} gana!")
    elif j2_cat > j1_cat:
        print(f"\n🏆 ¡{j2.nombre} gana!")
    else:
        if j1.vidas > j2.vidas:
            print(f"\n⚖️ ¡Empate en categorías, pero {j1.nombre} tiene más vidas y gana!")
        elif j2.vidas > j1.vidas:
            print(f"\n⚖️ ¡Empate en categorías, pero {j2.nombre} tiene más vidas y gana!")
        else:
            print("\n🤝 ¡Empate total!")

    guardar_resultados([j1, j2])

# -----------------------------
# Juego principal

# Juego principal

def main():
    print("🎉 Bienvenido a Preguntados en Python")
    modo = input("¿Querés jugar solo o con un amigo? (1 = solo, 2 = multijugador): ")

    if modo == "2":
        modo_multijugador()
    else:
        nombre = input("👤 Ingresá tu nombre: ")
        jugador = JugadorIndividual(nombre)

        while jugador.vidas > 0 and not jugador.ha_ganado():
            if not turno(jugador):
                break

        if jugador.ha_ganado():
            print(f"\n🏆 ¡Felicitaciones {jugador.nombre}, ganaste el juego!")
        else:
            print(f"\n😢 {jugador.nombre}, perdiste. Mejor suerte la próxima.")

        guardar_resultados([jugador])

if __name__ == "__main__":
    main()
