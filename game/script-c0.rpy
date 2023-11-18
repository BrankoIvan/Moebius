#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Mapa

label vagon:
    $ destino = None
    scene bg vagon with fade_comun
    play music bgm_Vagon fadeout 1.0 fadein 1.0 loop volume 1

    if escena in [1,3]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio

    while destino == None:
        window hide
        show screen flechasDeNavegacion("cabina","","","anden1" if escena > 2 else "")
        pause
    
    jump expression destino

label cabina:
    $ destino = None
    scene bg cabina with fade_comun
    play music bgm_Cabina fadeout 1.0 fadein 1.0 loop volume 1

    if escena in [2,10]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio
    
    if escena == 11:
        jump ending

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","vagon","")
        pause
    
    jump expression destino

label anden1:
    $ destino = None
    scene bg anden_1 with fade_comun
    play music bgm_Anden1 fadeout 1.0 fadein 1.0 loop volume 1

    if escena in [4,9]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio

    while destino == None:
        window hide
        show screen flechasDeNavegacion("anden2","vagon","","tunel2")
        pause
    
    jump expression destino

label tunel2:
    $ destino = None
    scene bg tunel_2 with fade_comun
    play music bgm_Tunel2 fadeout 1.0 fadein 1.0 loop volume 1

    if escena in []:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio
    
    while destino == None:
        window hide
        $ mochila.mostrar()
        show screen flechasDeNavegacion("tunelCerrado","","anden1","")
        pause
    
    jump expression destino

label anden2:
    $ destino = None
    scene bg anden_2 with fade_comun
    play music bgm_Anden2 fadeout 1.0 fadein 1.0 loop volume 1
    
    if escena in [8]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio

    while destino == None:
        window hide
        $ cartel.mostrar()
        show screen flechasDeNavegacion("anden_fondo","","anden1","tunel")
        pause
    
    jump expression destino

label anden_fondo:
    $ destino = None
    scene bg anden_fondo with fade_comun
    play music bgm_Anden2 fadeout 1.0 fadein 1.0 loop volume 1

    if escena in []:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio

    while destino == None:
        window hide
        $ poster.mostrar()
        show screen flechasDeNavegacion("","vias","anden2","baño")
        pause
    
    jump expression destino

label baño:
    $ destino = None
    scene bg baño with fade_comun
    play music bgm_Baño fadeout 1.0 fadein 1.0 loop volume 1
    
    if escena in []:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio

    while destino == None:
        window hide
        $ espejo.mostrar()
        show screen flechasDeNavegacion("","","anden_fondo","baño_2")
        pause
    
    jump expression destino

label baño_2:
    $ destino = None
    scene bg baño_2 with fade_comun
    play music bgm_Baño fadeout 1.0 fadein 1.0 loop volume 1
    
    if escena in []:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio

    while destino == None:
        window hide
        $ camara.mostrar()
        show screen flechasDeNavegacion("","","baño","")
        pause
    
    jump expression destino

label vias:
    $ destino = None
    scene bg vias with fade_comun
    play music bgm_Vias fadeout 1.0 fadein 1.0 loop volume 1

    if escena in []:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio
    
    while destino == None:
        window hide
        $ cigarrillos.mostrar()
        show screen flechasDeNavegacion("vias_2","","","anden_fondo")
        pause
    
    jump expression destino

label vias_2:
    scene black with fade_comun
    play music bgm_Vias fadeout 1.0 fadein 1.0 loop volume 1

    Protagonista "Está muy oscuro, es peligroso."

    if escena in []:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio

    jump vias

label tunelCerrado:
    $ destino = None
    scene bg salida_cerrada with fade_comun
    play music bgm_Puertas_Cerradas fadeout 1.0 fadein 1.0 loop volume 1
    

    if visitadotunelCerrado == False:
        Protagonista "Tendré que salir por otro lado."
        $ visitadotunelCerrado = True
    else:
        Protagonista "..."

    if escena in []:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio
    
    while destino == None:
        window hide
        $ cartel_vacio.mostrar()
        show screen flechasDeNavegacion("","","tunel2","")
        pause
    
    jump expression destino

