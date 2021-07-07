""" Programa para apoyar al marinero Seijo
    Almeiro Arango Avila
    Mayo 27-2021 """

import utilidades as util

def probar_funciones():
  criatura= util.aparecer_criatura()
  direccion=util.aparecer_direccion()
  print(criatura, direccion)

  if criatura == 'Kraken' or criatura == 'Hipocampo' or criatura == 'Pulpo':
    p = 'un'
    
  elif criatura == 'Sirenas' or criatura == 'Hidras':
    p = 'unas'

  elif criatura == 'Ballena' or criatura == 'Macaraprono':
    p = 'una'

  elif criatura == 'Leviatanes':
    p = 'unos'
  
  if direccion == 'babor' or direccion  == 'estribor':
    d = 'a'
    
  elif direccion == 'proa' or direccion  == 'popa':
    d = 'por la'

  print(f'Ahoy! capitán, {p} {criatura} {d} {direccion}')

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# Ejecuta el programa varias veces para ver su funcionamiento

probar_funciones()





