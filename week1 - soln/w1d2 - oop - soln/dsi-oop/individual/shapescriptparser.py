#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shapes import Circle, Rectangle
from operators import UnionShape, IntersectionShape, DiffShape
from collections import OrderedDict

class ShapeScriptParser():
    """A parser for a scripting language
    that would generate shapes (as objects defined in shapes.py)
    and display the result on screen (using SimpleGUI).

    Parameters
    ----------
    gui : {SimpleGUI} a gui object for drawing pixels.

    Attributes
    ----------
    TBD
    """
    def __init__(self, gui):
        """Instanciates the parser, gui is provided for drawing.
        """
        pass

    def parse(self, filepath):
        """Parses a file line by line using parse_line().

        Parameters
        ----------
        filename : {str} the path to the file

        Returns
        -------
        None
        """
        pass

    def parse_line(self, line):
        """Parses one line of the scripting language.
        Creates the corresponding object.

        Parameters
        ----------
        line    : {str} the line to parse

        Returns
        -------
        None
        """
        pass

    def draw(self):
        """Draws objects that have been created previously
        with parse() or parse_line().

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        pass
