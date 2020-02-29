# enelvo-microservice

Microsserviço REST para normalização pt\_BR usando o
[Enelvo](https://github.com/tfcbertaglia/enelvo). Ideal para aplicações
que precisam de normalização online como chatbots.

## Geração interfaces

```sh
python3 -m pip install grpcio-tools
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. normalization.proto
```

## Requisitos

- Instalar Docker-CE 19.03+
- 900 MB de espaço em disco para imagem

## Execução

Rodar os comandos:

```sh
# gerar a imagem
sudo docker build -t staticdev/enelvo:1.0.0 .
# verificar se gerou
sudo docker images
# instanciar imagem
sudo docker run --name enelvo -d -p 50051:50051 staticdev/enelvo:1.0.0
# conferir processo rodando
sudo docker ps -a

# para parar o container olhe o nome dele no docker ps -a e execute
sudo docker stop enelvo
# para remover um container (precisa parar primeiro)
sudo docker rm enelvo
# para deletar a imagem
sudo docker rmi staticdev/enelvo:1.0.0
```

## Exemplos de uso

Foi criado um cliente gRPC de [exemplo](normalization_client.py).