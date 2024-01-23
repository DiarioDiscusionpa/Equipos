from Modelo.equiposModel import equipoModel
class equipos: 


    def buscarequipos():
        datos = equipoModel.buscarEquipos()
        Equipos = []
        for equipo in datos:
            equipo = {
                "id": equipo[0],
                "tipo_equipo":equipo[1],
                "nombre_equipo": equipo[2],
                "estado_equipo":equipo[3],
                "descripcion_equipo":equipo[4]
            }
            Equipos.append(equipo)
        return Equipos
    
    def buscarEquipo(id):
        equipoBuscado = {}
        infoEquipo = equipoModel.buscarEquipo(id)
        for info in infoEquipo:
            equipoBuscado = {
                "id": info[0],
                "tipo_equipo": info[1],
                "nombre_equipo": info[2],
                "estado_equipo":info[3],
                "descripcion_equipo":info[4]
            }
        return equipoBuscado
