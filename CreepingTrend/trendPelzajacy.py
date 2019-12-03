from CreepingTrend import szacowanieKLiniowychModeliTendencjiRozwojowej, atrybutWygladzania

n=1000
l= atrybutWygladzania.l

SzacunekK = szacowanieKLiniowychModeliTendencjiRozwojowej.SzacunekIlosciModeli(n,l)
print(SzacunekK)