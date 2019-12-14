from nose.plugins.attrib import attr

from dobbot.identification import image_to_symbol, card_to_list
 

@attr(milestone=70)
def test_card_to_list():
    with open("test/img/single_card_001.jpg") as f:
        data = f.read()
    value = card_to_list(data)
    expected = [
        "yin yang",
        "fire",
        "orange man",
        "bird",
        "spider's web",
        "heart",
        "sunglasses",
        "exclamation mark"
    ]
    assert value == expected, value


@attr(milestone=30)
def test_image_to_symbol():
    with open("test/img/single_symbol__cheese__001.jpg", 'rb') as f:
        data = f.read()
    value = image_to_symbol(data)
    assert value == "cheese", value
