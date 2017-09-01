$(document).ready(function() {

  var myTimeout;

  // $( window ).resize(function() {
  //   if( $(window).width() >= 768 ) {
  //     $('.topbar').css("padding-right", 70);
  //   }
  // }).resize();

  $('.navig>.topbar>#brand').mouseenter(function() {
    myTimeout = setTimeout(function() {
      $('.navig>.topbar>#brand').children().text("Clovis Djiometsa");
        $('.navig>.topbar>#brand').hide().fadeIn(500);
      }, 500);
    }).mouseleave(function() {
        clearTimeout(myTimeout);
        $('.navig>.topbar>#brand').children().html("<code>{</code>Clovis<code>}</code>");
        $('.navig>.topbar>#brand').hide().fadeIn(500);
      });


  $(".email").click(function() {
    $(this).addClass("hidden");
    $('#emailText').removeClass('hidden');
  });
  $(".email").click(function() {
    $(this).addClass("hidden");
    $('#emailText').removeClass('hidden');
  });
  $('#closeButton').click(function() {
    $('#emailText').addClass('hidden');
    $('.email').removeClass('hidden');
  })
})
