$(document).ready(function(){
  $('.about').hide()
  $(function(){
    $('.button-collapse').sideNav();
  });
  $('#download-button').click(function(){
    $('.about').slideToggle('400');
  });

  $('.modal').modal();

  // test of ajax
  $(document).on("click",".likes", function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/like_category/', {question_id: catid}, function(data){
               $('#like_count').html(data);

               //$('#likes').hide(); // hides like buttons
    });
    location.reload(); // brute way, maybe try to find a better way
});

  $('#sub_but').click(functoin(){
    location.reload();
  });



/*$("a.like").click(function(){
    var curr_elem = $(this) ;
    $.get($(this).attr('href'), function(data){
        var my_div = $(curr_elem).parent().find("b");
        my_div.text(my_div.text()*1+1);
    });
    return false; // prevent loading URL from href
}); */

});
