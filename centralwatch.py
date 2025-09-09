# centralwatch.py - App CLI para registro de ocorrências de monitoramento 24h
# Autora: Juliana Santana

import csv, os
from datetime import datetime, date

ARQ_DIR = "dados"
ARQ_CSV = os.path.join(ARQ_DIR, "ocorrencias.csv")

TIPOS = ["ALARME", "CAMERA_OFFLINE", "INTRUSAO", "TESTE", "MANUTENCAO", "OUTROS"]
SEVERIDADES = ["BAIXA", "MEDIA", "ALTA", "CRITICA"]

def garantir_arquivo():
    os.makedirs(ARQ_DIR, exist_ok=True)
    if not os.path.exists(ARQ_CSV):
        with open(ARQ_CSV, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["timestamp","data","hora","cliente","local","tipo","severidade","descricao"])

def registrar():
    print("\n=== Registrar Ocorrência ===")
    cliente = input("Cliente: ")
    local = input("Local: ")
    tipo = input(f"Tipo {TIPOS}: ")
    severidade = input(f"Severidade {SEVERIDADES}: ")
    descricao = input("Descrição: ")
    agora = datetime.now()
    linha = [agora.isoformat(timespec="seconds"), agora.date(), agora.time().strftime("%H:%M:%S"),
             cliente, local, tipo, severidade, descricao]
    with open(ARQ_CSV, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(linha)
    print("✅ Ocorrência registrada!\n")

def listar():
    if not os.path.exists(ARQ_CSV):
        print("Nenhuma ocorrência registrada."); return
    with open(ARQ_CSV, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            print(f"[{row['data']} {row['hora']}] {row['cliente']} | {row['tipo']} | {row['severidade']} | {row['descricao']}")

def menu():
    garantir_arquivo()
    while True:
        print("\n=== CentralWatch ===")
        print("1) Registrar ocorrência")
        print("2) Listar ocorrências")
        print("3) Sair")
        op = input("Escolha: ")
        if op == "1": registrar()
        elif op == "2": listar()
        elif op == "3": break
        else: print("Opção inválida.")

if __name__ == "__main__":
    menu()
