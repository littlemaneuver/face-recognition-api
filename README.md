# face-recognition-api
Service for generating encodings from uploaded images

## Development
### Host machine requirements
1. `docker` and `docker-compose` are needed to run the application

### How to run
1. `./run start` should start containers
1. when containers are healty and running, run `./run initdb` to run initial migrations
1. new service will be available on `http://localhost:8000`

### How to test
1. containers should be running (started with `./run start`)
1. `./run test` will run api tests

## API endpoings
### GET `/encodings`
returns the list of all the previously uploaded face encodings

*Response*:
```js
[{ id: 1, encoding: [...]}, {id: 2, encoding: [...]}, ...]
```
### GET `/encodings/:id`
returns encoding by id

*Response*:
```js
{ id: 1, encoding: [...]}
```
### POST `/encodings`
generates encoding for the uploaded image (with face) and stores it

*Request*:
```js
    `Content-Type`: 'multipart/form-data'
    data: { file: imageBinary }
```

*Response*:
```js
{ id: 1, encoding: [...]}
```

### GET `/encodings/stats/count`
returns total count of processed (successfully, meaning those that contained faces) images

*Response*:
```js
    { count: 42 }
```

### GET `/encodings/stats/mean-encoding`
returns mean encoding for all the processed images

*Response*:
```js
    { mean_encoding: [...] }
```