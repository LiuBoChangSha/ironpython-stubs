class SpecialType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumerated type listing special types that can appear in an Autodesk.Revit.DB.ExportLayerTable.
       These types do not represent an independent category in Revit, but can be mapped to specific layers on export.
    
    enum SpecialType, values: Default (-1), ExteriorWall (2), FoundationWall (3), InteriorWall (1), RetainingWall (4)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Default = None
    ExteriorWall = None
    FoundationWall = None
    InteriorWall = None
    RetainingWall = None
    value__ = None
