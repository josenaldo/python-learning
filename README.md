INSTALAÇÃO DO AMBIENTE

Instalar o Docker - https://www.docker.com/products/docker-desktop

Instale o VS CODE - https://code.visualstudio.com/

CONSTRUIR CONTAINER
 – Executar, no terminal, o comando pra construir o container

docker build -t python-sandbox .

EXECUTAR CONTAINER

Verificar a pasta onde o arquivo Dockerfile está. O caminho dessa pasta deve ser configurado no comando docker run, no lugar de CAMINHO_DA_PASTA_HOST

docker run -it -d -v CAMINHO_DA_PASTA_HOST:/home/teste --name python-sandbox python-sandbox

Exemplo: 

O projeto está na pasta "D:\projetos\python-learning"

O comando a ser executado será 

docker run -it -d -v D:\projetos\python-learning:/home/teste --name python-sandbox python-sandbox

Executar, no terminal, o comando pra rodar o container


