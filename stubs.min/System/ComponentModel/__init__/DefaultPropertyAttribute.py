class DefaultPropertyAttribute(Attribute, _Attribute):
    """
    Specifies the default property for a component.
    
    DefaultPropertyAttribute(name: str)
    """
    def Equals(self, obj):
        """
        Equals(self: DefaultPropertyAttribute, obj: object) -> bool
        
            Returns whether the value of the given object is equal to the current System.ComponentModel.DefaultPropertyAttribute.
        
            obj: The object to test the value equality of.
            Returns: true if the value of the given object is equal to that of the current; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DefaultPropertyAttribute) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the default property for the component this attribute is bound to.

Get: Name(self: DefaultPropertyAttribute) -> str

"""


    Default = None
