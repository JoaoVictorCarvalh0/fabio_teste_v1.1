# -*- coding: utf-8 -*-
from pathlib import Path
import base64

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

ARQ_PUB = Path("chave_publica.pem")
ARQ_MSG_TXT = Path("mensagem_criptografada.txt")  # texto (Base64)

def carregar_chave_publica(caminho: Path = ARQ_PUB):
    if not caminho.exists():
        raise FileNotFoundError("Chave pública não encontrada. Gere as chaves primeiro.")
    with caminho.open("rb") as f:
        return serialization.load_pem_public_key(f.read())

def criptografar(mensagem: str, pubkey) -> bytes:
    return pubkey.encrypt(
        mensagem.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def executar_criptografia(msg: str | None = None):
    pub = carregar_chave_publica()

    if msg is None:
        msg = input("Digite a mensagem a ser criptografada: ").strip()
    if not msg:
        print("⚠️ Mensagem vazia. Operação cancelada.")
        return 3

    cipher = criptografar(msg, pub)
    b64 = base64.b64encode(cipher).decode("utf-8")

    # salva em TXT (base64 em texto)
    with ARQ_MSG_TXT.open("w", encoding="utf-8") as f:
        f.write(b64)

    print("\n--- Resultado ---")
    print(f"Texto original:\n{msg}")
    print(f"\nTexto criptografado (bytes em Base64):\n{b64}")
    print(f"\n💾 Salvo em: {ARQ_MSG_TXT.resolve()}")
    return 0

if __name__ == "__main__":
    executar_criptografia()