label tunel:
    $ destino = None
    scene bg tunel_1 with fade_comun
    play music bgm_Tunel1 fadeout 1.0 fadein 1.0 loop volume 1
    
    if escena in [5]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio
    
    while destino == None:
        window hide
        show screen flechasDeNavegacion("escalera","","anden2","")
        pause
    
    jump expression destino

label escalera:
    $ destino = None
    scene bg escalera with fade_comun
    play music bgm_Escaleras fadeout 1.0 fadein 1.0 loop volume 1
    
    if escena in [7]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio

    while destino == None:
        window hide
        show screen flechasDeNavegacion("puerta_cerrada","","tunel","")
        pause
    
    jump expression destino

label puerta_cerrada:
    $ destino = None
    scene bg salida_cerrada with fade_comun
    play music bgm_Puertas_Cerradas fadeout 1.0 fadein 1.0 loop volume 1

    if escena in [6]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += cambio

    while destino == None:
        window hide
        $ cartel_vacio.mostrar()
        show screen flechasDeNavegacion("","","escalera","")
        pause
    
    jump expression destino

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Historia

label intro:
    scene bg cerrar_ojos with fade_comun
    play music bgm_Tren_Llegando fadeout 1.0 fadein 1.0 loop volume 2

    Narrador "Estás volviendo de una larga jornada laboral en el subte que habitualmente tomás..." 
    Narrador "La línea A de Buenos Aires."
    Narrador "La fatiga te vence y te quedás dormido."
    
    scene bg sueño_1 with fade_comun
    
    Narrador "Soñás en la niebla de la memoria, con rostros que son relámpagos de antaño."

    scene bg sueño_2 with fade_comun

    Narrador "Con vínculos rotos y destellos de amores pasados."
    
    scene bg cerrar_ojos with fade_comun
     
    Narrador "El ser humano se encuentra en un viaje onírico..."
    Narrador "Una danza sin fin por las profundidades más oscuras de su ser."
    Narrador "En ese rincón entre el deseo y el horror, la conciencia se manifiesta, susurrando desde un abismo insondable."
    Narrador "¿Qué impulsa el rumbo de tu existencia?"
    
    menu:
        "Destino":
            $ karma = +1 
            Narrador "¿El destino está escrito en las estrellas, o es solo una ilusión?"
            pass
        "Elección":
            $ karma = +0
            Narrador "¿Sos el dueño de tu propio destino, o estás a merced de las circunstancias?"
            pass
        "Caos":
            $ karma = -1
            Narrador "¿El universo es un lugar aleatorio e impredecible, o hay un orden oculto que lo rige?"
            pass     
    
    Narrador "¿Qué inflama el latido de tu corazón? ¿Cuál llama ardiente guía tus pasos hacia el horizonte desconocido?"

    menu:
        
        "La compasión por los demás.":
            $ karma = +1 
            Narrador "¿Querés ayudar a los demás, o hacer del mundo un lugar mejor?"
            pass 
        "La búsqueda de la verdad.":
            $ karma = +0
            Narrador "¿Querés comprender el mundo que te rodea, o descubrir los secretos del universo?"
            pass
        "La venganza":
            $ karma = -1
            Narrador "¿Querés vengarte de los que te han hecho daño, o perdonarlos y seguir adelante?"
            pass
        
    scene bg opening_1 with fade_comun
    Narrador "Te despertás abruptamente en el vagón del subte."
    Narrador "Todos los pasajeros que te rodeaban desaparecieron misteriosamente."
    scene bg opening_2 with fade_comun
    Narrador "El aire es frío y húmedo, y parece impregnado de algo extraño..."
    Narrador "Algo que no podrías identificar."
    scene bg opening_3 with fade_comun
    play audio sfx_Voces fadeout 1.0 fadein 1.0 volume 1.5
    Narrador "Cansado, buscás reconocer un entorno que se muestra anormal, casi onírico..."
    Narrador "Que sugiere realidades incomprensibles."
    Narrador "Los asientos de plástico parecen más incómodos que nunca..."
    scene bg opening_4 with fade_comun
    Narrador "Y el constante traqueteo del tren, esa sinfonía mecánica, es ahora tu única compañía."
    scene bg despertar with fade_comun
    play audio sfx_Subte_Frenando fadeout 1.0 fadein 1.0 volume 1.5
    Narrador "Una tenue luz se filtra desde las lámparas del vagón, bañando todo de un resplandor particular."

    menu:
        "Ponerse de pie":
            jump vagon
        
        "Seguir durmiendo":
            pass
    
    scene bg cerrar_ojos with fade_comun
    play music bgm_Vagon fadeout 1.0 fadein 1.0 loop volume 1.5
    Protagonista "Solo un poco mas de sueño..."

    menu:
        
        "Ponerse de pie":
            jump vagon
        
        "Seguir durmiendo":
            pass
    
    scene bg sucumbir_oscuridad with fade_largo
    play music bgm_Sucumbir_Oscuridad fadeout 1.0 fadein 1.0 loop volume 2

    Narrador "Te sumís de nuevo en la oscuridad del sueño, pero esta vez, el sueño es oscuro y retorcido."
    Narrador "La penumbra se torna opresiva, y sentis que la realidad se desgarra a tu alrededor."
    Narrador "Las sombras adquieren vida propia, retorciéndose y contorsionándose como seres de pesadilla."
    
    Protagonista "Las sombras... se enroscan..."
    Protagonista "Me susurran secretos incomprensibles..."
    Narrador "Te tambaleas en el oscuro vagón del subte, perdido en un espiral de locura."
    Narrador "Las sombras se convierten en espectros que te rodean,susurrando palabras ininteligibles que perforan tu mente como dagas afiladas." 
    Protagonista "El subte... mi tumba..."
    Protagonista "Soy el prisionero de esta pesadilla."

    play audio sfx_Risa fadeout 1.0 fadein 1.0 volume 3

    Narrador "El subte es ahora tu sepulcro, y vos sos el prisionero condenado a una pesadumbre eterna,donde el eco de una risa maníaca resuena en el abismo."

    menu:      
        "Sucumbir a la oscuridad":
            pass
    
    jump BadEnding

