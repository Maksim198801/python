import re

def isEqual(s1, s2):
    if "*" not in s2:
        return s1 == s2
    else:
        return re.sub("[\*]*", '*', s2)



if __name__ == '__main__':
    s1, s2 = list(map(str, input().split()))
    print(isEqual(s1, s2))