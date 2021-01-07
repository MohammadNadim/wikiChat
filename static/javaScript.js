// javascript function using ajax 'POST' to return bot reply with JSON object
  function showUserTextPOST(){
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
    $("#textInput").val("");
    $("#chatbox").append(userHtml);   // printing the user text on the screen
    
    var input = {"freeText" : rawText};
    
    $.ajax({
      url: '/post',
      type: 'post',
      dataType: 'json',
      data: JSON.stringify(input),
      contentType: 'application/json',
      success: function(data){    // printing bot response on the screen
        var botHtml = '<p class="botText"><span> <b>Response:</b> ' + data.responseText + "</span></p>";
        $("#chatbox").append(botHtml);
      },
      error: function(error){
        alert (error);
      }
    });
  }

  function call_bot(event){
    if (event.which == 13 || event.KeyCode == 13){
      showUserTextPOST();
    }
  }