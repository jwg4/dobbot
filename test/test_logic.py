from nose.plugins.attrib import attr

from dobbot.logic import sets_to_play


@attr(milestone=1)
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


@attr(milestone=2)
def test_no_common_object():
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
        "four leaf clover",
        "question mark",
        "ink blot",
    ]
    try:
        value = sets_to_play(a, b)
    except Exception as e:
        assert e.args == ("No common element.",)
        return
    assert False, "No exception thrown."


@attr(milestone=2)
def test_two_common_objects():
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
        "bird",
        "stop sign",
        "yin yang",
        "question mark",
        "ink blot",
    ]
    try:
        value = sets_to_play(a, b)
    except Exception as e:
        assert e.args == ("More than one common element.",)
        return
    assert False, "No exception thrown."
