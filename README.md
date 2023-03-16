# zakupy backend

## Application startup
You need to create an .env file in the application's root directory, at the same level as docker-compose.yml.  
Sample file contents:
```
POSTGRES_USER=ADMIN
POSTGRES_PASSWORD=SECRET_PASSWORD
POSTGRES_DB=zakupy
POSTGRES_URL=db

SECRET=strong_secret
```
