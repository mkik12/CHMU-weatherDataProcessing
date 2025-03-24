def printDates(dates: list) -> None:
    print("Date intervals for different point layers used in raster interpolation.")

    for date in dates:
        print(f"{date[0].toString('dd/MM/yyyy')} - {date[1].toString('dd/MM/yyyy')}")