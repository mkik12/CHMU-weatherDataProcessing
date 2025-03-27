def prepareDataBox(IDs: list) -> dict[list]:
    '''
    Creates a dictionary with the following structure:
    - Key: Station ID (used as an index for values stored in lists).
    - Value: An empty list (used to store mean values for each station's date interval).
    '''

    dataBox = {}

    for ID in IDs:
        dataBox[ID] = []

    return dataBox