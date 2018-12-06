class jiraListString():

    separator = ""
    itemList = ""

    def __init__(self, separator, itemList):
        self.separator = separator
        self.itemList = itemList

    def __init__(self):
        pass

    def add_separator_text(self, separator, itemList):
        long_string = ''
        if len(itemList) > 1:
            for item in itemList:
                if item == itemList[-1]:
                    # add the last item to the string
                    long_string += str(item)
                else:
                    # add the item and the separator string
                    long_string += str(item) + str(separator)
            return long_string
        else:
            return ""
