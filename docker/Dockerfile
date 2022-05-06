FROM python:3
LABEL org.opencontainers.image.source=https://github.com/bpesics/pe-payment
ADD app/ /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
CMD flask run --host=0.0.0.0 --port=9000