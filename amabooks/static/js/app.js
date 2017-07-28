<<<<<<< HEAD
$(document).ready( function(){
  $('#savebtn').on('click', function(e){
    e.preventDefault()
    $.post('/todo/category/new/',
        $('#category').serialize(),
        function(data,status){
          $('#myModal').modal('hide');
        location.reload();

        }
    );
  });
}
=======
// $(document).ready(function () {
//   // Submit category form
//   $('#id="myModal"').on('click', function(event){
//     event.preventDefault()
//     $.post('//category/new/',
//       $('#newCategoryForm').serialize(),
//       function(data){
//         $('myModal').modal('hide');
//         location.reload();
//       }
//     )
//
//   });
//
//   $('#save-new-task').on('click', function(event){
//     event.preventDefault()
//     $.post('/to_do_list/task/new/',
//       $('#newTaskForm').serialize(),
//       function(data){
//         $('secModal').modal('hide');
//         console.log(data);
//         // location.reload();
//       }
//     )
//   });
// });
>>>>>>> d33f82c5de101619591daf07130004969adf8241