label c0escena1:

    play music bgm_Vagon fadeout 1.0 fadein 1.0 loop volume 1
    Narrador "Decidís que es hora de ponerte de pie." 
    Narrador "Te estirás y bostezás, estirando los músculos rígidos después de un largo día."
    Narrador "Tu mirada, lenta y pesada, se posa en la única fuente de luz en la penumbra que te rodea..." 
    Narrador "Una puerta solitaria, iluminada en medio de la oscuridad."
        
    scene bg puerta_vagon_cerrada with fade_comun

    Narrador "La puerta está cerrada." 
    Narrador "Estás atrapado en el subte y no podés evitar sentir una oleada de ansiedad que recorre tu espina dorsal."

    scene bg vagon with fade_comun
    
    Protagonista "¡¿Hola? ¿Hay alguien ahí?¡Estoy atrapado en el subte!"
    
    $ cambio = 1
    return

label c0escena2:

    play music bgm_Cabina fadeout 1.0 fadein 1.0 loop volume 1
    Narrador "La cabina del maquinista se extiende frente tuyo, una maraña de controles y palancas en un espacio reducido."
    Narrador "Los controles están manchados de grasa y, en el rincón, ves montones de envoltorios de caramelos."
    
    show spr maquinista with dissolve
    play music musica_maquinista fadeout 1.0 fadein 1.0 loop volume 1

    Narrador "El maquinista se gira lentamente en su silla hacia vos."
    
    menu:
        "¿Me podrías ayudar? Estoy perdido.":
            $ karma = +1
            Protagonista "Buenas noches ¿Cómo le va? Me quedé dormido y no sé donde estoy ¿Podrías ayudarme?"
            pass
        "¿Cuándo vuelve a andar el subte?":
            $ karma = +0
            Protagonista "Buenas noches, ¿Tenés idea si este era el último subte? ¿Cómo puedo irme?"
            pass
        "¿Por qué estoy encerrado acá?":
            $ karma = -1
            Protagonista "Disculpame ¿Acaso es normal encerrar pasajeros dentro del subte?"
            pass

    Maquinista "C a r a m e l o s . . ."

    menu:
        "¿Querés caramelos?":
            $ karma = +1
            Protagonista "¿Caramelos? Puedo traértelos pero necesitaría salir del vagón..."
            pass

        "¿Qué querés decir con caramelos?":
            $ karma = +0
            Protagonista "¿Qué significa esto? No entiendo para qué los querés..."
            pass

        "¿Caramelos? No tengo...":
            $ karma = -1
            Protagonista "No te voy a dar caramelos, pero necesito respuestas. ¿Por qué necesitas esos caramelos?"
            pass

    Maquinista "C a r a m e l o s . . ."

    menu:
        "¿Por qué?":
            pass

    Protagonista "¿Por qué solo decís “caramelos”?"
    Protagonista "No entiendo..."
    
    Maquinista "C a"
    Maquinista "r a"
    Maquinista "m e"
    Maquinista "l o s ..."

    Narrador "Parece que es lo único que puede pronunciar."     
    Narrador "Como si fuera la única cosa que su mente es capaz de recordar."
    Narrador "O la única que su alma pueda soportar decir..."  
            
    hide spr maquinista with dissolve
    #probar poner la puerta abriendo aca a ver si no aparece el minisalto?    
    $ cambio = 1
    return

