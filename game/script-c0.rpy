#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Mapa

label vagon:
    $ destino = None
    scene bg vagon with fade_comun
    play music bgm_Vagon fadeout 1.0 fadein 1.0 loop volume 1

    if escena in [1,3]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("cabina","","","anden1" if escena > 2 else "")
        pause
    
    jump expression destino

label cabina:
    $ destino = None
    scene bg cabina with fade_comun
    play music bgm_Cabina fadeout 1.0 fadein 1.0 loop volume 1

    if escena in [2,9]:
        $ renpy.call("c0escena" + str(escena))
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
    play music bgm_Anden1 fadeout 1.0 fadein 1.0 loop volume 1

    if escena in [4]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += 1

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
        $ escena += 1
    
    while destino == None:
        window hide
        show screen flechasDeNavegacion("tunelCerrado","","anden1","")
        pause
    
    jump expression destino

label anden2:
    $ destino = None
    scene bg anden_2 with fade_comun
    play music bgm_Anden2 fadeout 1.0 fadein 1.0 loop volume 1
    
    if escena in [8]:
        $ renpy.call("c0escena" + str(escena))
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
    play music bgm_Anden2 fadeout 1.0 fadein 1.0 loop volume 1

    if escena in []:
        $ renpy.call("c0escena" + str(escena))
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
    play music bgm_Baño fadeout 1.0 fadein 1.0 loop volume 1
    
    if escena in []:
        $ renpy.call("c0escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        $ cigarrillos.mostrar()
        show screen flechasDeNavegacion("","","anden_fondo","")
        pause
    
    jump expression destino

label vias:
    scene black with fade_comun
    play music bgm_Vias fadeout 1.0 fadein 1.0 loop volume 1

    Protagonista "Esta muy oscuro, es peligroso."

    if escena in []:
        $ renpy.call("c0escena" + str(escena))
        $ escena += 1

    jump anden_fondo

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
        $ escena += 1
    
    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","tunel2","")
        pause
    
    jump expression destino

label tunel:
    $ destino = None
    scene bg tunel_1 with fade_comun
    play music bgm_Tunel1 fadeout 1.0 fadein 1.0 loop volume 1
    
    if escena in [5]:
        $ renpy.call("c0escena" + str(escena))
        $ escena += 1
    
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
        $ escena += 1

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
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","escalera","")
        pause
    
    jump expression destino

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Historia

label intro:
    scene bg cerrar_ojos with fade_comun
    play music bgm_Tren_Llegando fadeout 1.0 fadein 1.0 loop volume 2

    Narrador "Estás volviendo de una larga jornada laboral en el subte que habitualmente tomas..." 
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
    Narrador "Te estiras y bostezas, estirando los músculos rígidos después de un largo día."
    Narrador "Tu mirada, lenta y pesada, se posa en la única fuente de luz en la penumbra que te rodea..." 
    Narrador "Una puerta solitaria, iluminada en medio de la oscuridad."
        
    scene bg puerta_vagon_cerrada with fade_comun

    Narrador "La puerta está cerrada." 
    Narrador "Estás atrapado en el subte y no podés evitar sentir una oleada de ansiedad que recorre tu espina dorsal."

    scene bg vagon with fade_comun
    
    Protagonista "¡¿Hola? ¿Hay alguien ahí?¡Estoy atrapado en el subte!"
        
    return

label c0escena2:

    play music bgm_Cabina fadeout 1.0 fadein 1.0 loop volume 1
    Narrador "La cabina del maquinista se extiende frente tuyo, una maraña de controles y palancas en un espacio reducido"
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
            Protagonista "¿Qué significa esto? No entiendo para qué los querés…"
            pass

        "¿Caramelos? No tengo…":
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

    Protagonista "Parece que es lo único que puede pronunciar."     
    Protagonista "Como si fuera la única cosa que su mente es capaz de recordar."
    Protagonista "O la única que su alma pueda soportar decir..."  
            
    hide spr maquinista with dissolve
    #probar poner la puerta abriendo aca a ver si no aparece el minisalto?
    return

label c0escena3:
    scene bg puerta_abriendo with fade_comun
    play audio sfx_Puerta fadeout 1.0 fadein 1.0 volume 1

    Narrador "La puerta se abre."
    Protagonista "¿Será obra del maquinista o acaso una fuerza innombrable alteró esta escena?"

    scene bg vagon with fade_comun

    pass

    return

label c0escena4:
    #scene anden_1 
    play music bgm_Anden1 fadeout 1.0 fadein 1.0 loop volume 1
    Narrador "El andén del subte es un abismo sin fondo que se abre a la oscuridad."
    Narrador "Los viejos asientos de madera se alinean a lo largo del andén, vacíos y desgastados por el tiempo."
    Narrador "Las luces apenas iluminan los rincones proyectando extrañas sombras."
    Narrador "Un eco lejano de tus propios pasos es lo único que rompe el silencio en este lugar abandonado."
    
    return

label c0escena5:
    play music bgm_Tunel1 fadeout 1.0 fadein 1.0 loop volume 1
    Narrador "Algo se mueve en la oscuridad."
    Narrador "Una sombra espesa que desafía la lógica y la percepción humana."
    Narrador "Como si fuese una manifestación de un rincón olvidado de la realidad."
    Narrador "Una entidad pareciera aguardar paciente en el abismo entre el mundo conocido y lo desconocido."
    Narrador "La sensación de que alguien o algo te observa te eriza la piel."
    Narrador "Tu corazón late con fuerza y sentís un nudo en el estómago."

    return

label c0escena6:
    play music bgm_Puertas_Cerradas fadeout 1.0 fadein 1.0 loop volume 1
    Protagonista "¡La puta madre! ¿Y ahora cómo salgo?"
    Narrador "El aire pesado se adhiere a tus pulmones."
    Narrador "Se posan en esa puerta cerrada."
    Narrador "Un muro impenetrable que desafía tu libertad."

    return

label c0escena7:
    play music bgm_Escaleras fadeout 1.0 fadein 1.0 loop volume 1
    Narrador "Después de atravesar el oscuro pasillo, te encontrás al pie de las escaleras."
    Narrador "La presencia extraña que lo acecha se vuelve más intensa a medida que se acerca."
    
    
    show spr seguridad with dissolve
    play music musica_guardia fadeout 1.0 fadein 1.0 loop volume 1
    Narrador "De repente, un guardia deformado, apenas reconocible como humano, aparece en la oscuridad. Te mira con una ceja alzada."
    Guardia "¿Qué haces acá, pibe?"
    Protagonista " ¡La concha de la lora! Estoy re perdid... me quedé dormido en el subte y necesito salir"
    Protagonista "¿Entendés?"


    Guardia "Tranquilo, tranquilo. No podés salir por acá, tenés que ir a la siguiente estación."

    menu:
        "¡¿Qué?! ¡Si este era el último subte de la noche, no hay más!":
            Guardia "¿El último? Todavía no partió, estás a tiempo. Vení, el último subte te está esperando."
            Guardia "Por ahí los necesitas más que yo, pibe."
            play audio sfx_Caramelos fadeout 1.0 fadein 1.0 volume 1
            $ caramelos.agregarAlInvetario()
            Protagonista "Bueno. ¡Gracias!"
        
        "¿Y si me abris la puerta? Tengo algo que capaz te interese…" if cigarrillos.estaEnInventario:
            Guardia "¿Cigarrillos, decís?"
            Protagonista "Exacto, amigo. Y estos no son cualquier cosa, son de calidad."
            $ cigarrillos.sacarDelInvetario()
            Guardia "Bueno, pibe, parece que tenés buenos gustos. Pero sí, estos cigarrillos son codiciados por estos lares. Tomá."
            play audio sfx_Caramelos fadeout 1.0 fadein 1.0 volume 1
            $ caramelos.agregarAlInvetario()
            Protagonista "¿Un caramelo?"
            Guardia "Mirá, acá abajo, los caramelos son como moneda de cambio, y si necesitas moverte entre estaciones, vas a requerir varios."
            Guardia "El loco de la cabina solo te va a llevar a cambio de caramelos media hora, ni idea que le pasa."
            Protagonista "Gracias por todo loco, nos vemos."

        "¡No me vengas con boludeces! ¿Sabes que este era el último subte de la noche? ¿O necesitás un dibujo, pelotudo?":
            Guardia "Por ahí te hacen bien, amargo."
            play audio sfx_Caramelos fadeout 1.0 fadein 1.0 volume 1
            $ caramelos.agregarAlInvetario()
            Guardia "Cuidado con lo que decís, pibe."
            Guardia "En este ambiente no te hagas el vivo que te bajan enseguida."
    
    hide spr guardia with dissolve

    return

label c0escena8:
    play music bgm_Anden2 fadeout 1.0 fadein 1.0 loop volume 1
    Protagonista "Qué quilombo, che, el guardia tenía razón. El subte sigue parado acá. Es re raro pero..."
    Protagonista "Puede ser que los caramelos sean la posta para zafar."

    return
    
label c0escena9:
    show spr maquinista with dissolve
    play music bgm_Cabina fadeout 1.0 fadein 1.0 loop volume 1
    Protagonista "Che, necesito llegar a la próxima estacion para poder salir, me estas entendido, ¿no?"
    Maquinista "D u l c e . . ."

    menu:
        "Bueno, dale. Toma los caramelo, rarito":
            $ caramelos.sacarDelInvetario()
    play audio sfx_Caramelos fadeout 1.0 fadein 1.0 volume 1

    hide spr maquinista with dissolve

    return

label BadEnding:
    scene black with fade_largo
    return

label ending:
    scene bg subte_viaje with fade_largo
    play audio sfx_Subte_Yendose fadeout 1.0 fadein 1.0 volume 1
    play music musica_final_del_cap fadeout 1.0 fadein 1.0 loop volume 1
    pause 3
    
    return