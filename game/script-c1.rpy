label c1vagon:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1cabina","","","c1cabina")
        pause
    
    jump expression destino

label c1cabina:
    $ destino = None
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1coneccion1","","c1anden1","c1tunel3")
        pause
    
    jump expression destino

label c1habitacion:
    $ destino = None
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1lobbyreloj","c1escalera3der","c1tuner3","c1escalera3izq")
        pause
    
    jump expression destino

label c1escalera3izq:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1segundocentroa","c1puestodiario","c1segundoderecha","")
        pause
    
    jump expression destino

label c1segundocentroa:
    $ destino = None
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
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
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","","")
        pause
    
    jump expression destino

label c1salaadministrativa:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","","")
        pause
    
    jump expression destino

label c1andenfrente2:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","","")
        pause
    
    jump expression destino

label c1salapersonal:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","","")
        pause
    
    jump expression destino

label c1pasajesecreto:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","","")
        pause
    
    jump expression destino

label c1salasuicidio:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","","")
        pause
    
    jump expression destino

label c1vias1:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","","")
        pause
    
    jump expression destino

label c1vias2:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("","","","")
        pause
    
    jump expression destino