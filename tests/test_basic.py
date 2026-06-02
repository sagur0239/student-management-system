from app.services import create_student

def test_create():
    s = create_student("Test", 20, "A")
    assert s["name"] == "Test"