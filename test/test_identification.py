from nose.plugins.attrib import attr

from dobbot.identification import image_to_symbol, card_to_list, image_to_play


@attr(milestone=100)
def test_image_to_play():
    with open("test/img/two_cards_001.jpg") as f:
        data = f.read()
    value = image_to_play(data)
    self.assertEqual(value, "question mark")


@attr(milestone=70)
def test_image_to_play():
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
    self.assertEqual(value, expected)


@attr(milestone=30)
def test_image_to_play():
    with open("test/img/single_symbol__cheese__001.jpg", 'rb') as f:
        data = f.read()
    value = image_to_symbol(data)
    self.assertEqual(value, "cheese")
    