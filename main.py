from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import matplotlib.pyplot as plt, io, base64
import librosa
from transformers import pipeline
import scipy

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
  return templates.TemplateResponse('index.html', context={"request" : request})

def conv_to_base64(fig: plt) -> str:
  """Converts a plot into image varibale in Base64 Format such that it can displayed on the website.
  :param fig: plot variable.
  :return: Image in string base64 format."""
  img_stream = io.BytesIO()
  fig.savefig(img_stream, format="png")
  img_stream.seek(0)
  img_data = base64.b64encode(img_stream.read()).decode("utf-8")
  return img_data

def generate_audio(musicPrompt: str, audioLength: int):
  """Generates the audio for the prompt entered."""
  synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")
  max_length = int(51.2 * audioLength) # for 15 seconds (768/51.2 = 15)
  music = synthesiser(musicPrompt, forward_params={"do_sample": True, "max_length": max_length})
  scipy.io.wavfile.write("musicgen_out.wav", rate=music["sampling_rate"], data=music["audio"])

def plot_waveform(musicPrompt: str, audioLength: int) -> str:
  """Generates the waveplot for the audio that is generated."""
  # Load the audio file
  file_path = 'musicgen_out.wav'
  y, sr = librosa.load(file_path)

  # Create a variable for the plot
  fig, ax = plt.subplots(figsize=(8, 2))
  # Generate the waveform plot without axis labels
  fig.patch.set_facecolor('#C0CFFA')
  ax.set_title(label=musicPrompt + " - " + str(audioLength) + " seconds")
  fig.tight_layout()
  librosa.display.waveshow(y, sr=sr, color='k', ax=ax)
  # Remove axis labels
  ax.axis('off')
  # Convert the plot into base64 image
  audio_waveform = conv_to_base64(fig)
  # Close the plot
  plt.close(fig)
  return audio_waveform

@app.post('/generate-music', response_class=HTMLResponse)
async def generate_music(musicPrompt: str=Form(..., title="musicPrompt"), audioLength: int=Form(...)):
  print("Generating Audio...\nPrompt:", musicPrompt, "\nLength: ", audioLength, " seconds")
  generate_audio(musicPrompt, audioLength)
  audio_waveform_img = plot_waveform(musicPrompt, audioLength)
  audio_filepath="musicgen_out"
  html_content = f"""
  <img class="rounded" src="data:image/png;base64,{audio_waveform_img}" alt="Waveform" style="width:100%; max-height: max-content;">
  <audio id="myAudio" src="/audio/{audio_filepath}" preload="auto"></audio>
  <div class="text-center my-2">
    <button class="blueGradientBtn me-1" onclick="playMusic()">Play</button>
    <a href="/audio" download="{musicPrompt} - AudioYours - Define your sound"><button class="blueGradientBtn ms-1">Download</button></a>
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
@app.get("/audio/{audio_filepath}")
async def get_audio_file(audio_filepath: str):
  audio_file_extension = ".wav"
  return FileResponse(audio_filepath+audio_file_extension)