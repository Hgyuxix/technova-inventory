import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test endpoint utama"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "TechNova Inventory API is running"

def test_get_items(client):
    """Test ambil semua item"""
    response = client.get("/items")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 2

def test_get_single_item(client):
    """Test ambil satu item berdasarkan ID"""
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Laptop"

def test_get_item_not_found(client):
    """Test item yang tidak ada"""
    response = client.get("/items/999")
    assert response.status_code == 404

def test_add_item(client):
    """Test tambah item baru"""
    new_item = {"name": "Keyboard", "quantity": 20}
    response = client.post("/items", json=new_item)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Keyboard"
    assert data["quantity"] == 20