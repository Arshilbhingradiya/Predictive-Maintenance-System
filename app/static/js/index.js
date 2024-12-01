

document.addEventListener('DOMContentLoaded', function() {
  
  var prediction = document.querySelector('#result h2').textContent.trim();

  var audio = new Audio('/static/js/alert.mp3'); 

  
  if (prediction === "Maintenance required") {
    
    engine = pyttsx3.init()
engine.say("alert alert alert")
engine.runAndWait()
  }
});
