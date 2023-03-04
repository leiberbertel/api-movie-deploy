## Fastapi-Api-Movie
Esta es una API sencilla para gestionar una lista de películas. Fue construido usando FastAPI

## Corriendo la API

En primer lugar, clone el repositorio:
```
git clone https://github.com/example/api-movie-deploy.git
```

Después cree un **entorno virtual**
```
python3 -m venv venv
```
Activa el entorno virtual en linux
```
source venv/bin/activate
```
Activa el entorno virtual en Windows
```
source venv\Script\activate
```

## Endpoints

La API tiene los siguientes endpoints:

- GET /movie: Devuelve una lista de películas.
- POST /movies: Añade una nueva película a la lista.
- GET /movies/{id}: Devuelve una película concreta.
- PUT /movies/{id}: Actualiza una película concreta.
- DELETE /películas/{id}: Elimina una película concreta.

Todos los enpoints están documentados mediante OpenAPI. Puede consultar la documentación en http://localhost:0.0.0.0:8000/docs, que es el punto final predeterminado para la interfaz de usuario Swagger.
