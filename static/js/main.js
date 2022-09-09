$(document).ready(function(){

  


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
      url = $('#urlid').val()
      $.ajax({
        url: "/video_url",
        type: "POST",
        data: {'data':url},
                
      }).done(function(data){
        console.log(data) 
        window.location = data;
       })
      e.preventDefault();
      
      
  });

  })