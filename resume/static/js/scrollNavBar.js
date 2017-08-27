
$(document).ready(function() {
  var myTimeout;

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

  $('.media-body').mouseenter(function() {
    myTimeout = setTimeout(function() {
      $('.media-body>h1').text("Clovis Djiometsa Ngnitewe").hide();
      $('.media-body>h1').fadeIn(800);
      }, 500);
    }).mouseleave(function() {
        clearTimeout(myTimeout);
        $('.media-body>h1').html("<code>{</code>Clovis_Djiometsa<code>}</code>").hide();
        $('.media-body>h1').fadeIn(800);
      });

  var cssImgOn = {
    width: 250,
    transition: 'width 1s ease'
  };
  var cssImgOff = {
    width: 150,
    transition: 'width 1s ease'
  };
  $('.media-left>#clo').hover(function(){
    $(this).css(cssImgOn);
  }, function() {
    $(this).css(cssImgOff);
  })

  $( window ).resize(function() {
    if( $(window).width() ) {
      $('canvas').css("width", $(window).width());
      $('canvas').css("height", $(window).height()*2/5);
    }
  }).resize();

  $(".email").mouseenter(function() {
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
