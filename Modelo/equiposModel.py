from Conexion.conexionBD import ConexionDB 
class equipoModel:

    def buscarEquipos():
        query = "SELECT * FROM equipos"
        tipoConsulta = 2
        conexionBD = ConexionDB()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta)
        conexionBD.desconectar()
        return resultado
    
    def buscarEquipo(id):
        query = "SELECT * FROM equipos WHERE id_equipo = %s"
        parametros = id,
        tipoConsulta = 2
        conexionBD = ConexionDB()
        conexionBD.conectar()
        resultado = conexionBD.consultaDB(query, tipoConsulta, parametros)
        conexionBD.desconectar()
        return resultado
    
    def crearEquipo(tipo_equipo, nombre_equipo, estado_equipo, descripcion_equipo):
        query = "INSERT INTO equipos (tipo_equipo, nombre_equipo, estado_equipo, descripcion_equipo) VALUES (%s,%s,%s,%s)"
        tipoConsulta = 1
        parametros = tipo_equipo, nombre_equipo, estado_equipo, descripcion_equipo
        conexionBD = ConexionDB()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha insertado Correctamente")
        except:
            print("Ha ocurrido un problema en la inserción")
        conexionBD.desconectar()
    
    def editarEquipo(nombreEquipo, id):
        query = "UPDATE equipos SET nombre_equipo = %s WHERE id_equipo = %s;"
        tipoConsulta = 1
        parametros = nombreEquipo, id,
        conexionBD = ConexionDB()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha Editado Correctamente")
        except:
            print("Ha ocurrido un problema en la edición")
        conexionBD.desconectar()

    def eliminarequipo(id):
        query = "DELETE FROM equipos WHERE id_equipo = %s;"
        tipoConsulta = 1
        parametros = id,
        conexionBD = ConexionDB()
        conexionBD.conectar()
        try:
            conexionBD.consultaDB(query, tipoConsulta, parametros)
            print("Se ha Eliminado Correctamente")
        except:
            print("Ha ocurrido un problema en la Eliminación")
        conexionBD.desconectar()
