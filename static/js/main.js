$(document).ready(function(){
  $("#videourl").on('submit',function(event){
    $('#preloader').show();
  //     var name = $('#urlid').val()
  //   $.ajax({
  //         url:"/video_url",
  //         type:"POST",
  //         data: {
  //             videourl:$('#urlid').val()
  //               },
  //      //  beforeSend:function (){
  //      //        $('#preloader').show();
  //      //  },
  //      //
  //      success: function(response){
  //
  //        data = response.result
  //          console.log(data)
  //          for(i=0;i<data.length;i++){
  //              $('#name').load('youtube.html')
  //          }
  //      },
  //      // complete:function(data){
  //      //  // Hide image container
  //      // }
  //     }).done(function(data) {
  //           if (data.error) {
  //               // $("#loader").hide();
  //               $('#errorAlert').text(data.error).show();
  //               $('#successAlert').hide();
  //           }
  //           else {
  //               // $("#loader").hide();
  //               $('#successAlert').text(data.name).show();
  //               $('#errorAlert').hide();
  //           }
  //
  //       });
  //       event.preventDefault();
  });
});

//
// $(function(){
// 	$('button').click(function(){
// 		var user = $('#inputUsername').val();
// 		var pass = $('#inputPassword').val();
// 		$.ajax({
// 			url: '/signUpUser',
// 			data: $('form').serialize(),
// 			type: 'POST',
// 			success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 	});
// });

