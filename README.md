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

- Instalar Docker-CE 18.03.1+
- 1.1 Gb de espaço em disco para imagem

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

Basta fazer um POST da mensagem a ser normalizada na url /reply passando
a mensagem no campo "message".

A mensagem normalizada é retornada no campo "reply". O status da
requisição no campo "status", tendo com valor padrão para sucesso "ok".

Exemplo curl:

```sh
curl -X POST \
  http://localhost:5000/reply \
  -H 'content-type: application/json; charset=utf-8' \
  -d '{
    "message": "oi td bm?"
}'
```

Exemplo python3 nativo (http.client):

```python
import http.client

conn = http.client.HTTPConnection("localhost:5000")

payload = "{\"message\": \"oi td bm?\"}"

headers = {
    'content-type': "application/json; charset=utf-8"
}

conn.request("POST", "/reply", payload, headers)
res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
```
