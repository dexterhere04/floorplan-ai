from app.models.layout_models import Layout
import pytest

def test_layout_creation():
    data={
        "rooms":[
            {"id":1,"type":"Bedroom","area":120}
        ],
        "relations": []
    }
    layout=Layout(**data)

    assert len(layout.rooms)==1
    assert layout.rooms[0].type=="Bedroom"
    assert layout.rooms[0].area==120
    assert layout.relations==[]

def test_layout_invalid_missing_room_field():
    data = {
        "rooms": [
            {"id": 1, "area": 120}  # missing type
        ],
        "relations": []
    }

    with pytest.raises(Exception):
        Layout(**data)