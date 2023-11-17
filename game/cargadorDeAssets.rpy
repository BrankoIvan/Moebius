#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Rutas
define backgrounds = "images/bg/"
define backgroundse1 = "images/bg/c1/"
define extras = "images/interactuables/"
define sprites = "images/sprites/"
define movies = "images/bg/movies/"
define backgroundmusic = "audio/bgm/"
define sfx = "audio/sfx/"
define music = "audio/music/"

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Sprites

image spr seguridad:
    sprites + "NPC_SEGURIDAD.png"
    xzoom 1.0 yzoom 1.0
    xalign 0.5 yalign 1.9

image spr maquinista:
    sprites + "NPC_MAQUINISTA.png"
    xzoom 1.0 yzoom 1.0
    xalign 0.5 yalign 1.0

image spr guardia:
    #sprites + "guardia.png"
    xzoom 1.0 yzoom 1.0
    xalign 0.5 yalign 1.9




#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fondos Mapa

#e0
image bg cabina = backgrounds + "cabina.jpg"
image bg anden_2 = backgrounds + "anden_2.jpg"
image bg anden_fondo = backgrounds + "anden_fondo.jpg"
image bg tunel_1 = backgrounds + "tunel_1.jpg"
image bg tunel_2 = backgrounds + "tunel_2.jpg"
image bg baño = backgrounds + "baño.jpg"
image bg puerta_vagon_cerrada = backgrounds + "vagon_salida_cerrada.jpg"
image bg salida_cerrada = backgrounds + "salida_cerrada.jpg"
image bg oscuridad = backgrounds + "oscuridad.jpg"

#c1
image bg anden_frente_1 = backgroundse1 + "anden_frente_1.jpg"
image bg anden_frente_2 = backgroundse1 + "anden_frente_2.jpg"
image bg baño_2 = backgroundse1 + "baño_2.jpg"
image bg conexión_1 = backgroundse1 + "conexión_1.jpg"
image bg c1_anden_1 = backgroundse1 + "c1_anden_1.jpg"
image bg c1_anden_2 = backgroundse1 + "c1_anden_2.jpg"
image bg escalera_3_der = backgroundse1 + "escalera_3_der.jpg"
image bg escalera_3_izq = backgroundse1 + "lobby.jpg"
image bg lobby_reloj = backgroundse1 + "lobby_reloj.jpg"
image bg pasaje_secreto = backgroundse1 + "pasaje_secreto.jpg"
image bg puesto_diario = backgroundse1 + "puesto_diario.jpg"
image bg recepcion = backgroundse1 + "recepcion.jpg"
image bg sala_personal = backgroundse1 + "sala_personal.jpg"
image bg sala_suicidio = backgroundse1 + "sala_suicidio.jpg"
image bg salida_cerrada_2 = backgroundse1 + "salida_cerrada_2.jpg"
image bg segundo_centro_a = backgroundse1 + "segundo_centro_a.jpg"
image bg segundo_centro_b = backgroundse1 + "segundo_centro_b.jpg"
image bg segundo_derecha = backgroundse1 + "segundo_derecha.jpg"
image bg segundo_izquierda= backgroundse1 + "segundo_izquierda.jpg"
image bg tunel_3 = backgroundse1 + "tunel_3.jpg"
image bg habitacion = backgroundse1 + "habitacion.jpg"
image bg vias_1 = backgroundse1 + "vias_1.jpg"
image bg vias_2 = backgroundse1 + "vias_2.jpg"
image bg vias_3 = backgroundse1 + "vias_3.jpg"


# Fondos Animados

image bg sueño_2 = Movie(play= movies + "sueño_1.webm")
image bg sueño_1 = Movie(play= movies + "sueño_2.webm")
image bg vagon = Movie(play= movies + "vagon.webm")
image bg anden_1 = Movie(play= movies + "anden_1.webm")
image bg despertar = Movie(play = movies + "despertar.webm")
image bg escalera = Movie(play = movies + "escalera.webm")

