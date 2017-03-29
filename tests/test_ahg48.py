import ahg48


def test_address():
    assert ahg48.address().find("Eiheiji") != -1
