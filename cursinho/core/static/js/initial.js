function insertFamiliar_comment(comment_id) {
    //coloque sua url que leva a view de inserir contactos
    var insert_contact_url = "/url/insert_contact/";
    // var contact_data = new FormData();
    var contact_data = new FormData($('#form_id'));

    var name = $('#name_input').val();
    var parente = $('#parente_input').val();
    var esc = $('#esc_input').val();
    var salario = $('#salario_input').val();
    // var person = $('#person').val()

    //cheque a documentação de como passar o CSRF Token no ajax
    contact_data.append('csrfmiddlewaretoken', csrftoken);
    //Aqui será adcionado os dados que será eviado no POST
    contact_data.append('name', name);
    contact_data.append('parente', parente);
    contact_data.append('esc', esc);
    contact_data.append('salario', salario);
    // contact_data.append('person', person);
    $.ajax({
      url: insert_contact_url,
      type: 'POST',
      data: contact_data,
      processData: false,
      contentType: false,
      success: function(data){
          alert('Contato adicionado com sucesso');
      }
    });
}
