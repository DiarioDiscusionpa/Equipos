from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from Modelo.equiposModel import equipoModel
from Controlador.equiposController import equipos

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)


#pueblos

@app.get('/api/equipos')
def buscarEquipo():
    equipo = equipos.buscarequipos()
    return equipo

@app.get('/api/equipo/{id}')
def buscarEquipo(id):
    equipoBuscado = equipos.buscarEquipo(id)
    return equipoBuscado

@app.post('/api/equipo/')
async def crearEquipo(request: Request):
    datos = await request.json()
    tipo = str(datos['tipo_equipo'])
    nombre = str(datos['nombre_equipo'])
    estado = str(datos['estado_equipo'])
    descripcion = str(datos['descripcion_equipo'])
    print(tipo, nombre, estado, descripcion)
    print(equipoModel.crearEquipo(tipo, nombre, estado, descripcion))
    return datos

@app.put('/api/equipo/{id}')
async def editarEquipo(request: Request):
    datos = await request.json()
    nombre = str(datos['nombre'])
    _id = int(datos['id'])
    print(equipoModel.editarEquipo(nombre, _id))
    return datos

@app.delete('/api/equipo/{id}')
async def eliminarequipo(request: Request):
    datos = await request.json()
    _id = int(datos['id'])
    print(equipoModel.eliminarequipo(_id))
