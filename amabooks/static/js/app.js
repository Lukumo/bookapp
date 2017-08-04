$(document).ready(function () {
  // Submit category form
  $('#save_button').on('click', function(event){
    event.preventDefault()
    $.post('/amabooks/upload/',
      $('#uploadForm').serialize(),
      function(data){
        $('myModal').modal('hide');
        console.log(data);
        // location.reload();
      }
    )

  });
});
