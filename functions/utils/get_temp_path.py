from tempfile import NamedTemporaryFile

def getTempPath(fileExtension: str, directory: str) -> str: 
    '''
    Creates a path to the plugin's temporary folder with the specified suffix.
    '''

    with NamedTemporaryFile(suffix=fileExtension, dir=directory) as tempFile:
        tempFilePath = tempFile.name
    
    return tempFilePath