#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Clases y Funciones

define voz_de_prota = ['audio/B1 Narrador_prota.mp3', 'audio/B2 Narrador_prota.mp3', 'audio/B3 Narrador_prota.mp3', 'audio/B4 Narrador_prota.mp3', 'audio/B5 Narrador_prota.mp3']
define voz_de_dario = ['audio/B1 Darío.mp3', 'audio/B2 Darío.mp3', 'audio/B3 Darío.mp3', 'audio/B4 Darío.mp3', 'audio/B5 Darío.mp3']
define voz_de_alma = ['audio/B1 Alma_perdida.mp3', 'audio/B2 Alma_perdida.mp3', 'audio/b3 Alma_perdida.mp3', 'audio/B4 Alma_perdida.mp3', 'audio/B5 Alma_perdida.mp3']
define voz_de_guardia = ['audio/A1 Guardia.mp3', 'audio/A2 Guardia.mp3', 'audio/A3 Guardia.mp3', 'audio/A4 Guardia.mp3']

init python:
    class Interactuable:
        def __init__( self, rutaParaBoton, unasCoordenadas, rutaParaVistaCercana, unLabel, unSonido):
            self.rutaDelBoton = rutaParaBoton
            self.posicion = unasCoordenadas
            self.rutaDeCerca = rutaParaVistaCercana
            self.descripcion = unLabel
            self.sfx = unSonido
        
        def mostrar( self ):
            renpy.show_screen( "interactuableScreen", self )
        
        def interactuar(self):
            renpy.sound.play(self.sfx)

    class Item( Interactuable ):
        inventario = []

        def __init__( self, rutaParaBoton, unasCoordenadas, rutaParaVistaCercana, unLabel, unSonido, rutaParaInventario ):
            super().__init__( rutaParaBoton, unasCoordenadas, rutaParaVistaCercana, unLabel, unSonido )
            
            self.rutaDelInvetario = rutaParaInventario
            self.estaEnInventario = False
            self.fueAgarrado = False

        def agregarAlInvetario( self ):
            self.fueAgarrado = True
            self.estaEnInventario = True
            self.inventario.append( self )
            
            self.actualizarInventario()
        
        def sacarDelInvetario( self ):
            self.fueAgarrado = True
            self.estaEnInventario = False
            self.inventario.remove( self )
            
            self.actualizarInventario()

        def actualizarInventario( self ):
            super().interactuar()
            renpy.hide_screen( "inventarioScreen" )
            renpy.show_screen( "inventarioScreen" )
        
        def mostrar( self ):
            if not self.fueAgarrado:
                super().mostrar()

    renpy.music.register_channel ("music2", mixer = "music", loop = True, stop_on_mute = True, tight = False, file_prefix = '', file_suffix = '', buffer_queue = True )

    def voz_prota(event, interact=True, **kwargs):
        if interact: voz(event, voz_de_prota)
        
        return
        
    def voz_guardia(event, interact=True, **kwargs):
        if interact: voz(event, voz_de_guardia)
        
        return

    def voz_alma(event, interact=True, **kwargs):
        if interact: voz(event, voz_de_alma)
        
        return

    def voz_dario(event, interact=True, **kwargs):
        if interact: voz(event, voz_de_dario)
        
        return

    
    def voz(event, lista_de_voces):
        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))
            renpy.sound.queue(renpy.random.choice(lista_de_voces))

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
    
    def crossfade (track_new, track_new_loop = None, fadeIn = 4.2, fadeOut = 4.2):
        primerCanal = "music"
        segundoCanal = "music2"
        
        do_loop = True

        if track_new_loop is not None:
            do_loop = False
        
        if not renpy.music.is_playing("music"):
            primerCanal = "music2"
            segundoCanal = "music"

        renpy.music.stop ( primerCanal, fadeout = fadeOut )

        renpy.music.play ( track_new, channel = segundoCanal, fadein = fadeIn, loop = do_loop )
        
        if not do_loop:
            renpy.music.queue ( track_new_loop, channel = segundoCanal, loop = True )

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Inventario, Items e Interactuables

screen inventarioScreen():
    vbox:
        align derecha, arriba
        
        add Null(0,20)
        
        hbox:
            align derecha, arriba
            box_reverse True
            for item in Item.inventario:
                add Null(20,20)
                add item.rutaDelInvetario

screen interactuableScreen( interactuable ):
    imagebutton:
        pos interactuable.posicion
        auto interactuable.rutaDelBoton action [Hide("interactuableScreen"),Call("pantallaDeCerca", interactuable)]
    
label pantallaDeCerca( interactuable ):
    $ interactuable.fueInteractuado = True
    play sound interactuable.sfx
    show screen interactuableDeCerca( interactuable.rutaDeCerca ) with Fade(0.25,0.0,0.25)    
    pause .5

    call expression interactuable.descripcion from _call_expression
    hide screen interactuableDeCerca
    return

screen interactuableDeCerca(unaRuta):
    add "#00000088"
    add unaRuta align centro, centro

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Navegacion

define centro = 0.5
define arriba = 0.02
define izquierda = 0.02
define derecha = 0.98
define abajo = 0.98

define flecha = "ui/flecha_%s.png"
define anchoFlecha = 50
define altoFlecha = 50
define flechaVacia = Null( anchoFlecha, altoFlecha )    

transform rotacion( grados ):
    rotate grados

screen flechasDeNavegacion( flechaArriba, flechaDerecha, flechaAbajo, flechaIzquierda ):

    if flechaArriba: 
        imagebutton:
            align centro, arriba
            focus_mask True
            auto flecha action [SetVariable("destino", flechaArriba), Call("hide_all")]
    else:
        add( flechaVacia )

    if flechaDerecha: 
        imagebutton:
            align derecha, centro
            focus_mask True
            auto flecha action [SetVariable("destino", flechaDerecha), Call("hide_all")] at rotacion(90)
    else:
        add( flechaVacia )

    if flechaAbajo: 
        imagebutton:
            align centro, abajo
            focus_mask True
            auto flecha action [SetVariable("destino", flechaAbajo), Call("hide_all")] at rotacion(180)
    else: 
        add( flechaVacia )  
     
    if flechaIzquierda: 
        imagebutton:
            align izquierda, centro
            focus_mask True
            auto flecha action [SetVariable("destino", flechaIzquierda), Call("hide_all")] at rotacion(270)
    else: 
        add( flechaVacia )

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Nombre De Habitacion

screen nombreDeHabitacion(unNombre):
    zorder 100

    frame at toggleShow:
        align izquierda, arriba
        xpadding 20
        ypadding 10
        text unNombre

    timer 1 action [Hide("nombreDeHabitacion")]

transform toggleShow:
    on show:
        alpha 0
        linear .1 alpha 1.0
    on hide:
        linear .1 alpha 0.0

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# 

label hide_all:
    hide screen interactuableScreen
    hide screen flechasDeNavegacion
    return