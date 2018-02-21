class Template:
    """
    Template to be used for matching against images.

    Args:
        template (Template): initializes the template to be a clone of the other template
    """
    def __init__(self, template=None):
        if template:
            self.boxes = template.boxes
        else:
            self.boxes = []

    def addBox(self, name, descr, datatype):
        """
        adds a box to the template

        Args:
            name (str):                        A string to identify given box. Should be unique
            descr (tuple<int, int, int, int>): Top left coord, top right coord, width, height of box
            datatype (str):                    Name of datatype to be found in box.

        Side Effects:
            Appends a dictionary created from the parameters to the template boxes list
        """
        assert name not in map(lambda box: box['name'], self.boxes)

        newBox = {
            'name': name,
            'descr': descr,
            'datatype': datatype
        }

        self.boxes.append(newBox)
