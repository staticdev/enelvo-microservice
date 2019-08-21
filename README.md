# enelvo-microservice

Microsserviço REST para normalização pt\_BR usando o
[Enelvo](https://github.com/tfcbertaglia/enelvo). Ideal para aplicações
que precisam de normalização online como chatbots.

## Requisitos

- Instalar Docker-CE 18.03.1+
- 1.1 Gb de espaço em disco para imagem

## Execução

Rodar os comandos:

``` {.sourceCode .sh}
# gerar a imagem
sudo docker build -t staticdev/enelvo:0.9.2 .
# verificar se gerou
sudo docker images
# instanciar imagem
sudo docker run --name enelvo -d -p 5000:5000 staticdev/enelvo:0.9.2
# conferir processo rodando
sudo docker ps -a

# para parar o container olhe o nome dele no docker ps -a e execute
sudo docker stop enelvo
# para remover um container (precisa parar primeiro)
sudo docker rm enelvo
# para deletar a imagem
sudo docker rmi staticdev/enelvo:0.9.2
```

## Exemplos de uso

Basta fazer um POST da mensagem a ser normalizada na url /reply passando
a mensagem no campo "message".

A mensagem normalizada é retornada no campo "reply". O status da
requisição no campo "status", tendo com valor padrão para sucesso "ok".

Exemplo curl:

``` {.sourceCode .sh}
curl -X POST \
  http://localhost:5000/reply \
  -H 'content-type: application/json; charset=utf-8' \
  -d '{
    "message": "oi td bm?"
}'
```

Exemplo python3 nativo (http.client):

``` {.sourceCode .python}
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
