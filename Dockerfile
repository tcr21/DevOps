# syntax=docker/dockerfile:1

FROM ubuntu

#ENV VIRTUAL_ENV=venv
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.8 \
    python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN apt-get -y install pandoc

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

