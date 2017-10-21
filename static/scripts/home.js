hasContent = false;

$(document).ready(function(){
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

incrementor = 0;
samples = ["strollers", "coffee shops in Providence", "bicycle makers", "hotels in Reykjavik"];



function scrollSamples()
{
  if (!$("#listable").hasClass("fadedFont")){
    $("#listable").addClass("fadedFont");
  }
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