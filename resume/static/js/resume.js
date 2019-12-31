$(document).ready(function() {

  $( window ).resize(function() {
    if ( $(window).width() < 700 ) {
      $('.tools').addClass('hidden');
      $('.tools2').removeClass('hidden');
    }
  }).resize();
})
