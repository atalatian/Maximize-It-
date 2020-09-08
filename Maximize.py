import re
import random


def get_values():
    m = None
    k = []
    k_allow = None
    ith = [None, None, None, None, None, None, None]
    try:
        m_k_value = input()
        k_allow = re.findall("\d+", m_k_value)[0]
        m = re.findall("\d+", m_k_value)[1]
        if int(k_allow) > 7 or int(k_allow) < 1:
            print("K is out of range PROGRAM STARTING FROM TOP...\n")
            get_values()
        if int(m) > 1000 or int(m) < 1:
            print("m is out of range PROGRAM STARTING FROM TOP...\n")
            get_values()

        for i in range(0, int(k_allow)):
            ith_value = input()
            found = re.findall("\d+", ith_value)
            for i in found:
                if int(i) > 10 ** 9 or int(i) < 1:
                    print("Entered number is out of range PROGRAM STARTING FROM TOP...")
                    get_values()
            for j in range(0, len(found)):
                ith[j] = int(found[j])
            k.append(ith)
            ith = [None, None, None, None, None, None, None]

        dic = {
            "m": int(m),
            "k": k
        }

        return dic

    except IndexError:
        print("Out of range only 7 number can be written PROGRAM STARTING FROM TOP...")
        get_values()


def maximize():
    dic = get_values()
    sum = 0
    result = None
    for i in range(0, len(dic["k"])):
        while True:
            rand = random.randrange(0, 7, 1)
            if dic["k"][i][rand]:
                break
        sum += dic["k"][i][rand] ** 2

    result = sum % dic["m"]

    print("Result is: {}".format(result))


maximize()
