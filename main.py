import src.dataPull.twelveData as dailyPull


if __name__ == '__main__':
    qString = {"exchange":"NASDAQ","format":"json"}
    outputLoc = 'data/twelveDataDaily.json'

    print('getting data')
    response = dailyPull.get12Data(qString=qString, outputLoc=outputLoc)

    with open(outputLoc, 'w') as outfile:
        outfile.write(response)