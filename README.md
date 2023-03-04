## Fastapi-Api-Movie
Esta es una API sencilla para gestionar una lista de películas. Fue construido usando FastAPI, una demo ha sido desplagada en Railway

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

## Demo
Puedes consultar los endpoints y jugar con ellos, en https://api-movie-deploy-production.up.railway.app/.
1. Vas a el endpoint **auth**  ingresas con el email: *admin@gmail.com* Despues la contraseña: *admin*
2. Luego copy and paste del jwt del output y te auntenticas
3. A probar