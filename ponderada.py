import threading

class meuThread(threading.Thread):
    def __init__(self, lista, name):
        threading.Thread.__init__(self)
        self.lista = lista
        self.name = name
        self.resultado = 0

    def run(self):
        self.resultado = sum(self.lista)
        print(f"Thread {self.name} - soma parcial: {self.resultado}")

def dividir_lista(lista, n):
    tamanho_parte = len(lista) // n
    return [lista[i * tamanho_parte: (i + 1) * tamanho_parte] for i in range(n)]

if __name__ == "__main__":

    num_threads = 4
    tamanho_lista = 10000000

    lista_numeros = [i for i in range(tamanho_lista)]
    partes = list(dividir_lista(lista_numeros, num_threads))

    threads = []
    for i, parte in enumerate(partes):
        thread = meuThread(parte, i)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    soma_total = sum(thread.resultado for thread in threads)
    print(f"Soma total: {soma_total}")
