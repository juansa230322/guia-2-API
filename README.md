# API REST - Gestión de Productos

## Descripción
API REST desarrollada en Python utilizando FastAPI para administrar productos de una empresa.

## Tecnologías
- Python
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI

## Instalación
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución
```bash
uvicorn main:app --reload
```

Swagger UI:
http://127.0.0.1:8000/docs

## Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | /productos | Consultar todos los productos |
| GET | /productos/{id} | Consultar producto por ID |
| POST | /productos | Registrar producto |
| PUT | /productos/{id} | Actualizar producto |
| DELETE | /productos/{id} | Eliminar producto |

## Validaciones
- Nombre obligatorio.
- Precio mayor que cero.
- Stock no negativo.
- ID único.
- Productos inexistentes generan HTTP 404.

## Códigos HTTP
- 200 OK
- 201 Created
- 400 Bad Request
- 404 Not Found
- 422 Unprocessable Entity
