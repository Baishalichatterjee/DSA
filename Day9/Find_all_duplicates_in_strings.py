def printDuplicates(s):
    mpp = {};
    for c in s:
        mpp[c]=mpp.get(c,0)+1;
    for key,value in mpp.items():
        if value > 1:
             print(["{}".format(key),mpp[key]],end=",");

if __name__ == "__main__":

    s = "geeksforgeeks"

    printDuplicates(s)
