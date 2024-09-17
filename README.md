# Chatroom em Python
Este é um projeto de chatroom cliente-servidor desenvolvido em Python, utilizando sockets para comunicação em rede. Ele permite que múltiplos usuários se conectem e troquem mensagens em tempo real.

## Funcionalidades
-   **Comunicação em tempo real** entre múltiplos clientes
-   **Identificação dos usuários** via apelidos (nicknames)
-   **Broadcast de mensagens** para todos os clientes conectados
-   **Notificações de entrada e saída** de usuários no chat

## Como executar
### Servidor
1. Para iniciar o servidor, execute o arquivo `server.py`:
```bash
python server.py
```
O servidor será iniciado e ficará escutando na porta 7976 por padrão.

### Cliente
1. Execute o arquivo `client.py`:
```bash
python client.py
```
2. Insira um nickname quando solicitado.
3. Comece a enviar e receber mensagens no chat!

## Estrutura do Projeto
- `server.py`: Contém a lógica do servidor, que gerencia as conexões e o envio/recebimento de mensagens.
- `client.py`: Implementa o cliente que se conecta ao servidor para enviar e receber mensagens.

## Configurações
- A porta padrão usada para a comunicação é 7976, configurável nos arquivos server.py e client.py.
