# Recursividad111

#  Codigo

    fun factorial (n: int): int {
    if (n == O)
    {
      return 1
    }
    else
    {
        return n * factorial(n - 1)
    }
    fun main()
    {
      println(factorial(5))
    }

## ¿Que es un factorial en matematicas?
El factorial de un número es una operación matemática que se representa con un signo de exclamación (!) y que consiste en multiplicar ese número por todos los números enteros positivos menores que él.
Definición formal:
Para un número entero positivo 
𝑛
n, el factorial se denota como 
𝑛!
n! y se define así:
𝑛!=𝑛×(𝑛−1)×(𝑛−2)×⋯×3×2×1
n!=n×(n−1)×(n−2)×⋯×3×2×1
Y por definición:
0!=1

## ¿Para qué se usa?
El factorial se utiliza mucho en:
-Combinatoria (por ejemplo, para contar cuántas formas hay de ordenar objetos: 𝑛! n! es el número de permutaciones de  𝑛 n elementos).
-Probabilidades
-Series matemáticas
-Álgebra y análisis matemático

