## Overview
This is _very_ simple REST service implemented in *Python* with *Flask* for the [The Pleo SRE Challenge](https://github.com/pleo-io/tinjis#instructions)

## Local testing
`make deploy-local`

## Docker build and image publishing
Implemented as a GitHub workflow with [.github/workflows/docker-publish.yml](.github/workflows/docker-publish.yml)

Image available at: `ghcr.io/bpesics/pe-payment:latest`

## Available endpoints
* `/health`
  ```
  curl http://localhost:9000/health
  ```
* `/api/v1/charge` **POST**
  ```
  curl -XPOST -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" http://localhost:9000/api/v1/charge
  ```

## Logging
If a valid json document is `POST`-ed to `/api/v1/charge` the request payload is logged to `stdout`:

for instance:
```
INFO:app:json request => {'key1': 'value1', 'key2': 'value2'}
```

