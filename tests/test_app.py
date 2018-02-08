import pytest
import json
from src.app import app

@pytest.fixture
def client():
  return app.test_client()

def test_respons(client):
  """Test that the app is responding"""
  res = client.get('/')
  assert res.status_code == 200

def test_root_message(client):
  """Test that root route returns a json object containing a message"""
  res = client.get('/')
  data = json.loads(res.data)
  assert data["message"] == "Monitor API is up and running"