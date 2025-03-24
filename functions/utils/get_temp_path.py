from tempfile import NamedTemporaryFile

def getTempPath(fileExtension: str, directory: str) -> str: 
    '''
    Creates a temporary path with a specified suffix. 
    '''

    with NamedTemporaryFile(suffix=fileExtension, dir=directory) as tempFile:
        tempFilePath = tempFile.name
    
    return tempFilePath