label c0escena3:
    scene bg puerta_abriendo with fade_comun
    play audio sfx_Puerta fadeout 1.0 fadein 1.0 volume 1

    Narrador "La puerta se abre."
    Narrador "¿Será obra del maquinista o acaso una fuerza innombrable alteró esta escena?"

    scene bg vagon with fade_comun

    $ cambio = 1

    return

label c0escena4:
    play music bgm_Anden1 fadeout 1.0 fadein 1.0 loop volume 1
    Narrador "El andén del subte es un abismo sin fondo que se abre a la oscuridad."
    Narrador "Los viejos asientos de madera se alinean a lo largo del andén, vacíos y desgastados por el tiempo."
    Narrador "Las luces apenas iluminan los rincones proyectando extrañas sombras."
    Narrador "Un eco lejano de tus propios pasos es lo único que rompe el silencio en este lugar abandonado."
    $ cambio = 1
    return

label c0escena5:
    play music bgm_Tunel1 fadeout 1.0 fadein 1.0 loop volume 1
    Narrador "Algo se mueve en la oscuridad."
    Narrador "Una sombra espesa que desafía la lógica y la percepción humana."
    Narrador "Como si fuese una manifestación de un rincón olvidado de la realidad."
    Narrador "Una entidad pareciera aguardar paciente en el abismo entre el mundo conocido y lo desconocido."
    Narrador "La sensación de que alguien o algo te observa te eriza la piel."
    Narrador "Tu corazón late con fuerza y sentís un nudo en el estómago."
    $ cambio = 1
    return

label c0escena6:
    play music bgm_Puertas_Cerradas fadeout 1.0 fadein 1.0 loop volume 1
    Protagonista "¡La puta madre! ¿Y ahora cómo salgo?"
    Narrador "El aire pesado se adhiere a tus pulmones."
    Narrador "Se posan en esa puerta cerrada."
    Narrador "Un muro impenetrable que desafía tu libertad."
    $ cambio = 1
    return

