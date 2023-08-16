def test_for_else(target):
    i = 0
    while i < 6:
        if i == target:
            print("get it!")
            break
        i = i+1
    else:
        print("ho no, i cant find ", target)

if __name__ == "__main__":
    test_for_else(3)
    test_for_else(8)
