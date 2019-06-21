FROM python:3.7.3-alpine

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

RUN apk add --no-cache --virtual .build-deps \
            gcc \
            g++ \
            musl-dev \
            git \
            gfortran \
            openblas-dev \
  && pip install -r requirements.txt \
  && git clone --branch v0.9.0 https://github.com/tfcbertaglia/enelvo.git enelvo-src-0.9.0 \
  && cd enelvo-src-0.9.0 \
  && python setup.py install \
  && apk del .build-deps \
  && cd .. \
  && mv enelvo-src-0.9.0/enelvo enelvo \
  && rm -fr enelvo-src-0.9.0 \
  && apk add --no-cache libstdc++ \
             openblas-dev

EXPOSE 5000

# run app.py when the container launches
CMD ["gunicorn", "__init__:create_app()", "-b", ":5000"]
