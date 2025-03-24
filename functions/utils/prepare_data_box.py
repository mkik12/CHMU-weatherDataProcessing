def prepareDataBox(IDs: list) -> dict[list]:
    '''
    Creates a dictionary containing these items:\n
    * key = station ID (used as an index for values stored in lists)\n
    * value = empty list (used for storing mean values for every station's date interval)
    '''

    dataBox = {}

    for ID in IDs:
        dataBox[ID] = []

    return dataBox