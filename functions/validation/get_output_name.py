import os

def getOutputName(chosenCategory: str, interpolationMethod, outputPath: str) -> str:
    if outputPath is None:
        outputName = f"{chosenCategory} - {interpolationMethod}"
    else:
        outputName = os.path.basename(outputPath).split(".")[0]
    
    return outputName