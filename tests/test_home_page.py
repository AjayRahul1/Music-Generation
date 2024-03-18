from fastapi.testclient import TestClient
import main

client = TestClient(app=main.app)

def test_home():
  response = client.get("/")
  assert response.status_code == 200

def test_generate_audio():
  response = client.get("/audio/musicgen_out")
  assert response.status_code == 200