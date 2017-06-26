class Cylinder(object, IEpsilonComparable[Cylinder]):
    """
    Cylinder(baseCircle: Circle)
    Cylinder(baseCircle: Circle, height: float)
    """
    def CircleAt(self, linearParameter):
        """ CircleAt(self: Cylinder, linearParameter: float) -> Circle """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: Cylinder, other: Cylinder, epsilon: float) -> bool """
        pass

    def LineAt(self, angularParameter):
        """ LineAt(self: Cylinder, angularParameter: float) -> Line """
        pass

    def ToBrep(self, capBottom, capTop):
        """ ToBrep(self: Cylinder, capBottom: bool, capTop: bool) -> Brep """
        pass

    def ToNurbsSurface(self):
        """ ToNurbsSurface(self: Cylinder) -> NurbsSurface """
        pass

    def ToRevSurface(self):
        """ ToRevSurface(self: Cylinder) -> RevSurface """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, baseCircle, height=None):
        """
        __new__[Cylinder]() -> Cylinder
        
        __new__(cls: type, baseCircle: Circle)
        __new__(cls: type, baseCircle: Circle, height: float)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis(self: Cylinder) -> Vector3d

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: Cylinder) -> Point3d

"""

    Height1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height1(self: Cylinder) -> float

Set: Height1(self: Cylinder) = value
"""

    Height2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height2(self: Cylinder) -> float

Set: Height2(self: Cylinder) = value
"""

    IsFinite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinite(self: Cylinder) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Cylinder) -> bool

"""

    TotalHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalHeight(self: Cylinder) -> float

"""


    Unset = None
