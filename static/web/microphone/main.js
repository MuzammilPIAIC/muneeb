// Set up the AudioContext.
const audioCtx = new AudioContext();

// Top-level variable keeps track of whether we are recording or not.
let recording = false;

// Ask user for access to the microphone.
if (navigator.mediaDevices) {
    navigator.mediaDevices.getUserMedia({"audio": true}).then((stream) => {
    const mediaRecorder = new MediaRecorder(stream);
    let chunks = [];

    mediaRecorder.ondataavailable = (event) => {
      chunks.push(event.data);
      console.log(chunks);
      download(chunks);

    }
    mediaRecorder.onstop = (event) => {
      const audio = new Audio();
      audio.setAttribute("controls", "");
      $("#sound-clip").append(audio);
      $("#sound-clip").append("<br />");

      const blob = new Blob(chunks, {"type": "audio/ogg; codecs=opus"});
      audio.src = window.URL.createObjectURL(blob);
      console.log(audio.src )
      sendAudioFile(blob);
      chunks = [];
    };


    // Set up event handler for the "Record" button.
    $("#record").on("click", () => {
      if (recording) {
        console.log('start recording')
        // mediaRecorder.stop();
        mediaRecorder.pause();
        recording = false;
        $("#record").html("Start");
      } else {
        mediaRecorder.start();
        recording = true;
        $("#record").html("Stop");
      }
    });

    $("#record-start").on("click", () => {
        mediaRecorder.start();
        console.log('start recording')
      });


    $("#record-stop").on("click", () => {
          mediaRecorder.stop();
          recording = false;
          console.log('Stop recording')
          
        
      });
    $("#record-resume").on("click", () => {
          mediaRecorder.resume();
          recording = false;
          console.log('Resume recording')

        
      });
      $("#record-pause").on("click", () => {
          mediaRecorder.pause();
          recording = false;
          console.log('Pause recording')
      });



  }).catch((err) => {
    alert("Oh no! Your browser cannot access your computer's microphone.");
  });
} else {
  alert("Oh no! Your browser cannot access your computer's microphone. Please update your browser.");
}


function download(chunks) {
  const blob = new Blob(chunks, {
    type: "audio/ogg" 
  });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  document.body.appendChild(a);

  var audio_file_class = 'audio-file';

  // a.style = "display: block";
  a.href = url;
  a.download = "test.mp3";
  document.getElementById('audio-file').files[0] = url
  // a.click();
  window.URL.revokeObjectURL(url);
}

const sendAudioFile = file => {
  const formData = new FormData();
  formData.append('audio-file', file);
  formData.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken')[0].value)
  return fetch('http://localhost:9000/record2/', {
    method: 'POST',
    body: formData
  });
};
