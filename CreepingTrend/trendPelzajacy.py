from CreepingTrend import szacowanieKLiniowychModeliTendencjiRozwojowej, atrybutWygladzania

n=15
l=atrybutWygladzania.l

SzacunekK = szacowanieKLiniowychModeliTendencjiRozwojowej.SzacunekIlosciModeli(n,l)
print(SzacunekK)

TeoretycznaWartosc = szacowanieKLiniowychModeliTendencjiRozwojowej.TeoretycznaWartoscZmiennejPrognozowanej(1,1)
print(TeoretycznaWartosc)

