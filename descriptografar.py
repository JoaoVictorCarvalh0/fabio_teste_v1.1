from pathlib import Path
import base64

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

ARQ_PRIV = Path("chave_privada.pem")
ARQ_MSG_TXT = Path("mensagem_criptografada.txt")  # texto (Base64)

def carregar_chave_privada(caminho: Path = ARQ_PRIV):
    if not caminho.exists():
        raise FileNotFoundError("Chave privada não encontrada. Gere as chaves primeiro.")
    with caminho.open("rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def descriptografar(cipher_bytes: bytes, privkey) -> str:
    plano = privkey.decrypt(
        cipher_bytes,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plano.decode("utf-8")

def executar_descriptografia():
    if not ARQ_MSG_TXT.exists():
        print("arquivo criptografado não encontrado")
        return 4

    priv = carregar_chave_privada()

    try:
        b64 = ARQ_MSG_TXT.read_text(encoding="utf-8").strip()
        if not b64:
            print("⚠️ Arquivo de mensagem está vazio.")
            return 5
        cipher = base64.b64decode(b64)
    except Exception as e:
        print(f"⚠️ Erro ao ler/decodificar {ARQ_MSG_TXT.name}: {e}")
        return 6

    try:
        texto = descriptografar(cipher, priv)
    except Exception as e:
        print(f"⚠️ Falha ao descriptografar. Verifique se a chave corresponde à mensagem. Detalhes: {e}")
        return 7

    print("\n--- Resultado ---")
    print("Texto descriptografado (igual ao original):")
    print(texto)
    return 0

if __name__ == "__main__":
    executar_descriptografia()
