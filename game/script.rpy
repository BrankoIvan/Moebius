#Santi
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Iniciaciones

define Protagonista = Character("", 
    color = "#ff9100", 
    what_prefix = "{k=3}")

define Narrador = Character("", 
    color = "#008cff",
    what_color="#bdbcfb", 
    what_prefix = "{k=3}{i}")

define Maquinista = Character("Maquinista", 
    color = "#0aff1e8c", 
    what_prefix = "{cps=5}")

define Guardia = Character("Guardia", 
    color = "#ff28288c", 
    what_prefix = "")

default preferences.text_cps = 40

define escena = 1

define destino = None

define fadetime= 0.1
define fade_comun = Fade(fadetime,0.0,fadetime)
define fade_largo = Fade(5,0.0,5)

label start:
    scene black
    show screen inventarioScreen
    jump intro
    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Definicion de Items e Interactuables

define cartel = Interactuable(exCartel, (298,445), exCartelCerca, "descripcionCartel")

label descripcionCartel:
    Narrador "El cartel se encuentra desgastado y roto, no se puede ver el nombre de la estación."
    return

define poster = Interactuable(exPoster, (586,391), exPosterCerca, "descripcionPoster")

label descripcionPoster:
    Narrador "Un afiche sucio y desgastado, parece de una pelicula. La fecha de estreno esta arrancada."
    return

define cigarrillos = Item(exCigarrillos, (1264,354), exCigarrillosCerca, "descripcionCigarrillos", exCigarrillosInventario)

label descripcionCigarrillos:

    Protagonista "Cerrados, y de mi marca favorita."

    menu:
        "tomar":
            $ cigarrillos.agregarAlInvetario()
        
        "dejar":
            pass

    return

define caramelos = Item("", (151,826), "", "descripcionCaramelos", exCaramelosInventario)

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Visitas
define visitadotunelCerrado = False

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Mapa

