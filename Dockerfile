# syntax=docker/dockerfile:1

FROM ubuntu


RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.8 \
    python3-pip


#ENV VIRTUAL_ENV=venv
#RUN python3 -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install pandoc texlive-full

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

