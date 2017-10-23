hasContent = false;

incrementor = 0;
samples = ["strollers", "coffee shops in Providence", "bicycle makers", "hotels in Reykjavik"];

$(document).ready(function(){
  setButtonEvents();
  setListableEvents();
  requestAnimationFrame(scrollSamples);

});

function setListableEvents(){
  $("#listable").focus(function(){
    hasContent = true;

    txtContent = $("#listable").val().trim();
    if(samples.indexOf(txtContent) > -1)
    {
      $("#listable").val("");
    }

    if ($("#listable").hasClass("fadedFont")){
      $("#listable").removeClass("fadedFont");
    }

  });

  $("#listable").focusout(function(){
    txtContent = $("#listable").val().trim();
    if(txtContent == "")
    {
      hasContent = false;
      requestAnimationFrame(scrollSamples);
    }
    else
    {
      hasContent = true;
    }
  });
}
function setButtonEvents(){
  $("#rankem").click(function(){
    searchTerm = $("#listable").val().trim();
    //if there is no good content, then do nothing
    if (searchTerm == "" || samples.indexOf(searchTerm) > -1){
      $(".messageAlert").text("Please provide a valid search");
      $(".messageAlert").css("display", "block");
    }
    //if there is good content, then load it in the database and show an error message and thank them.
    else{

      $.ajax({
        method: "POST",
        url: "https://api.airtable.com/v0/applFlW642fYMqKOj/Table%201",
        beforeSend: function (xhr) {
          xhr.setRequestHeader('Authorization', 'Bearer keyqXy9wVseyd2L6S');
          $("#rankem").attr("disabled", "disabled");
        },
        contentType: "application/json",
        data: '{"fields": {"Search Term": "'+ searchTerm + '"}}'
      })
        .done(function( msg ) {
          $(".messageAlert").text("We are so excited that you want to use our product! We're still working, though. Please check back in a month or so!");
          $(".messageAlert").css("display", "block");
          $("#rankem").removeAttr("disabled");
        })
        .always(function(msg) {
          console.log(msg);
        });
    }
  });
}

function setDefaultStyling()
{
  // var disabled_attr = $("#rankem").attr('disabled');
  // if (typeof disabled_attr == typeof undefined || disabled_attr == false)
  // {
  //   $("#rankem").attr('disabled', 'disabled');
  // }

  if (!$("#listable").hasClass("fadedFont")){
    $("#listable").addClass("fadedFont");
  }
}

function scrollSamples()
{
  setDefaultStyling();

  index = (incrementor % samples.length);
  phrase = samples[index];

  var millisecondsToWait = 2000;
  $("#listable").val(phrase);


  setTimeout(function() {
    incrementor = incrementor + 1;
    if(!hasContent)
    {
      requestAnimationFrame(scrollSamples);
    }
  }, millisecondsToWait);

}