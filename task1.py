# 1st
def itoBase(n,base):
   b = len(base)
   if n < b:
      return base[n]
   else:
      return itoBase(n//b,base) + base[n%b]


if __name__ == '__main__':
    try:
        n, base = list(map(str, input().split()))
        n = int(n)
        print(itoBase(n, base))
    except Exception:
        print(Exception)

