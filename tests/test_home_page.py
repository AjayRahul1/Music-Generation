"""
Run the program using
$ pytest -W ignore
to filter the warnings
"""

from fastapi.testclient import TestClient
import main

client = TestClient(app=main.app)

def test_home():
  response = client.get("/")
  assert response.status_code == 200

def test_generate_audio_response():
  # Change the data below to modify the testing conditions
  data = { "musicPrompt": "A 90s funky beat", "audioLength": 5 }
  response = client.post("/generate-music", data=data)
  assert response.status_code == 200

def test_generate_audio():
  timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
  response = client.get(f"/audio/musicgen_out?t={timestamp}")
  assert response.status_code == 200
