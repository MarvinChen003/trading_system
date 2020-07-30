from db_func import StudentDB


def test_scott_data():
    db = StudentDB()
    db.connect("data.json")
    scott_data = db.get_data("Scott")
    assert scott_data["id"] == 1
    assert scott_data["name"] == "Scott"
    assert scott_data["result"] == "pass"
    db.close


def test_mark_data():
    db = StudentDB()
    db.connect("data.json")
    mark_data = db.get_data("Mark")
    assert mark_data["id"] == 2
    assert mark_data["name"] == "Mark"
    assert mark_data["result"] == "fail"
    db.close
