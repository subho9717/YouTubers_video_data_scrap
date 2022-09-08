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

  $('#videourl').on('submit',function(){
    $('#preloader').show()
  })
})