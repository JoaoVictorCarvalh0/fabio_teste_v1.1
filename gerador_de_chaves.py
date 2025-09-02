from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

ARQ_PRIV = Path("chave_privada.pem")
ARQ_PUB  = Path("chave_publica.pem")

def gerar_novas_chaves(key_size: int = 2048) -> None:
    priv = rsa.generate_private_key(public_exponent=65537, key_size=key_size)

    with ARQ_PRIV.open("wb") as f:
        f.write(
            priv.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    with ARQ_PUB.open("wb") as f:
        f.write(
            priv.public_key().public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
        )

    print("✅ Chaves geradas e salvas (chave_privada.pem, chave_publica.pem).")

if __name__ == "__main__":
    gerar_novas_chaves()
