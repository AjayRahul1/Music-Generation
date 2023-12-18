from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
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

@app.post('/generate-music', response_class=HTMLResponse)
async def generate_music(musicPrompt : str=Form(...)):
  import librosa
  # Load the audio file
  file_path = 'musicgen_out.wav'
  y, sr = librosa.load(file_path)

  # Generate the waveform plot without axis labels
  plt.figure(figsize=(10, 2))
  librosa.display.waveshow(y, sr=sr)

  # Remove axis labels
  plt.axis('off')
  audio_waverform = conv_to_base64(plt)
  plt.close()

  html_content = f"""
  <html>
    <body>
      <div class="border rounded mb-2 overflow-hidden">
        <img src="data:image/png;base64,{audio_waverform}" alt="Waveform" style="width: 100%; max-height: min-content;">
        <h2><strong>{musicPrompt}</strong></h2>
      </div>
    </body>
  </html>
  """
  return HTMLResponse(content=html_content, status_code=200)