label vagon:
    $ destino = None
    scene bg vagon with fade_comun
    play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in [1,3]:
        $ renpy.call("escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("cabina","","","anden1" if escena > 2 else "")
        pause
    
    jump expression destino

label cabina:
    $ destino = None
    scene bg cabina with fade_comun
    play music bgm_Entras_en_la_cabina fadeout 1.0 fadein 1.0 loop volume 0.3
    if escena in [2,9]:
        $ renpy.call("escena" + str(escena))
        $ escena += 1
    
    if escena == 10:
        jump ending

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","vagon","")
        pause
    
    jump expression destino

label anden1:
    $ destino = None
    scene bg anden_1 with fade_comun
    play music bgm_Al_salir fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in [4]:
        $ renpy.call("escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("anden2","vagon","","tunel2")
        pause
    
    jump expression destino

label tunel2:
    $ destino = None
    scene bg tunel_2 with fade_comun
    play music bgm_Pasillo_largo fadeout 1.0 fadein 1.0 loop volume 1.5
    if escena in []:
        $ renpy.call("escena" + str(escena))
        $ escena += 1
    
    while destino == None:
        window hide
        show screen flechasDeNavegacion("tunelCerrado","","anden1","")
        pause
    
    jump expression destino

label anden2:
    $ destino = None
    scene bg anden_2 with fade_comun
    play music bgm_Al_salir fadeout 1.0 fadein 1.0 loop volume 0.3
    
    if escena in [8]:
        $ renpy.call("escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        $ cartel.mostrar()
        show screen flechasDeNavegacion("anden_fondo","","anden1","tunel")
        pause
    
    jump expression destino

label anden_fondo:
    $ destino = None
    scene bg anden_fondo with fade_comun
    play music bgm_Pasillo_largo fadeout 1.0 fadein 1.0 loop volume 1.5

    if escena in []:
        $ renpy.call("escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        $ poster.mostrar()
        show screen flechasDeNavegacion("","vias","anden2","baño")
        pause
    
    jump expression destino

label baño:
    $ destino = None
    scene bg baño with fade_comun
    play music bgm_Pasillo_largo fadeout 1.0 fadein 1.0 loop volume 1.5
    
    if escena in []:
        $ renpy.call("escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        $ cigarrillos.mostrar()
        show screen flechasDeNavegacion("","","anden_fondo","")
        pause
    
    jump expression destino

label vias:
    scene black with fade_comun
    play music bgm_Pasillo_largo fadeout 1.0 fadein 1.0 loop volume 1.5

    Protagonista "Esta muy oscuro, es peligroso."

    if escena in []:
        $ renpy.call("escena" + str(escena))
        $ escena += 1

    jump anden_fondo

label tunelCerrado:
    $ destino = None
    scene bg salida_cerrada with fade_comun
    play music bgm_Pasillo_largo fadeout 1.0 fadein 1.0 loop volume 1.5

    if visitadotunelCerrado == False:
        Protagonista "La puta madre."
        $ visitadotunelCerrado = True

    if escena in []:
        $ renpy.call("escena" + str(escena))
        $ escena += 1
    
    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","tunel2","")
        pause
    
    jump expression destino

label tunel:
    $ destino = None
    scene bg tunel_1 with fade_comun
    play music bgm_Pasillo_largo fadeout 1.0 fadein 1.0 loop volume 1.5
    
    if escena in [5]:
        $ renpy.call("escena" + str(escena))
        $ escena += 1
    
    while destino == None:
        window hide
        show screen flechasDeNavegacion("escalera","","anden2","")
        pause
    
    jump expression destino

label escalera:
    $ destino = None
    scene bg escalera with fade_comun
    play music bgm_Escaleras fadeout 1.0 fadein 1.0 loop volume 2
    
    if escena in [7]:
        $ renpy.call("escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("puerta_cerrada","","tunel","")
        pause
    
    jump expression destino

label puerta_cerrada:
    $ destino = None
    scene bg salida_cerrada with fade_comun
    play music bgm_Escaleras fadeout 1.0 fadein 1.0 loop volume 2

    if escena in [6]:
        $ renpy.call("escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","escalera","")
        pause
    
    jump expression destino

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Historia

label intro:
    scene bg opening_1 with fade_comun
    play music bgm_Estas_volviendo_a_casa fadeout 1.0 fadein 1.0 loop volume 0.3

    Narrador "Estás volviendo de una larga jornada laboral en el subte que habitualmente tomas: la línea A de Buenos Aires."
    Narrador "Te quedaste dormido."
    
    scene bg opening_2 with fade_comun
    
    Narrador "El traqueteo constante de las ruedas contra los rieles crea una sinfonía mecánica que te acompaña hace varios años."
    
    scene bg opening_3 with fade_comun
     
    Narrador "Mientras el tren se desliza por debajo de la tierra, los sonidos del mundo exterior se desvanecen gradualmente."
    
    scene bg opening_4 with fade_comun
    
    Narrador "La brisa caliente de la noche te acaricia el rostro, pero no te da consuelo, sino una extraña sensación de opresión."
    
    scene bg despertar with fade_comun
    
    Narrador "Despertas de golpe, transpirado."
    Narrador "El clima pesa sobre tus hombros. Tu cuerpo, sumido en la fatiga, descansa contra los incómodos asientos de plástico."
    Narrador "Tus párpados te pesan, pero no podes volver a cerrarlos."
    Narrador "Una tenue luz azulada se filtra desde las lámparas del vagón, bañando todo de un resplandor particular."
    Narrador "Las voces que normalmente llenan el subte con su murmullo constante han desaparecido, dejando un silencio ensordecedor en su lugar."
    Narrador "El aire se espesa con una tensión palpable, como si algo oscuro acechara en las sombras de Buenos Aires."
    Narrador "Abrís los ojos en un escenario peculiar: el interior del último subte, uno de esos vagones destartalados."
    Narrador "Un escalofrío te recorre la espalda, y te das cuenta de que esta noche, tu viaje de regreso no será el habitual."

    menu:
        "Ponerse de pie":
            jump vagon
        
        "Seguir durmiendo":
            pass
    
    scene bg ojos_cerrados with fade_comun
    
    Protagonista "Solo un poco mas de sueño..."

    menu:
        
        "Abrir los ojos":
            jump vagon
        
        "Seguir durmiendo":
            pass
    
    scene bg sucumbir_oscuridad with fade_largo
    play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3
    Narrador "Te sumís de nuevo en la oscuridad del sueño, pero esta vez, el sueño es oscuro y retorcido."
    Narrador "La penumbra se torna opresiva, y sentis que la realidad se desgarra a tu alrededor."
    Narrador "Las sombras adquieren vida propia, retorciéndose y contorsionándose como seres de pesadilla."
    play sound sfx_Sepulcro fadeout 1.0 fadein 1.0 volume 0.3
    Protagonista "Las sombras... se enroscan..."
    Protagonista "Me susurran secretos incomprensibles..."
    Narrador "Te tambaleas en el oscuro vagón del subte, perdido en un espiral de locura."
    Narrador "Las sombras se convierten en espectros que te rodean,susurrando palabras ininteligibles que perforan tu mente como dagas afiladas." 
    Protagonista "El subte... mi tumba..."
    Protagonista "Soy el prisionero de esta pesadilla."
    Narrador "El subte es ahora tu sepulcro, y vos sos el prisionero condenado a una pesadumbre eterna,donde el eco de una risa maníaca resuena en el abismo."

    menu:        
        "Sucumbir a la oscuridad":
            pass
    
    jump BadEnding

label escena1:
    
    Narrador "Decidís que es hora de ponerte de pie. Te estiras y bostezas, estirando los músculos rígidos después de un largo día."
    Narrador "Tu mirada, lenta y pesada, se posa en la única fuente de luz en la penumbra que te rodea: una puerta solitaria, iluminada en medio de la oscuridad."
    Narrador "Miras a tu alrededor y notas que el vagón está vacío. Todos los pasajeros que te rodeaban desaparecieron misteriosamente."
    
    scene bg puerta_vagon_cerrada with fade_comun

    Narrador "La puerta está cerrada. Estás atrapado en el subte y no podés evitar sentir una oleada de ansiedad que recorre tu espina dorsal."

    scene bg vagon with fade_comun
    
    Protagonista "¡¿Hola? ¿Hay alguien ahí?"  
    
    return

label escena2:
    
    Narrador "La cabina del maquinista se extiende frente tuyo, una maraña de controles y palancas en un espacio reducido"
    Narrador "Los controles están manchados de grasa y, en el rincón, ves montones de envoltorios de caramelos."
    
    show spr maquinista with dissolve
    
    Narrador "El maquinista se gira lentamente en su silla hacia vos."
    
    menu:
        "¡Hola, loco! ¿Qué onda? ¿Por qué está cerrada la puerta? ¿Este subte es el último de la noche, che? ¿Dónde mierda estoy?":
            pass
   
    Maquinista "D u l c e . . ."

    menu:
        "Caramelos... ¿Estás hablando en serio? Necesito respuestas, no caramelos. ¿Qué está pasando?":
            Maquinista "D u l c e..."
            Protagonista "Tomatela, rarito..."

        "Esto no es gracioso. Si no me decís lo que necesito saber, puedo volverte la vida un infierno, amigo.":
            Maquinista "D u l c e..."
            Protagonista "Tomatela, rarito..."

        "¿Caramelos, decís? Che, ¿tenemos que hacer algo con golosinas para que esto funcione?":
            Maquinista "D u l c e..."
            Protagonista "Bueno... está bien... Gracias, amigo."
            
    hide spr maquinista with dissolve

    return

label escena3:
    scene bg puerta_abriendo with fade_comun
    play sound sfx_Puerta_se_abre fadeout 1.0 fadein 1.0 volume 0.3
    Protagonista "Al menos me abrió la puerta..."

    scene bg vagon with fade_comun

    return

label escena4:
    Narrador "Finalmente, te aventuras fuera del vagón y te encontras en el andén de la estación."
    Narrador "Debería estar lleno de gente esperando el tren, pero la soledad te envuelve."
    Narrador "Los viejos asientos de madera se alinean a lo largo del andén, vacíos y desgastados por el tiempo."
    Narrador "Un eco lejano de tus propios pasos es lo único que rompe el silencio en este lugar abandonado."
    
    return

label escena5:
    Narrador "Una figura, apenas perceptible, acecha en el confín del pasillo"
    Narrador "Sus contornos se desdibujan en la penumbra, pero su presencia es innegable."
    Narrador "La sensación de que alguien o algo te observa te eriza la piel."
    Narrador "La figura permanece quieta como una estatua en medio de la oscuridad, esperando, observando."
    Narrador "Tu corazón late con fuerza y sentís un nudo en el estómago."

    return

label escena6:
    Narrador "La puerta de salida, que normalmente estaría abierta a esta hora, está sellada con una barrera de acero."
    Narrador "La frustración te invade; el agotamiento de la larga jornada te carcome y tu paciencia llega a su límite."
    Narrador "El sueño te arrebata la cordura, y te preguntas cómo has llegado a esta situación absurda."
    Narrador "Las palabras de descontento fluyen de tus labios, maldecidas por tu cansancio."
    Protagonista "¡La concha de la lora, no puede ser! ¿Qué mierda pasa con esta puerta, eh?"
    Narrador "Las luces parpadeantes del andén arrojan una sombra intermitente sobre la puerta cerrada, como si se burlaran de tu impotencia."
    Narrador "Estás atrapado en este lugar desconcertante, y la realidad comienza a desdibujarse mientras la fatiga se apodera de vos."

    return

label escena7:
    play music bgm_Escaleras fadeout 1.0 fadein 1.0 loop volume 1.5
    Narrador "Después de atravesar el oscuro pasillo, te encontrás al pie de las escaleras."
    Narrador "La presencia extraña que lo ace   cha se vuelve más intensa a medida que se acerca."
    
    show spr seguridad with dissolve
    
    Narrador "De repente, un guardia deformado, apenas reconocible como humano, aparece en la oscuridad. Te mira con una ceja alzada."
    Guardia "¿Qué haces acá, pibe?"
    Protagonista " ¡La concha de la lora! Estoy re perdid... me quedé dormido en el subte y necesito salir"
    Protagonista "¿Entendés?"


    Guardia "Tranquilo, tranquilo. No podés salir por acá, tenés que ir a la siguiente estación."

    menu:
        "¡¿Qué?! ¡Si este era el último subte de la noche, no hay más!":
            Guardia "¿El último? Todavía no partió, estás a tiempo. Vení, el último subte te está esperando."
            Guardia "Por ahí los necesitas más que yo, pibe."
            $ caramelos.agregarAlInvetario()
            Protagonista "Bueno. ¡Gracias!"
        
        "¿Y si me abris la puerta? Tengo algo que capaz te interese…" if cigarrillos.estaEnInventario:
            Guardia "¿Cigarrillos, decís?"
            Protagonista "Exacto, amigo. Y estos no son cualquier cosa, son de calidad."
            $ cigarrillos.sacarDelInvetario()
            Guardia "Bueno, pibe, parece que tenés buenos gustos. Pero sí, estos cigarrillos son codiciados por estos lares. Tomá."
            $ caramelos.agregarAlInvetario()
            Protagonista "¿Un caramelo?"
            Guardia "Mirá, acá abajo, los caramelos son como moneda de cambio, y si necesitas moverte entre estaciones, vas a requerir varios."
            Guardia "El loco de la cabina solo te va a llevar a cambio de caramelos media hora, ni idea que le pasa."
            Protagonista "Gracias por todo loco, nos vemos."

        "¡No me vengas con boludeces! ¿Sabes que este era el último subte de la noche? ¿O necesitás un dibujo, pelotudo?":
            Guardia "Por ahí te hacen bien, amargo."
            $ caramelos.agregarAlInvetario()
            Guardia "Cuidado con lo que decís, pibe."
            Guardia "En este ambiente no te hagas el vivo que te bajan enseguida."
    
    hide spr guardia with dissolve

    return

label escena8:
    Protagonista "Qué quilombo, che, el guardia tenía razón. El subte sigue parado acá. Es re raro pero..."
    Protagonista "Puede ser que los caramelos sean la posta para zafar."

    return
    
label escena9:
    show spr maquinista with dissolve
    
    Protagonista "Che, necesito llegar a la próxima estacion para poder salir, me estas entendido, ¿no?"
    Maquinista "D u l c e . . ."

    menu:
        "Bueno, dale. Toma los caramelo, rarito":
            $ caramelos.sacarDelInvetario()

    hide spr maquinista with dissolve

    return

label BadEnding:
    scene black with fade_largo
    return

label ending:
    scene bg subte_viaje with fade_largo

    pause 3
    
    return
