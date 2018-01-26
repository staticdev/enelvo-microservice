FROM python:3.5.4-slim

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install git and build-essential
RUN apt-get update && \
    apt-get install -y git build-essential

# install requirements
RUN pip install -r requirements.txt

# download enelvo
RUN git clone https://github.com/carolcoimbra/enelvo.git temp

# install requirements
RUN cd temp && pip install --user -r requirements.txt
RUN cd temp && python setup.py install
RUN mv temp/enelvo enelvo

EXPOSE 5000

# run app.py when the container launches
CMD ["gunicorn", "app:APP", "-b", ":5000"]