image bg opening_1 = Movie(play = movies + "opening_1.webm")
image bg opening_2 = Movie(play = movies + "opening_2.webm")
image bg opening_3 = Movie(play = movies + "opening_3.webm")
image bg opening_4 = Movie(play = movies + "opening_4.webm")
image bg cerrar_ojos = Movie(play = movies + "cerrar_ojos.webm")
image bg sucumbir_oscuridad = Movie(play = movies + "sucumbir_oscuridad.webm")
image bg puerta_abriendo = Movie(play= movies + "puerta_abriendo.webm", loop=False, image= movies + "puerta_abriendo_fix.jpg")
image bg subte_viaje = Movie(play= movies + "subte_viaje.webm")

image vagon_interior = Movie(play= movies + "vagon_interior_1.webm")
image vagon_interior_2 = Movie(play= movies + "vagon_interior_2.webm")

image anden_1 = Movie(play= movies + "anden_1.webm")
image cartel_anden_1 = Movie(play= movies + "cartel_anden_1.webm")


image escalera_1 = Movie(play= movies + "escalera_1.webm")
image escalera_1a = Movie(play= movies + "escalera_1a.webm")
image escalera_1b = Movie(play= movies + "escalera_1b.webm")
image la_nada = Movie(play= movies + "la_nada.webm")
image mano_llave = Movie(play= movies + "mano_llave.webm")
image muerte_1 = Movie(play= movies + "muerte_1.webm")
image puerta_cerrada_1b = Movie(play= movies + "puerta_cerrada_1b.webm")


image bg good ending = Movie(play= movies + "el_fin.webm")

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Audio -Backgrounds

define audio.bgm_Anden1 = backgroundmusic + "Ambiente Andén 1.mp3"
define audio.bgm_Anden2 = backgroundmusic + "Ambiente Andén 2 y Andén fondo.mp3"
define audio.bgm_Baño = backgroundmusic + "Ambiente Baño.mp3"
define audio.bgm_Cabina = backgroundmusic + "Ambiente cabina.mp3"
define audio.bgm_Escaleras = backgroundmusic + "Ambiente Escaleras.mp3"
define audio.bgm_Puertas_Cerradas = backgroundmusic + "Ambiente Puertas cerradas (1 y 2).mp3"
define audio.bgm_Sucumbir_Oscuridad = backgroundmusic + "Ambiente sucumbir a la oscuridad.mp3"
define audio.bgm_Tunel1 = backgroundmusic + "Ambiente Túnel 1.mp3"
define audio.bgm_Tunel2 = backgroundmusic + "Ambiente Túnel 2.mp3"
define audio.bgm_Vagon = backgroundmusic + "Ambiente Vagón.mp3"
define audio.bgm_Vias = backgroundmusic + "Ambiente Vías.mp3"
define audio.bgm_Tren_Llegando = backgroundmusic + "Inicio-Tren llegando.mp3"

# Audio - Musica

define audio.musica_final_del_cap = music + "Música final del capítulo.mp3"
define audio.musica_guardia = music + "Música Guardia.mp3"
define audio.musica_maquinista = music + "Música Maquinista.mp3"

#Audio - Sonidos

define audio.sfx_Caramelos = sfx + "SFX Agarrar caramelos_ entregar caramelos.mp3"
define audio.sfx_Cigarillos = sfx + "SFX Agarrar Cigarrillos.mp3"
define audio.sfx_Cartel = sfx + "SFX Interacción Cartel.mp3"
define audio.sfx_Espejo = sfx + "SFX Interacción Espejo en baño.mp3"
define audio.sfx_Poster = sfx + "SFX Interacción Poster.mp3"
define audio.sfx_Puerta = sfx + "SFX La puerta del subte se abre.mp3"
define audio.sfx_Risa = sfx + "SFX Risa maníaca.mp3"
define audio.sfx_Subte_Frenando = sfx + "SFX Subte frenando.mp3"
define audio.sfx_Subte_Yendose = sfx + "SFX Subte yéndose.mp3"
define audio.sfx_Voces = sfx + "SFX Voces se desvanecen en el subte.mp3"

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Extras

define exCigarrillos = extras + "cigarrillos_%s.png"
define exCigarrillosCerca = extras + "cigarrillos_zoom.png"
define exCigarrillosInventario = extras + "cigarrillos_ui.png"

define exCartel = extras + "cartel_anden_%s.png"
define exCartelCerca = extras + "cartel_anden_zoom.png"

define exPoster = extras + "poster_%s.png"
define exPosterCerca = extras + "poster_zoom.png"

define exCaramelosInventario = extras + "caramelos_ui.png"


