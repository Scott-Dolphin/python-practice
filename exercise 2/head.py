def itPrinter(x):
    cNumber = 0
    pNumber = 0
    print(f'Current Number {cNumber} Previous number 0 Sum: 0')

    for iteration in range(x):
        cNumber += 1
        print(f'Current Number {cNumber} Previous Number {pNumber} Sum: {cNumber + pNumber}')
        pNumber += 1
