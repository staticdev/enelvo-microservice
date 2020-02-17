FROM python:3.7.6-slim-stretch

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && apt-get install -y git \
  && pip install -r requirements.txt \
  && git clone https://github.com/tfcbertaglia/enelvo.git enelvo-src \
  && cd enelvo-src \
  && python setup.py install \
  && cd .. \
  && mv enelvo-src/enelvo enelvo \
  && rm -fr enelvo-src

EXPOSE 50051

# run app.py when the container launches
CMD ["python", "app.py"]