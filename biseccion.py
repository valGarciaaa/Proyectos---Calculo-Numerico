import math

def biseccion_valeria(f, a, b, tol, max_iter):
    """
    Metodo de Biseccion - Proyecto Calculo Numerico
    Estudiante: Valeria Garcia
    """
    error_it = 1.0
    cont = 0
    m_ant = None
    
    # Verificacion inicial
    if f(a) * f(b) >= 0:
        print("[-] El intervalo no es valido para biseccion.")
        return None, None

    print(f"{'Iter':<5} | {'Punto Medio (m)':<15} | {'Error Relativo':<15}")
    print("-" * 45)

    while (error_it > tol) and (cont < max_iter):
        m_act = (a + b) / 2
        
        if m_ant is not None:
            error_it = abs((m_act - m_ant) / m_act)
        
        print(f"{cont+1:<5} | {m_act:<15.6f} | {error_it:<15.6f}")

        if f(a) * f(m_act) < 0:
            b = m_act
        else:
            a = m_act
            
        m_ant = m_act
        cont += 1
        
    return m_act, error_it

if __name__ == "__main__":
    # Datos f(x) = e^x - 3x^2
    func = lambda x: math.exp(x) - 3*(x**2)
    inf, sup = 0, 1
    cota_error = 0.04
    
    print("Realizado por: Valeria Garcia C.I: 31.649.272. Sección 0520")
    print("Cálculo Numérico I| 230-3154")
    print("--------Método de Bisección--------")
    res_raiz, res_error = biseccion_valeria(func, inf, sup, cota_error, 100)
    
    if res_raiz:
        print("-" * 45)
        print(f"Raiz aproximada: {res_raiz:.6f}")
        print(f"Error final: {res_error:.6f}")