#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Iniciaciones

define Protagonista = Character("", 
    color = "#ff9100", 
    what_prefix = "{k=3}",
    callback=voz_prota)

define Narrador = Character("", 
    color = "#008cff",
    what_color="#bdbcfb", 
    what_prefix = "{k=3}{i}",
    callback=voz_prota)

define Maquinista = Character("Maquinista", 
    color = "#0aff1e8c", 
    what_prefix = "{cps=5}",
    callback=voz_dario)

define Guardia = Character("Guardia", 
    color = "#ff28288c",
    callback=voz_guardia)

define Alma_perdida = Character("???", 
    color = "#ff28288c",
    callback=voz_dario)

default preferences.text_cps = 40

define escena = None
define cambio = None
define destino = None
define visitadotunelCerrado = None
define camara_menu_option1 = True
define karma = 0

define fadetime = 0.1
define fade_comun = Fade(fadetime, 0.0, fadetime)
define fade_largo = Fade(5, 0.0, 5)

define cartel = None
define poster = None
define mochila = None
define espejo = None
define cartel_vacio = None
define cigarrillos = None
define caramelos = None
define camara = None

label start:
    scene black
    
    call inicializacionDeVariables from _call_inicializacionDeVariables
    
    jump intro

label inicializacionDeVariables:
    python:
        escena = 1
        destino = None
        visitadotunelCerrado = False

        Item.inventario = []
        
        cartel = Interactuable(exCartel, (375,450), exCartelCerca, "descripcionCartel", audio.sfx_Cartel)
        poster = Interactuable(exPoster, (586,391), exPosterCerca, "descripcionPoster", audio.sfx_Poster)
        mochila = Interactuable(exMochila, (501,600), exMochilaCerca, "descripcionMochila", audio.sfx_Mochila)
        espejo = Interactuable(exEspejo, (840,279), exEspejoCerca, "descripcionEspejo", audio.sfx_Espejo)
        cartel_vacio = Interactuable(exCartelVacio, (726,382), exCartelVacioCerca, "descripcionCartelVacio", audio.sfx_Cartel_Vacio)
        
        cigarrillos = Item(exCigarrillos, (341,796), exCigarrillosCerca, "descripcionCigarrillos", audio.sfx_Cigarillos, exCigarrillosInventario)
        caramelos = Item("", (0,0), "", "", audio.sfx_Caramelos, exCaramelosInventario)        
        camara = Item(exCamara, (492,87), exCamaraCerca, "descripcionCamara", audio.sfx_Camara, exCamaraInventario)
    
    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Definicion de Items e Interactuables

label descripcionCartel:
    Narrador "El cartel se encuentra desgastado y roto, no se puede ver el nombre de la estación."
    return

label descripcionPoster:
    Narrador "Un afiche sucio y desgastado, parece de una película. La fecha de estreno está arrancada."
    return

label descripcionMochila:
    Narrador "Revisás la mochila tirada en busca de pistas sobre su dueño, pero no encontrás ninguna información significativa."
    return

label descripcionEspejo:
    Narrador "Un espejo roto cuelga sobre una pileta rota, como si una fuerza sobrenatural lo hubiera destruido."
    Narrador "Intentaste ver tu rostro en el espejo, pero solo pudiste distinguir una vaga silueta masculina. "
    Narrador "De repente, te invadió una sensación de desesperación: ¿acaso habías olvidado tu propio rostro?"
    return

label descripcionCartelVacio:
    Narrador "El cartel de señalización estaba en blanco como una puerta abierta a la locura"
    return

label descripcionCigarrillos:
    Narrador "Una lata de cigarrillos, un objeto de otro tiempo."

    menu:
        "Tomar":
            $ cigarrillos.agregarAlInvetario()
        
        "Dejar":
            pass

    return

label descripcionCamara:
    Narrador "Una cámara de fotos abandonada, con el obturador oxidado y la lente empañada, evoca recuerdos de un pasado olvidado."

    menu:
        "Tomar":
            $ camara.agregarAlInvetario()
        
        "Dejar":
            pass

    return
