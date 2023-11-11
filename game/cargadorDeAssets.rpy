#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Rutas
define backgrounds = "images/bg/"
define backgroundse1 = "images/bg/c1/"
define extras = "images/interactuables/"
define sprites = "images/sprites/"
define movies = "images/bg/movies/"
define backgroundmusic = "audio/bgm/"
define sfx = "audio/sfx/"

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
image bg escalera_3_izq = backgroundse1 + "escalera_3_izq.jpg"
image bg lobby = backgroundse1 + "lobby.jpg"
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

image bg vagon = Movie(play= movies + "vagon.webm")
image bg anden_1 = Movie(play= movies + "anden_1.webm")
image bg despertar = Movie(play = movies + "despertar.webm")
image bg escalera = Movie(play = movies + "escalera.webm")

image bg opening_1 = Movie(play = movies + "opening_1.webm")
image bg opening_2 = Movie(play = movies + "opening_2.webm")
image bg opening_3 = Movie(play = movies + "opening_3.webm")
image bg opening_4 = Movie(play = movies + "opening_4.webm")
image bg ojos_cerrados = Movie(play = movies + "cerrar_ojos.webm")
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
# Audio

define audio.bgm_Estas_volviendo_a_casa = backgroundmusic + "Estás volviendo de una larga jornada.mp3"
define audio.bgm_Pasillo_largo = backgroundmusic + "Pasillo largo.mp3"
define audio.bgm_Al_salir = backgroundmusic + "Al salir del subte.mp3"
define audio.bgm_Entras_en_la_cabina = backgroundmusic + "Entras en la cabina del conductor.mp3"
define audio.bgm_Escaleras = backgroundmusic + "Escaleras.mp3"
define audio.bgm_Te_Despertaste = backgroundmusic + "Te despertaste.mp3"

define audio.bgm_Ambiente1 = backgroundmusic + "Ambiente 1.mp3"
define audio.bgm_Ambiente2 = backgroundmusic + "Ambiente 2.mp3"
define audio.bgm_Conductor = backgroundmusic + "Pista Conductor.mp3"

define audio.sfx_Panel_de_control = sfx + "Efecto-El panel de control se extiende.mp3"
define audio.sfx_Sepulcro = sfx + "Efecto-El subte es ahora tu sepulcro.mp3"
define audio.sfx_Cartel_vacio = sfx + "Efecto-La pared donde debería estar el cartel.mp3"
define audio.sfx_Puerta_se_abre = sfx + "Efecto-Puerta se abre antes de salir al andén.mp3"

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


