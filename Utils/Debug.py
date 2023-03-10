from Utils import pr





class Debug():

    """
    Utility class for custom debuging
    """

    def objlist(listOfObjects, definition="Objects"):
        """
            Returns List of Object Names from List of Objects
    
            :listOfObjects: List of Objects to be parsed
            :definition: Naming scheme in Output like (Loaded {definition}: {listOfObjectNames})
                
            =return= Returns DBG Print
        """ 
        _curObjects = []
        for _object in listOfObjects:
            _curObjects.append(_object.name)
        return pr.dbg(F"Loaded {definition}: {_curObjects}")