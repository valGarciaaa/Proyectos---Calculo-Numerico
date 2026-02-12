import math

def calcular_riemann_integral(f, a, b, n):
    """
    Metodo de Sumas de Riemann.
    Ejercicio de aproximacion de area para 4 particiones.
    """
    # 1. Calculo del ancho de los intervalos (h)
    h = (b - a) / n
    suma_total = 0

    print(f"---Integración numérica (Método de Riemann) (n = {n}) ---")
    print(f"Tamaño de Particiones (h) = {h}")
    print("-" * 45)

    # 2. Suma de Riemann (xi) 
    # La sumatoria va desde i = 0 hasta n-1
    for i in range(n):
        xi = a + i * h
        valor_f = f(xi)
        suma_total += valor_f
        print(f"x{i} = {xi:<6.2f} | f(x{i}) = {valor_f:<8.4f}")

    # 3. Resultado de la aproximacion
    area_aprox = h * suma_total
    return area_aprox

if __name__ == "__main__":
    # Identificacion
    print("Realizado por: Valeria Garcia C.I: 31.649.272. Sección 0520")
    print("Cálculo Numérico I| 230-3154")
    
    # Definicion de la funcion del ejercicio: f(x) = 3x * sqrt(x^2 + 1)
    funcion_ejercicio = lambda x: 3 * x * math.sqrt(x**2 + 1)
    
    # Parametros
    limite_a = 0
    limite_b = 1
    particiones = 4
    valor_real_cuaderno = 1.828  # Obtenido por sustitucion 
    
    # Ejecucion del calculo
    resultado_aprox = calcular_riemann_integral(funcion_ejercicio, limite_a, limite_b, particiones)
    
    # Calculo del Error Relativo
    error_rel = abs(valor_real_cuaderno - resultado_aprox) / valor_real_cuaderno
    
    print("-" * 45)
    print(f"Valor Aproximado: {resultado_aprox:.3f}")
    print(f"Valor Real (Sustitucion): {valor_real_cuaderno:.3f}")
    print(f"Error Relativo de la Aproximacion: {error_rel:.2f}")
    print("-" * 45)