label c0escena7:
    play music bgm_Escaleras fadeout 1.0 fadein 1.0 loop volume 1
    
    Narrador "Sentís que algo desciende por las escaleras, un sutil escalofrío recorre tu cuerpo."
    Narrador "Un alma perdida aparece ante vos, como una figura borrosa en las penumbras del lugar."
    Narrador "Sus movimientos son erráticos y titubeantes, como si estuviera perdido entre la realidad y la ilusión."
    Narrador "Su aspecto denota confusión y su mirada, perdida en un enigma del que parece incapaz de escapar."
    Narrador "Su voz, trémula y vacilante, apenas logra articular palabras coherentes."
    Narrador "Te acercás con cierto temor a este ser."

    show spr alma with dissolve

    if not camara.estaEnInventario:
        Alma_perdida "Cámara... cámara... cámara"
        Protagonista "¿Hola?"
        Alma_perdida "Mi ... cámara ... mi ... cámara"
        Narrador "Parece que no vas a tener otra respuesta"
        $ cambio = 0
        return

    menu:
        "¿Estás bien?":
            $ karma += 1
            Protagonista "Hola. Disculpame pero... ¿Te puedo ayudar con algo? ¿Estás bien?"
            Alma_perdida "No... sé... estoy... atrapado. Necesito.... recuperar.... cámara..."
        
        "¿Sabés donde hay una salida?":
            Alma_perdida " ...Necesito mi cámara... mi cámara... necesito ...mi... cámara...."
        
        "¿Por qué te ves así?":
            Protagonista "¿Por qué tenés ese aspecto?"
            Narrador "La sombra se detiene momentáneamente, su apariencia se torna más sombría y triste."
            Alma_perdida "No ... sé.. estoy... perdido... atrapado... necesito... cámara..."

    menu:
        "¿Cámara?":
            pass
    
    Protagonista "¿Estás buscando esto? La encontré en el baño."
    Alma_perdida "Mi..." 
    
    show spr seguridad with dissolve

    Guardia "¡Epa, una cara nueva por acá! ¿Y vos, pibe? ¿Qué hacés en este lugar a estas horas?"
    Protagonista "Estaba intentando ayudarlo... Parece que perdió algo."
    Guardia "No te confíes tan fácilmente, pibe. Todos se aprovechan en estos lados. ¿Y vos...?"

    menu:
        "Solo soy un pasajero":
            Protagonista "Solo soy un pasajero del subte, tratando de..."
        
        "Quiero salir de este infierno":
            $ karma -= 1
            Protagonista "Señor, me quedé dormido y..."
    
    Guardia "Está bien... no hay necesidad de que te expliques tanto. Mejor seguí tu camino y no te entrometas donde no te llaman. Acá no queremos problemas."
    Protagonista "Está bien, no quiero problemas."
    Guardia "Y vos, vení conmigo."
    Alma_perdida "Solo... mi cámara, no quería..."
    Protagonista "¿Esta cámara?"
    Guardia "¿Qué tal si me das esa cámara, pibe? No deberías estar metido en asuntos que no te corresponden."
    Alma_perdida "Por favor..."

    menu camara_menu:
        "¿Por qué querés la cámara?" if camara_menu_option1:
            $ camara_menu_option1 = False
            
            Protagonista "No termino de entender porque querés tener este artefacto tan viejo."
            Guardia "Solo entrégala y nadie va a salir lastimado. Este hijo de puta es peligroso."
            Alma_perdida "Por favor..."
            
            jump camara_menu
        
        "Acá tenés la cámara":
            $ karma -= 10
            Narrador "Al dar la cámara, sentís una una sensación etérea e inexplicable rodeándote, como si algo más estuviera en juego."
            Narrador "No te confíes, en este subte, hay cosas que van más allá de lo que ves. ¿Te animás a descubrir lo que espera?"
            
            menu:
                "No dar la cámara": 
                    $ karma += 5
                    jump .noDarCamara
                
                "Dar la cámara":
                    jump .darCamara

        "No te voy a dar la cámara.":
            $ karma += 10
            Guardia "Vas a tener problemas si no cooperas, pibe."
            Alma_perdida "Por... favor... no... lo.... hagas...."
            Guardia "Mirá, pibe, vos no tenés idea de lo que significa esto para mí. Es solo un objeto para ese tipo, pero para mí, es mi boleto de salida de esta vida miserable."
            Narrador "Las decisiones precipitadas arrastran consigo infortunios insondables, ¿Estás seguro de tu decisión?"

            menu:
                "No dar cámara":
                    jump .noDarCamara
                
                "Darle la cámara":
                    $ karma -= 20
                    jump .darCamara

    label .darCamara:
        Protagonista "Está bien, acá tenés la cámara. Pero por favor, dejanos en paz. No queremos problemas"
        Alma_perdida "¡NO!... MI CÁMARA... POR FAVOR... MI CÁMARA. MI CÁMARA. MI CÁMARA. MI CÁMARA."
        Guardia "Sos un tipo sensato, pibe."
        
        $ camara.sacarDelInvetario()
        
        Guardia "¿Querés ver cómo lidiamos con los hijos de puta acá abajo?"
        Protagonista "¿Qué está pasando?"
        Guardia "Vamos a hacer un pequeño espectáculo."
        Alma_perdida "POR FAVOR. NO. LO. HAGAS"
        Protagonista "¿Qué hice?"
        Narrador "El guardia tiene un gesto de desdén y sadismo. Sus ojos brillan con malicia mientras observa a su presa, disfrutando de la sensación de poder absoluto sobre los demás."
        Guardia "Acá abajo, se hacen cumplir las reglas, y quien no las respeta paga el precio. Es hora de recordarles a todos dónde están sus límites."
        Narrador "Un escalofrío recorre la habitación cuando el guardia levanta la cámara sobre su cabeza con un brillo retorcido en sus ojos."
        Alma_perdida "POR FAVOR. NO. LO. HAGAS"
        Guardia "Las reglas son claras. Y las consecuencias, inevitables."
        Narrador "Sin un atisbo de humanidad, el guardia tira la cámara con una violencia deliberada contra el piso. El estruendo retumba en la habitación, pero lo que sigue es mucho más macabro."

        #(//Por ahi aca se puede poner todo en negro, o parar el sonido, o hacer un plano detalle de la cara del alma perdida o el guardia)
        
        Narrador "La criatura indefensa, en el momento en que la cámara estalla en mil fragmentos, siente cómo su ser se desgarra." 
        Narrador "No es solo su cuerpo lo que se desintegra, sino su esencia misma, su identidad." 
        Narrador "Se convulsiona en un torbellino de agónica disolución, sus gritos ahora mezclados con un sufrimiento más allá de lo físico, un tormento que trasciende la materia."
        Narrador "Sus gritos se convierten en un aullido desgarrador, un sonido que atraviesa las paredes del subte y resuena en los pasillos. Es un sonido que no es solo de dolor, sino también de miedo, de desesperación, de pérdida."
        Narrador "La habitación se llena con una malevolencia palpable mientras el guardia observa con placer retorcido."
        Narrador "Los restos destrozados de la cámara yacen inertes en el piso, pero la verdadera tragedia residía en la pérdida absoluta y espantosa, cuyo ser ahora vaga disperso por los rincones más oscuros de este lugar festado de maldad."
        
        Guardia "No te hagas drama, todo quedó entre nosotros, ¿viste? A veces hay que hacer lo que hay que hacer para mantener el orden, y vos colaboraste. Así que, tomatelo con calma, ¿eh? Vos entendiste cómo funciona esto. Te la jugaste, y eso se valora."
        Guardia "Bueno, bien ahí, pibe. Gracias por la ayuda. Tomá, esto es para vos." 
        $ caramelos.agregarAlInvetario()
        hide spr guardia with dissolve
        Narrador "Un caramelo en el bolsillo, pero el sabor amargo perdura."
    $ cambio = 1
    return

    label .noDarCamara:
        Protagonista "No pienso darte algo que no es tuyo. No tenés derecho a exigirlo."
        Guardia "¿No entendés que esto es más grande que vos? Te conviene no hacerte el héroe."
        Alma_perdida "Mi... cámara...."
        Guardia "Escuchá, amigo, este tipo no es quien aparenta. Está en líos permanentemente. Robos, estafas, vos no tenés idea. No vale la pena arriesgarse por alguien así."
        Protagonista "¿Y vos, Guardia? ¿Qué te pasó para terminar así?"
        Guardia "¿Qué querés saber? Solía soñar con ser un buen policía, atrapar a los malos, ¿sabés? Pero la vida, amigo... te golpea tan fuerte que te saca las ganas de soñar."

    menu:
        "Todavía no es tarde":
            $ karma += 1
            Protagonista "Siempre hay una opción, una forma de cambiar las cosas."
            Guardia "¿Cambiar? ¿Acaso creen que es fácil cambiar cuando ya estás tan adentro?"
            Protagonista "No es fácil, pero es posible. A veces, las elecciones más difíciles son las más significativas."
            Guardia "Ustedes viven en un mundo idealista. No entienden lo que es la realidad."

        "Mirá en lo que te convertiste":
            $ karma -= 1
            Protagonista "Mirá en lo que te convertiste. Tu cinismo te ha transformó en lo que tanto despreciabas."
            Guardia "¿Qué sabés vos sobre mí? No tienes idea de lo que implica mi realidad."
            Protagonista "Aunque no entienda completamente tu situación, algo de bondad debe quedar en vos, buscando tu redención."
            Guardia "¿Redención? Estás perdiendo el tiempo. No hay redención para alguien como yo."
            #(Con gesto de resignación) 
            Protagonista "Todos merecen una oportunidad de hacer las cosas bien."
            Guardia "¿En serio me decís? ¿Incluso para alguien como yo?"
        
    Protagonista "La realidad puede ser dura, pero eso no impide que el cambio sea una posibilidad. Uno puede encontrar su camino, incluso en la oscuridad."
    Guardia "No sé si entienden... No pueden entender."
    #(Respira profundamente)
    Narrador "El guardia, visiblemente afectado por la conversación, muestra un atisbo de conflicto interno, pero tras un momento de silencio tenso, toma una decisión."
    Guardia "No sé si creerles. Pero... no vale la pena continuar así."
    #(Suspira)
    Narrador "El guardia, con gesto dubitativo, da media vuelta y se aleja, dejando una sensación de incertidumbre en el ambiente."
    Guardia "No sé si podré, pero... tal vez sea hora de intentarlo."
    hide spr guardia with dissolve
    Alma_perdida "Gracias..." 
    $ caramelos.agregarAlInvetario()
    $ cambio = 1
    return

