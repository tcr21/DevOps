# syntax=docker/dockerfile:1
FROM gitlab.informatik.uni-bremen.de:5005/hoeffner/pandoc-python-docker:latest
# docker image with exactly what we need: pandoc, python and latex

WORKDIR /app

#copy directory contents to docker
COPY . .

# set up the venv folder and set it as path for installs/launch
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# set character coding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#install requirements
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD flask run --host=0.0.0.0 --port=&PORT

