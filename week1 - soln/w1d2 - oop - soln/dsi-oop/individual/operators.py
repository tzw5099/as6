#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UnionShape():
    """The union of two shapes (as objects defined in shapes.py).

    Parameters
    ----------
    shape_a   : {shape} shape object A.
    shape_b   : {shape} shape object B.

    Attributes
    ----------
    TBD
    """
    def __init__(self, shape_a, shape_b):
        """Constructs a UnionShape as union of given shapes
        shape_a and shape_b.

        Note: color or union should be the average between
        colors of shape_a and shape_b.
        """
        pass

    def mu(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False.

        Parameters
        ----------
        x : int, x coordinate of a pixel
        y : int, y coordinate of a pixel

        Returns
        -------
        boolean : True or False whether (x,y) is within the shape.
        """
        pass


class IntersectionShape():
    """The intersection of two shapes (as objects defined in shapes.py).

    Parameters
    ----------
    shape_a   : {shape} shape object A.
    shape_b   : {shape} shape object B.

    Attributes
    ----------
    TBD
    """
    def __init__(self, shape_a, shape_b):
        """Constructs a IntersectionShape as intersection
        of given shapes shape_a and shape_b.

        Note: color or intersection should be the average between
        colors of shape_a and shape_b.
        """
        pass

    def mu(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False.

        Parameters
        ----------
        x : int, x coordinate of a pixel
        y : int, y coordinate of a pixel

        Returns
        -------
        boolean : True or False whether (x,y) is within the shape.
        """
        pass


class DiffShape():
    """The difference of two shapes (as objects defined in shapes.py).

    Parameters
    ----------
    shape_a   : {shape} shape object A.
    shape_b   : {shape} shape object B.

    Attributes
    ----------
    TBD
    """
    def __init__(self, shape_a, shape_b):
        """Constructs a DiffShape as difference between two given shapes
        shape_a and shape_b.

        Note: color or difference should be the color of shape_a.
        """
        pass

    def mu(self, x, y):
        """Characteristic function of the shape.
        Returns True if (x,y) is inside the shape, else False.

        Parameters
        ----------
        x : int, x coordinate of a pixel
        y : int, y coordinate of a pixel

        Returns
        -------
        boolean : True or False whether (x,y) is within the shape.
        """
        pass
