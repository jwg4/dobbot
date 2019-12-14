from nose.plugins.attrib import attr

from dobbot.game import image_to_play


@attr(milestone=100)
def test_image_to_play():
    with open("test/img/two_cards_001.jpg") as f:
        data = f.read()
    value = image_to_play(data)
    assert value == "question mark", value
