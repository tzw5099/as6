import nose.tools as n
from io import StringIO
import functions


def test_write_to_file():
    out = StringIO()
    functions.write_to_file(["one", "two", "three", "four"], out)
    n.assert_equal(out.getvalue(), "1 one\n2 two\n3 three\n4 four\n")


def test_merge_files():
    f1 = StringIO("cat\ndog\npig\n")
    f2 = StringIO("rabbit\nhorse\nmouse\n")
    out = StringIO()
    functions.merge_files(f1, f2, out)
    n.assert_equal(out.getvalue(), "cat,rabbit\ndog,horse\npig,mouse\n")


def test_key_in_value():
    d = {"a": ["b", "c", "a"],
         "b": ["a", "c"],
         "c": ["c"],
         "d": ["c", "d"],
         "e": []}
    answer = set(("a", "c", "d"))
    result = functions.key_in_value(d)
    n.assert_equal(len(result), 3)
    n.assert_equal(set(result), answer)


def test_most_common_letters():
    result = functions.most_common_letters("abb bbdddc cdcdc")
    n.assert_equal(result, "b d c")


def test_merge_dictionaries():
    d1 = {"a": 3, "b": 9, "c": 4}
    d1_copy = d1.copy()
    d2 = {"b": 12, "c": 11, "d": 2, "e": 5}
    d2_copy = d2.copy()
    result = functions.merge_dictionaries(d1, d2)
    n.assert_equal(d1, d1_copy, 'd1 was changed')
    n.assert_equal(d2, d2_copy, 'd2 was changed')
    n.assert_equal(result, {"a": 3, "b": 21, "c": 15, "d": 2, "e": 5})
