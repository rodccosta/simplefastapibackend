# simplefastapibackend
Repositorio para compartilhar um backend fastapi simples integrado com um frontend fornecido pelo próprio fastapi.

# pré-requisito
- Um servidor mysql configurado e com permissões de acesso remoto para um usuário com acesso por senha.

# Como utilizar
Faça o clone do repositório, depois disso instale as dependencias através do comando pip install -r requirements.txt 
Apos isto, crie um arquivo .env na raiz do repositório contendo as seguintes informações

```sh
DB_USER= ...
DB_PASSWORD= ...
DB_HOST= ....
DB_NAME=....
DB_PORT=...
```

E depois é só executar python main.py
