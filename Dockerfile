FROM python:3.7.6-slim-stretch as builder

RUN apt-get update && apt-get install -y git \
 && git clone https://github.com/tfcbertaglia/enelvo.git enelvo-src \
 && cd enelvo-src \
 && python setup.py bdist_wheel

FROM python:3.7.6-slim-stretch

# set the working directory to /app
WORKDIR /app

COPY --from=builder /enelvo-src/dist/Enelvo*.whl /app

# copy the current directory contents into the container at /app
COPY . /app

RUN pip install -r requirements.txt \
 && pip install Enelvo*.whl \
 && rm -fr Enelvo*.whl

EXPOSE 50051

# run app.py when the container launches
CMD ["python", "normalization_server.py"]
