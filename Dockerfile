FROM python:3.7.7-slim-buster as builder

ENV PATH="/root/.local/bin:/root/.poetry/bin:${PATH}"

COPY poetry.lock pyproject.toml ./

RUN apt-get update && apt-get install -y curl git \
 && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
 && git clone https://github.com/tfcbertaglia/enelvo.git enelvo-src \
 && cd enelvo-src \
 && poetry build

FROM python:3.7.7-slim-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.8

# set the working directory to /app
WORKDIR /app

COPY --from=builder poetry.lock pyproject.toml /enelvo-src/dist/enelvo*.whl /app/

RUN pip install "poetry==$POETRY_VERSION" \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev \
  && pip install enelvo*.whl \
  && rm -fr enelvo*.whl

# copy the current directory contents into the container at /app
COPY src/* /app/

EXPOSE 50051

# run app.py when the container launches
CMD ["python", "normalization_server.py"]