label c0escena8:
    #SI SACAS FINAL MALO
    #NARRADOR: En un torbellino de emociones, te ves envuelto en un abismo de miedo y
    #desconcierto, sin poder discernir entre lo real y lo ilusorio.
    #SI SACAS FINAL BUENO
    #En un acto de incertidumbre redimida, con un suspiro de alivio, conseguiste disipar las sombras
    #de la desdicha, convenciendo al guardia de desistir de su infausta decisión
    $ cambio = 1
    return
    
label c0escena9:
    #show spr maquinista with dissolve
    #play music bgm_Cabina fadeout 1.0 fadein 1.0 loop volume 1
    #Protagonista "Che, necesito llegar a la próxima estacion para poder salir, me estas entendido, ¿no?"
    #Maquinista "D u l c e . . ."

    #menu:
    #    "Bueno, dale. Toma los caramelo, rarito":
    #        $ caramelos.sacarDelInvetario()
    #play audio sfx_Caramelos fadeout 1.0 fadein 1.0 volume 1

    #hide spr maquinista with dissolve
    
    
    
    #NARRADOR Te ves envuelto en una precipitada carrera, donde tus pasos resuenan en el vacío de
    #los pasillos, un eco de urgencia que domina tu ser. Tu mente, turbada por la reciente experiencia,
    #oscila entre la necesidad de escapar y el desconcierto que aún te embarga, un poso insondable
    #del abrumador encuentro
    
    
    
    $ cambio = 1
    return

