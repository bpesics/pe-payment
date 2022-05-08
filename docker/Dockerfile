FROM python:3-slim as base

# assign image to repo
LABEL org.opencontainers.image.source=https://github.com/bpesics/pe-payment
COPY app/ /app
WORKDIR /app

FROM base as requirements
RUN pip install \
    --no-cache-dir \
    --prefix=/tmp/pip \
    -r requirements.txt

FROM base
COPY --from=requirements /tmp/pip /usr/local
EXPOSE 9000
CMD flask run --host=0.0.0.0 --port=9000