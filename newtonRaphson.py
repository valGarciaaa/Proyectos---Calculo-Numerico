import math

def calcular_newton(f, df, d2f, x0, tol, max_iter):
    """
    Implementacion del Método de Newton-Raphson.
    Calcula la raiz de una función partiendo de un punto inicial x0.
    """
    # 1. Analisis del Criterio de Convergencia
    # Formula: | f(x0) * f''(x0) | / | f'(x0) |^2
    numerador = abs(f(x0) * d2f(x0))
    denominador = abs(df(x0))**2
    criterio = numerador / denominador
    
    print("--- Método de Newton-Raphson ---")
    print(f"Valor del criterio: {criterio:.4f}")
    print("-" * 55)

    # 2. Iteracion
    error_it = 1.0
    xi = x0
    i = 0

    print(f"{'i':<3} | {'Xi':<10} | {'Xi+1':<10} | {'Error Relativo':<15}")
    print("-" * 55)

    while (error_it > tol) and (i < max_iter):
        fi = f(xi)
        dfi = df(xi)
        
        if dfi == 0:
            print("Aviso: Derivada igual a cero. El método no puede continuar.")
            break
            
        xi_siguiente = xi - (fi / dfi)
        
        # Calculo del error relativo segun la formula
        error_it = abs((xi_siguiente - xi) / xi_siguiente)
        
        print(f"{i:<3} | {xi:<10.4f} | {xi_siguiente:<10.4f} | {error_it:<15.4f}")
        
        # Actualizacion de valores
        xi = xi_siguiente
        i += 1

    return xi, error_it

if __name__ == "__main__":
    # Definicion de la funcion: f(x) = e^x - 3x^2
    f = lambda x: math.exp(x) - 3*(x**2)
    df = lambda x: math.exp(x) - 6*x
    d2f = lambda x: math.exp(x) - 6
    
    # Parametros de entrada del ejercicio
    x0 = 0.5
    tolerancia = 0.02
    
    print("Realizado por: Valeria Garcia C.I: 31.649.272. Sección 0520")
    print("Cálculo Numérico I| 230-3154")
    raiz, error_f = calcular_newton(f, df, d2f, x0, tolerancia, 50)
    
    if raiz is not None:
        print("-" * 55)
        print(f"Resultado de la raiz (p): {raiz:.6f}")
        print(f"Comprobacion f(p): {f(raiz):.8f}")