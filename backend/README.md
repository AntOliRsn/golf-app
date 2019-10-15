# Backend Readme

## WIP

- dump_only in ma.SchemaModel not working !!!

## Remarks:

- All Models need ot be defined before importing Schemas !

## Swagger:
- Use APIspec marshmallow plugin 
- Create a method generate_spec to be used at the end of each route file 
- Create a APISPEC global congig variable defining parameters of the swagger
- Look at this example [https://github.com/flasgger/flasgger/blob/master/examples/apispec_example.py] for both advantage of apispec and flasgger

## TODO:
- use nested api instead of nested schemas 
- refactor app.py code 
- define a method to fill APIspec template in an automatic way