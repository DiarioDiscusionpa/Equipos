
$.ajax({
    url:"http://127.0.0.1:8000/api/equipos",
    type: "GET",
    contentType: "application/json ; charset=utf8",
    dataType:"json",
    success: function(response){
      var tabla = $('#myTable > tbody:last-child')
  
      console.log(response)
  
      response.forEach(equipos => {
        var id_equipo = equipos.id_equipo;
        var tipo_equipo = equipos.tipo_equipo;
        var nombre_equipo = equipos.nombre_equipo;
        var estado_equipo = equipos.estado_equipo;
        var descripcion_equipo = equipos.descripcion_equipo;
        var fila = '<tr class="fila">' + '<td class="id">' + id_equipo + '</td>' + '<td>' + tipo_equipo + '</td>' + '<td>' + nombre_equipo + '</td>' + '<td>' + estado_equipo + '</td>' + '<td>' + descripcion_equipo + '</td>'
      })
    }
  })
  
  function btnVer(){
    var button = event.target
    var row = button.closest('tr')
    var idElement = row.querySelector('.id')
    var id = idElement.textContent;
  
    
    $.ajax({
      url: `http://127.0.0.1:8000/api/equipo/${id}`,
      type: "GET",
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      success: (response) => {
        console.log(response)
        $('#tituloModal').html(response.nombre_equipo);
        $('#contenidoModal').html(`Tipo: ${response.tipo_equipo}\n <br> Nombre:  ${response.nombre_equipo}\n <br> Estado: ${response.estado_equipo}\n <br> Descripcion: ${response.descripcion_equipo}`);
        $('#exampleModal').modal('show');
      }
    });
  }
  
  function btnBorrar(){
    var button = event.target
    var row = button.closest('tr')
    var idElement = row.querySelector('.id')
    var id = idElement.textContent;
  
    var datos = {
      "id":id
    }
    
    $.ajax({
      url: `http://127.0.0.1:8000/api/equipo/${id}`,
      type: "DELETE",
      data: JSON.stringify(datos),
      contentType: "application/json ; charset=utf8",
      dataType: "json",
      success: (response) => {
        location.reload()
      }
    });
  }
  
  function btnEditarModal(){
    var button = event.target
    var row = button.closest('tr')
    var idElement = row.querySelector('.id')
    var id = idElement.textContent;
    $('#modalEditar').modal('show')
    $('#editarBtn').click(() => {
      var nombre = $('#nombreValEd').val()
      var datos = {
        "id":id,
        "nombre":nombre
      }
  
      $.ajax({
        url: `http://127.0.0.1:8000/api/equipo/${id}`,
        type: "PUT",
        contentType: "application/json ; charset=utf8",
        dataType: "json",
        data: JSON.stringify(datos),
        success: (response) => {
          $('#exampleModal').modal('show');
          location.reload()
        }
      });
    })
  }
  
  
  $('#crearBtn').click(() => {
    var tipo_equipo = $('#tipo_equipoVal').val()
    var nombre_equipo = $('#nombre_equipoVal').val()
    var estado_equipo = $('#estado_equipoVal').val()
    var descripcion_equipo = $('#descripcion_equipoVal').val()
    
    var datos = {
      "tipo_equipo": tipo_equipo,
      "nombre_equipo": nombre_equipo,
      "estado_equipo":  estado_equipo,
      "descripcion_equipo": descripcion_equipo
    }
  
    $.ajax({
      url:"http://127.0.0.1:8000/api/equipo/",
      type:"POST",
      contentType:"application/json ; charset=utf8",
      data: JSON.stringify(datos) ,
      success: function(response){
        location.reload()
      }
    })
  })
  
 