label c0escena10:
    show spr maquinista with dissolve
    play music bgm_Cabina fadeout 1.0 fadein 1.0 loop volume 1
    
    Narrador "En la cabina del tren, el aire se densificaba con un aura de urgencia y tensión. El Maquinista, inexpresivo, repetía con monotonía una única súplica."
    Protagonista "¡Necesito respuestas! ¡Por favor, explicame qué está pasando!"
    Maquinista "Caramelos..."
    Protagonista "¡No tengo tiempo para esto! ¡Necesito saber qué está pasando!"
    Maquinista "Caramelos..."
    Protagonista "¡Espera! ¡Tengo algo!"
    Protagonista "¡Toma, toma esto!"
    
    $ caramelos.sacarDelInvetario()
    
    Maquinista "Caramelos..."
    hide spr maquinista with dissolve
    Narrador "En ese instante, las puertas se cierran y el tren comienza su trayecto, dejándote con un sentimiento de desconcierto y alivio a la vez"

    $ cambio = 1
    return

label BadEnding:
    scene black with fade_largo
    return

label ending:
    play music musica_final_del_cap fadeout 1.0 fadein 0.1 loop volume 1
    play sound sfx_Subte_Yendose fadeout 1.0 fadein 0.1 volume 1  
    scene bg subte_viaje with fade_largo  
    pause 5
    stop music
    stop sound
    scene bg continuara with fade_comun
    pause
    
    return