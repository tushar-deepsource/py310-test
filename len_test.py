SEQ = [1, 2, 3]
SEQ1 = (1, 2, 3)
SEQ2 = {1, 2, 3}
SEQ3 = list((1, 2, 3))

if len(SEQ) > 0:
    print(SEQ)

if len(SEQ) > 1:
    print(SEQ)

if len(SEQ1) > 0:
    print(SEQ1)

if len(SEQ1) > 1:
    print(SEQ1)

if len(SEQ2) > 0:
    print(SEQ2)

if len(SEQ2) > 1:
    print(SEQ2)

if len(SEQ3) > 0:
    print(SEQ3)

if len(SEQ3) > 1:
    print(SEQ3)

def something():
    if len(SEQ) > 0:
        print("SEQ is greater than 0")
