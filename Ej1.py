import threading

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calcularPrimo():
    global primos
    primos = []
    for i in range (100):
        if(es_primo(i)):
            with lock:
                primos.append(i)


lock = threading.Lock()
hilos = []
for i in range (10):
    hilo = threading.Thread(target=calcularPrimo)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

resultado = sorted(primos)
print("Números primos del 1 al 100:", resultado)