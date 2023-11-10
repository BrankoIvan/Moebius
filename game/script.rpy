#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Iniciaciones

define Protagonista = Character("", 
    color = "#ff9100", 
    what_prefix = "{k=3}",
    callback=voz_lenta)

define Narrador = Character("", 
    color = "#008cff",
    what_color="#bdbcfb", 
    what_prefix = "{k=3}{i}",
    callback=voz_lenta)

define Maquinista = Character("Maquinista", 
    color = "#0aff1e8c", 
    what_prefix = "{cps=5}",
    callback=voz_lenta)

define Guardia = Character("Guardia", 
    color = "#ff28288c",
    callback=voz_lenta)

default preferences.text_cps = 40

define escena = None
define destino = None
define visitadotunelCerrado = None

define fadetime = 0.1
define fade_comun = Fade(fadetime, 0.0, fadetime)
define fade_largo = Fade(5, 0.0, 5)

define cartel = None
define poster = None
define cigarrillos = None
define caramelos = None

label start:
    scene black
    
    call inicializacionDeVariables from _call_inicializacionDeVariables
    
    jump intro

label inicializacionDeVariables:
    python:
        escena = 1
        destino = None
        visitadotunelCerrado = False
        
        cartel = Interactuable(exCartel, (298,445), exCartelCerca, "descripcionCartel")
        poster = Interactuable(exPoster, (586,391), exPosterCerca, "descripcionPoster")
        
        cigarrillos = Item(exCigarrillos, (1264,354), exCigarrillosCerca, "descripcionCigarrillos", exCigarrillosInventario)
        caramelos = Item("", (151,826), "", "descripcionCaramelos", exCaramelosInventario)
    
    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Definicion de Items e Interactuables

label descripcionCartel:
    Narrador "El cartel se encuentra desgastado y roto, no se puede ver el nombre de la estación."
    return

label descripcionPoster:
    Narrador "Un afiche sucio y desgastado, parece de una pelicula. La fecha de estreno esta arrancada."
    return

label descripcionCigarrillos:

    Protagonista "Cerrados, y de mi marca favorita."

    menu:
        "tomar":
            $ cigarrillos.agregarAlInvetario()
        
        "dejar":
            pass

    return
