label c1vagon:
    $ destino = None
    scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1cabina","","","c1anden1")
        pause
    
    jump expression destino

label c1cabina:
    $ destino = None
    scene bg cabina with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1vagon","")
        pause
    
    jump expression destino

label c1anden1:
    $ destino = None
    scene bg c1_anden_1 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1anden2","c1vagon","","c1habitacion")
        pause
    
    jump expression destino

label c1anden2:
    $ destino = None
    scene bg c1_anden_2 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1conexion1","","c1anden1","c1tunel3")
        pause
    
    jump expression destino

label c1habitacion:
    $ destino = None
    scene bg habitacion with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1anden1","")
        pause
    
    jump expression destino

label c1tunel3:
    $ destino = None
    scene bg tunel_3 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1lobby","","c1anden2","")
        pause
    
    jump expression destino

label c1lobby:
    $ destino = None
    scene bg lobby with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1lobbyreloj","c1escalera3der","c1tunel3","c1escalera3izq")
        pause
    
    jump expression destino

label c1escalera3izq:
    $ destino = None
<<<<<<< HEAD
    scene bg vagon with fade_comun
    play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3
=======
    scene bg escalera_3_izq with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3
>>>>>>> 9e76e5912a786479dd0170b7565b43175211ef34

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1segundoizquierda","","c1lobby","")
        pause
    
    jump expression destino

label c1segundoizquierda:
    $ destino = None
    scene bg segundo_izquierda with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1escalera3izq","")
        pause
    
    jump expression destino


label c1escalera3der:
    $ destino = None
    scene bg escalera_3_der with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1segundoderecha","","c1lobby","")
        pause
    
    jump expression destino

label c1segundoderecha:
    $ destino = None
    scene bg segundo_derecha with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1segundocentrob","c1recepcion","","c1escalera3der")
        pause
    
    jump expression destino

label c1recepcion:
    $ destino = None
    scene bg recepcion with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1segundoderecha","")
        pause
    
    jump expression destino

label c1segundocentrob:
    $ destino = None
    scene bg segundo_centro_b with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1segundocentroa","c1puestodiario","","c1segundoderecha")
        pause
    
    jump expression destino

label c1segundocentroa:
    $ destino = None
    scene bg segundo_centro_a with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","c1salidacerrada2","c1segundocentrob","")
        pause
    
    jump expression destino

label c1salidacerrada2:
    $ destino = None
    scene bg salida_cerrada_2 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1segundocentroa","")
        pause
    
    jump expression destino

label c1puestodiario:
    $ destino = None
    scene bg puesto_diario with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1segundocentrob","")
        pause
    
    jump expression destino

label c1lobbyreloj:
    $ destino = None
    scene bg lobby_reloj with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1lobby","")
        pause
    
    jump expression destino

label c1conexion1:
    $ destino = None
    scene bg conexión_1 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","c1andenfrente1","c1anden2","")
        pause
    
    jump expression destino

### A PARTIR DE ACA FALTA LA NAVEGACIÓN

label c1andenfrente1:
    $ destino = None
    scene bg anden_frente_1 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1andenfrente2","","c1conexion1","c1salaadministrativa")
        pause
    
    jump expression destino

label c1salaadministrativa:
    $ destino = None
    scene bg baño_2 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1andenfrente1","")
        pause
    
    jump expression destino

label c1andenfrente2:
    $ destino = None
    scene bg anden_frente_2 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","c1vias1","c1andenfrente1","c1salapersonal")
        pause
    
    jump expression destino

label c1salapersonal:
    $ destino = None
    scene bg sala_personal with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1pasajesecreto","","c1andenfrente2","")
        pause
    
    jump expression destino

label c1pasajesecreto:
    $ destino = None
    scene bg pasaje_secreto with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1salasuicidio","","c1salapersonal","")
        pause
    
    jump expression destino

label c1salasuicidio:
    $ destino = None
    scene bg sala_suicidio with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1pasajesecreto","")
        pause
    
    jump expression destino

label c1vias1:
    $ destino = None
    scene bg vias_1 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1vias2","c1andenfrente2","","")
        pause
    
    jump expression destino

label c1vias2:
    $ destino = None
    scene bg vias_2 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1vias3","","c1vias1","")
        pause
    
    jump expression destino

label c1vias3:
    $ destino = None
    scene bg vias_3 with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","c1vias2","")
        pause
    
    jump expression destino