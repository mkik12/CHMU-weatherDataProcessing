def getOutputName(chosenCategory: str, interpolationMethod, outputPath: str) -> str:
    if outputPath is None:
        outputName = f"{chosenCategory} - {interpolationMethod}"
    else:
        outputName = outputPath.split("\\")[-1].split(".")[0]
    
    return outputName