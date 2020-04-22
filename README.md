### Sistema encuetas

## Cómo usar:

1. Dirigirse al  [Survey Creator de survey.js](https://surveyjs.io/create-survey), crear la encuesta que desee con esta herramienta.

2. Al finalizarla dirigirse a la pestaña `JSON editor` y copiar el JSON Generado

3. Pegar el JSON en la variable data del archivo **/app/static/json.js**

4. Levantar los container de docker
```bash
docker-compose up -d
```

#Una vez realizados estos pasos podra ver los servicios corriendo:

###[Encuesta](localhost:8080)

###[Administracion de base de datos](localhost:8081)