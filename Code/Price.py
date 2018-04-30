import json


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

def getPrice():
    import os
    os.chdir(os.path.dirname(__file__))
    a = open(os.getcwd() + '\Addresses.json', 'r')
    f = open(os.getcwd() + '\Final.json', 'r')

    addresses = json.load(a)
    final = json.load(f)

    for aa in addresses:
        aa['FIELD3'] = aa['FIELD3'].title()

    a.close()
    f.close()

    iii = 0;
    print(len(addresses))
    print(len(final))
    for f in final:
        add = f['Street']
        street = int(str(add).split(' ')[0])
        c = 0
        i = -1
        at = -1

        for a in addresses:
            i = i + 1
            if len (str(a['FIELD3']).split(' ')) <= 0:

                continue
            if not str(a['FIELD3']).split(' ')[0].isdigit():
                continue
            streetThis = int(str(a['FIELD3']).split(' ')[0])
            if streetThis != street:
                continue;
            if (lcs(add, a['FIELD3']) > c):
                at = i
                c = lcs(add, a['FIELD3'])
        if at >= 0:
            f['Price'] = addresses[at]['FIELD7'].replace(',', '').replace('$', '')
            f['AddressTaken'] = addresses[at]['FIELD3']
        iii = iii + 1
        print(iii)

    with open('WithPrice.json', 'w') as fp:
        json.dump(final, fp)

#getPrice()