import os
from readchar import readkey, key
from typing import List, Tuple

print("Mueve al personaje (↑ ↓ ← →): ")

def convertir_mapa_a_matriz(laberinto: str) -> List[List[str]]:
   return [list(fila) for fila in laberinto.split("\n")]


def mostrar_mapa(mapa: List[List[str]]):
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in mapa:
        print(''.join(fila))
 

def main_loop(mapa: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]):
    px, py = inicio
    mapa[px][py] = 'P'
    
    while (px, py) != final:
        mostrar_mapa(mapa)
        print(end='')
        movimiento = readkey()
        

        nueva_px, nueva_py = px, py
        if movimiento == key.UP: # Flecha arriba
            nueva_px -= 1
        elif movimiento == key.DOWN: # Flecha abajo
            nueva_px += 1
        elif movimiento == key.LEFT: # Flecha derecha
            nueva_py -= 1
        elif movimiento == key.RIGHT: # Flecha izquierda
            nueva_py += 1
            
        if 0 <= nueva_px < len(mapa) and 0 <= nueva_py < len(mapa[0]) and mapa[nueva_px][nueva_py] != '#':
        
            mapa[px][py] = '.'
            px, py = nueva_px, nueva_py
            mapa[px][py] = 'P'
 
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####   
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa_laberinto = convertir_mapa_a_matriz(laberinto)
inicio = (0, 0)
final = (len(mapa_laberinto) - 1, len(mapa_laberinto[0]) - 1)
main_loop(mapa_laberinto, inicio, final)