from nose.plugins.attrib import attr

from dobbot.logic import sets_to_play


@attr(milestone=5)
def test_one_common_object():
    a = [
        "yin yang",
        "fire",
        "orange man",
        "bird",
        "spider's web",
        "heart",
        "sunglasses",
        "exclamation mark",
    ]
    b = [
        "ice cube",
        "cheese",
        "tree",
        "stop sign",
        "yin yang",
        "question mark",
        "ink blot",
    ]
    value = sets_to_play(a, b)
    assert value == "yin yang", value
