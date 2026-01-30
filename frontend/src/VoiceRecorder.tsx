import React, { useState } from "react";

const VoiceRecorder = () => {
  const [response, setResponse] = useState("");

  const recordAudio = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    const chunks: Blob[] = [];

    mediaRecorder.ondataavailable = e => chunks.push(e.data);
    mediaRecorder.onstop = async () => {
      const audioBlob = new Blob(chunks, { type: "audio/wav" });
      const formData = new FormData();
      formData.append("file", audioBlob);

      const res = await fetch("http://localhost:8000/voice-chat", {
        method: "POST",
        body: formData
      });

      const data = await res.json();
      setResponse(data.response_text);

      const audio = new Audio(`data:audio/mp3;base64,${data.audio}`);
      audio.play();
    };

    mediaRecorder.start();
    setTimeout(() => mediaRecorder.stop(), 4000);
  };

  return (
    <div>
      <button onClick={recordAudio}>🎙️ Speak</button>
      <p>{response}</p>
    </div>
  );
};

export default VoiceRecorder;
