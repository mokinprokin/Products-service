$('.chat-input div  input').keyup(function(e) {
    if ($(this).val() == '')
      $(this).removeAttr('good');
    else
      $(this).attr('good', '');
  });