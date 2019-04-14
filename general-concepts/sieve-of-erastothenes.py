"""
Generate prime numbers between 1 and N
"""

def seiveOfErastothenes(n):
    pIndex = [True for _ in range(2, n)]
    pValues = [i for i in range(2, n)]

    pDict = dict(zip(pValues, pIndex))

    for key in pDict.keys():
        if pDict[key]:
            for i in range(key, n, key):
                if i != key:
                    pDict[i] = False

    return [key for key, val in pDict.items() if val is True]


if __name__ == "__main__":
    print(seiveOfErastothenes(15))