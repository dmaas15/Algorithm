score=input("Enter Score:")
fscore=float(score)
if fscore > 1.0:
    print(">1.0 is not valid")
elif fscore >= 0.9:
    print("A")
elif fscore >= 0.8:
    print("B")
elif fscore >= 0.7:
    print("C")
elif fscore >= 0.6:
    print("D")
elif fscore >=0.0:
    print("F")
else:
    print("<0.0 is not valid")
