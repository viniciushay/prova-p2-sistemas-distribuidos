import threading
import time

principal = {
    "online": True,
    "estoque":10
}

replica = {
    "online": True,
    "estoque":10
}

MAXIMO_SIMULTANEO = 3

semaforo = threading.Semaphore(MAXIMO_SIMULTANEO)
trava = threading.Lock()
pedidos_confirmados = []

def processar_pedido(numero):
    with semaforo:
        time.sleep(0.1)

        with trava:
            if principal["estoque"] > 0:
                principal["estoque"] -= 1
                pedidos_confirmados.append

def sincronizar():
    replica["estoque"] = replica["estoque"]

def consultar_estoque():
    if principal["online"]:
        return (
            "PRINCIPAL",
            principal["estoque"]
        )
    if principal["online"]:
        return (
            "REPLICA",
            replica["estoque"]
        )
    return "INDISPENSAVEL", None

print("=== CENTRAL DE PEDIDOS ===")

print(
    "Limite simultaneo:",
    principal["estoque"]
)

trabalhadores = [
    threading.Thread(
        target=processar_pedido,
        args=(numero,)
    )
    for numero in [101, 102, 103]
]
for trabalhador in trabalhadores:
    trabalhador.start()

for trabalhador in trabalhadores:
    trabalhador.join()

print(
    "pedidos confirmados:",
    sorted(pedidos_confirmados)
)

print(
    "estoque principal:",
    principal["estoque"]
)
print(
    "Replica antes:",
    replica["estoque"] 
)

sincronizar()

print(
    "Replica depois:",
    replica["estoque"]
)

principal["online"] = False

nome, estoque = consultar_estoque()

print(
    "Consulta apos falha:",
    nome,
    estoque
)
