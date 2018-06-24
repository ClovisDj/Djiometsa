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

  $(".email, #emailContact").click(function() {
    $(".email").addClass("hidden");
    $('#emailText').removeClass('hidden');
  });
  $('#closeButton').click(function() {
    $('#emailText').addClass('hidden');
    $('.email').removeClass('hidden');
    if ($('#status').text() !== '' ){
      $('#status').text('');
    }
  })

  $( window ).resize(function() {
    if ( $(window).width() < 601 ) {
      $('#message').attr("rows",'8');
    }else {
      $('#message').attr("rows",'10');
    }
  }).resize();

})

// Ajax POST
$(document).ready(function() {

  $('#send').click(function(event) {
    var data = $('#form').serialize();

    $.ajax({
      type: "POST",
      url: "ajax/send_email/",
      dataType: "json",
      data: data,
      success: function(data) {
        if (data['status'] === 'good') {
          $('#status').text("Message Successfully Delivered, thank you!");
          $('#status').css('color','green');
          $('#name, #email, #subject, #message').val('');
        }else {
          $('#status').text(data['status']);
          $('#status').css('color','red');
        }
      },
    });
    event.preventDefault();
  })

  var csrftoken = Cookies.get('csrftoken');

  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
})
