from CreepingTrend import trendPelzajacy


def SzacunekIlosciModeli(n,l):
    k = 0
    k = n-l+1
    return k

def TeoretycznaWartoscZmiennejPrognozowanej(a,b):
    a = 2
    b = 2
    l=5
    i = 1
    t = 1
    while i<trendPelzajacy.SzacunekK and i<=t<=l+i-1:
        wynik= a+b*t
        i+=1
        t+=1
        print(wynik)
  #  return wynik
