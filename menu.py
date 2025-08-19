# -*- coding: utf-8 -*-
import sys

from gerador_de_chaves import gerar_novas_chaves
from criptografar import executar_criptografia
from descriptografar import executar_descriptografia

def menu():
    while True:
        print("\n==============================")
        print("        MENU INTERATIVO       ")
        print("==============================")
        print("[1] Gerar novas chaves")
        print("[2] Criptografar uma mensagem")
        print("[3] Descriptografar a mensagem")
        print("[0] Sair")
        esc = input("Escolha uma opção: ").strip()

        if esc == "1":
            gerar_novas_chaves()
        elif esc == "2":
            executar_criptografia()
        elif esc == "3":
            executar_descriptografia()
        elif esc == "0":
            print("👋 Saindo...")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n👋 Interrompido pelo usuário.")
        sys.exit(130)
