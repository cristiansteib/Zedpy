import pilas

import escenas


pilas.iniciar(ancho=2751, alto=1306, titulo='Robot', centrado=False, pantalla_completa=False)

pilas.cambiar_escena(escenas.escena_usuarios.iniciar())

pilas.ejecutar()