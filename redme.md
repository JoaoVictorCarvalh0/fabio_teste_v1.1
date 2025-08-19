Criptografia RSA – Menu + Scripts Separados

Projeto didático que gera chaves, criptografa e descriptografa mensagens com RSA (OAEP + SHA‑256), usando quatro scripts separados:

gerador_de_chaves.py
criptografar.py
descriptografar.py
menu.py (orquestra tudo por um menu interativo)


🧱 Pré‑requisitos
Python 3.10+ (recomendado 3.12)
Pacote cryptography:
    pip install cryptography

📂 Estrutura esperada:
    .
    ├─ gerador_de_chaves.py
    ├─ criptografar.py
    ├─ descriptografar.py
    ├─ menu.py
    ├─ chave_publica.pem           # gerado pelo script
    ├─ chave_privada.pem           # gerado pelo script
    └─ mensagem_criptografada.txt  # salvo ao criptografar

▶️ Uso rápido

1) Rodar o menu:
    python menu.py

2) Opções do menu:

[1] Gerar novas chaves: Gera um par de chaves RSA (pública e privada) e as salva nos arquivos chave_publica.pem e chave_privada.pem.
[2] Criptografar uma mensagem: Solicita uma mensagem do usuário, criptografa usando a chave pública e salva o resultado no arquivo mensagem_criptografada.txt.
[3] Descriptografar a mensagem: Lê o arquivo mensagem_criptografada.txt, descriptografa usando a chave privada e exibe o texto original.
[0] Sair: Encerra o programa.

⚠️ Observações
    Certifique-se de gerar as chaves antes de tentar criptografar ou descriptografar mensagens.
    O arquivo mensagem_criptografada.txt será sobrescrito a cada nova criptografia.
    A chave privada deve ser mantida em segurança, pois é necessária para descriptografar as mensagens.
    
🛠️ Tecnologias Utilizadas
    Python: Linguagem de programação principal.
    Cryptography: Biblioteca para operações criptográficas.

📜 Licença
    Este projeto é de uso didático e não possui uma licença específica. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário.