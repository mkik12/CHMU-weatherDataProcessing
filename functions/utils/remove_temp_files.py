import os

def removeTempFiles(dirPath: str) -> None:
    '''
    Removes temporary files created for the plugin's proper functionality.
    '''

    for file in os.listdir(dirPath):
        filePath = os.path.join(dirPath, file)
        try:
            os.remove(filePath)
        except:
            pass