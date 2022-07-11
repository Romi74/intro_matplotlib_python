# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos de "line_plot" de clase

    # Se desea graficar los valores de "x" e "y" en un gráfico de línea
    # A continuación los datos ya disponibles de "x" e "y" para que utilice:
    x = list(range(-10, 11, 1))

    # Bucle que completa y calcula todos los valores de "y"
    y = []
    for i in x:
        y.append(i**2)

    # Alumno: Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "y" en función de "x"

    fig = plt.figure()
    
    ax = fig.add_subplot()
    ax.plot(x,y, color = "r", marker = ".", label="y=x^2")
    fig.suptitle("Función exponencial\n\
    Y en funcion de X", fontsize=16, color = "b") #como se centran dos lineas de titulo?
    
    ax.set_xlabel("valores de X", color="b", fontsize= 11)
    ax.set_ylabel("Valores de Y", color="b", fontsize=11)
    ax.set_xlim([-10,11])
    ax.set_ylim([0, 100]) #como cambio tamaño de fuente, color, etc de ejes???
    ax.set_facecolor("g")
    ax.legend()
    ax.grid(ls="solid", color="b")
    
    # Alumno: Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección

    # Crear acá su gráfico
    plt.show(block=False)
print("terminamos") 
"""el grafico no tiene bello diseño, pero jugue con colores, tamaños de fuentes etc"""