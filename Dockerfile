FROM python:3.8.3-slim-buster as builder

ENV PATH="/root/.local/bin:/root/.poetry/bin:${PATH}"

RUN apt-get update && apt-get install -y curl git \
 && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
 && git clone https://github.com/tfcbertaglia/enelvo.git enelvo-src \
 && cd enelvo-src \
 && poetry build

FROM python:3.8.3-slim-buster

# set the working directory to /app
WORKDIR /app

COPY --from=builder /enelvo-src/dist/enelvo*.whl /app

# copy the current directory contents into the container at /app
COPY . /app

RUN pip install -r requirements.txt \
 && pip install enelvo*.whl \
 && rm -fr enelvo*.whl

EXPOSE 50051

# run app.py when the container launches
CMD ["python", "normalization_server.py"]
