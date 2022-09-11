$(document).ready(function(){
  // $("#comment_table").hide();
  


  var count = 0;
  var counter = setInterval(function(){
  if (count < 101){
    $('.count').text(count + '%');
    $('.loader').css('width', count +  '%')
    count++
  }
  else{
    clearInterval(counter)
  }
})

  $('#videourl').on('submit',function(e){
    $('#preloader').show()
    // alert($('#urlid').val())
  //     url = $('#urlid').val()
  //     $.ajax({
  //       url: "/video_url",
  //       type: "POST",
  //       data: {'data':url},
  //
  //     }).done(function(data){
  //       console.log(data)
  //       window.location = data;
  //      })
  //     e.preventDefault();
  //
  //
  });
  // var display =  $("#comment_table").css("display");
  //   if(display!="none")
  //   {
  //       $("#comment_table").attr("style", "display:none");
  //   }
  // $('#comment').click(function(e){
  //   $("#comment_table").show();
  // })

  // $("#comment_table tr td").each(function(){
  //   var emptyrows = $.trim($(this).text());
  //   console.log(emptyrows.length)
  //   if (emptyrows.length == 0){
  //     $("#comment_table").hide();
  //   }
  // }); 
  var trd_count = $("#comment_table tr ").length
  if (trd_count < 2){
        $("#comment_table").hide();
      }

  })