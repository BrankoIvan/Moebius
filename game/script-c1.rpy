label c1vagon:
    $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

    if escena in []:
        $ renpy.call("c1escena" + str(escena))
        $ escena += 1

    while destino == None:
        window hide
        show screen flechasDeNavegacion("c1cabina","","","")
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
        show screen flechasDeNavegacion("","","c1vagon","c1anden1")
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
        show screen flechasDeNavegacion("c1anden2","c1vagon","","c1tunel3")
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
        show screen flechasDeNavegacion("c1coneccion1","","","c1tunel4")
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
        show screen flechasDeNavegacion("lobby","","c1anden2","")
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

#label c1lobby:
   # $ destino = None
    #scene bg vagon with fade_comun
    #play music bgm_Te_Despertaste fadeout 1.0 fadein 1.0 loop volume 0.3

   # if escena in []:
    #    $ renpy.call("c1escena" + str(escena))
    #    $ escena += 1

   # while destino == None:
  #      window hide
  #      show screen flechasDeNavegacion("c1lobbyreloj","c1escalera3der","c1tuner3","c1escalera3izq")
  #      pause
    
   # jump expression destino


