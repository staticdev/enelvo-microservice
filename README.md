# enelvo-microservice

Microsserviço REST para normalização pt_BR usando o [Enelvo](https://github.com/tfcbertaglia/enelvo). Ideal para aplicações que precisam de normalização online como chatbots.

## Requisitos

- Instalar Docker-CE 19.03+
- 550 MB de espaço em disco para imagem

## Geração interfaces

```sh
python3 -m pip install grpcio-tools
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/normalization.proto
```

## Execução

Rodar os comandos:

```sh
# gerar a imagem
sudo docker build -t staticdev/enelvo:0.9.4 .
# verificar se gerou
sudo docker images
# instanciar imagem
sudo docker run --name enelvo -d -p 50051:50051 staticdev/enelvo:0.9.4
# conferir processo rodando
sudo docker ps -a

# para parar o container olhe o nome dele no docker ps -a e execute
sudo docker stop enelvo
# para remover um container (precisa parar primeiro)
sudo docker rm enelvo
# para deletar a imagem
sudo docker rmi staticdev/enelvo:0.9.4
```

## Exemplo de uso

Foi criado um cliente gRPC de [exemplo](examples/normalization_client.py).
