from dtab.parser import NameTreeParsers
from unittest import TestCase


class PathTest(TestCase):

  def test_show(self):
    self.assertTrue(NameTreeParsers.parsePath("/foo/bar").show == "/foo/bar")
