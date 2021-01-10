
$(document).ready(function() {

  windowHeight = $(window).height();
  $('.head').css({'padding-bottom': windowHeight/8 + 'px'});

  // $('.main').css('margin-top', $("canvas").height()*2/5);

  var myTimeout;
  $('.media-body').mouseenter(function() {
      $('.media-body>h1').text("Clovis Djiometsa Ngnitewe").hide();
      $('.media-body>h1').show();
    }).mouseleave(function() {
        $('.media-body>h1').html("<code>{</code>Clovis_Djiometsa<code>}</code>").hide();
        $('.media-body>h1').show();
      });

  var cssImgOn = {
    width: 250,
    transition: 'width 1s ease'
  };
  var cssImgOff = {
    width: 150,
    transition: 'width 1s ease'
  };

  if ($(window).width() < 601) {
     cssImgOn = {
      width: 150,
      transition: 'width 1s ease',
    };
    cssImgOff = {
      width: 80,
      "padding-bottom": '200',
      transition: 'width 1s ease'
    };
  }

  $('.media-left>#clo').hover(function(){
    $(this).css(cssImgOn);
  }, function() {
    $(this).css(cssImgOff);
  })


  $('#myMap,#duomo,#montreal,#austin, #clev, #greenv, #silicon-hills-img').click(function() {
    $(this).parent().removeClass('col-md-6').removeClass('col-md-offset-6').addClass('col-md-12');
  }).mouseleave(function() {
    $(this).parent().addClass('col-md-6').addClass('col-md-offset-6');
  })

  $('#myMap').mouseenter(function() {
    $(this).parent().removeClass('col-md-6').removeClass('col-md-offset-6').addClass('col-md-12');
  }).mouseleave(function() {
    $(this).parent().addClass('col-md-6').addClass('col-md-offset-6');
  })
})
