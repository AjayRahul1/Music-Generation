from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import matplotlib.pyplot as plt, io, base64

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
  context = {"request" : request}
  return templates.TemplateResponse('index.html', context=context)

def conv_to_base64(fig):
  img_stream = io.BytesIO()
  fig.savefig(img_stream, format="png")
  img_stream.seek(0)
  img_data = base64.b64encode(img_stream.read()).decode("utf-8")
  return img_data

def plot_waveform():
  import librosa
  # Load the audio file
  file_path = 'musicgen_out.wav'
  y, sr = librosa.load(file_path)

  # Generate the waveform plot without axis labels
  plt.figure(figsize=(10, 2))
  librosa.display.waveshow(y, sr=sr)

  # Remove axis labels
  plt.axis('off')
  audio_waveform = conv_to_base64(plt)
  plt.close()
  return audio_waveform

@app.post('/generate-music', response_class=HTMLResponse)
async def generate_music(musicPrompt : str=Form(...)):
  audio_waveform = plot_waveform()
  html_content = f"""
  <img src="data:image/png;base64,{audio_waveform}" alt="Waveform" style="width: 100%; max-height: min-content;">
  <audio id="myAudio" src="/audio" preload="auto"></audio>
  <div class="text-center">
    <button class="btn btn-outline-success me-1" onclick="playMusic()">Play</button>
    <a href="/audio" download="MusicGen - Define your sound"><button class="btn btn-outline-success ms-1">Download</button></a>
  </div>
  <script>
    function playMusic() {{
      var audio = document.getElementById('myAudio');
      if (audio.paused) {{
        audio.play();
      }} else {{
        audio.pause();
      }}
    }}
  </script>
  """
  return HTMLResponse(content=html_content, status_code=200)

# Endpoint to serve the audio file
@app.get("/audio")
async def get_audio_file():
  audio_path = "musicgen_out.wav"
  return FileResponse(audio_path)