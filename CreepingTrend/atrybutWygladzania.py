#Arbitralne ustalenie wartości okresu wygladzania l.

n = 1000  # pózniej będzie ilośc elementów (wierszy) w pliku
l = 3
czyParzysta = ""

while 1:
    try:
        if czyParzysta == "T":
            break
        czyWprowadzaszAtrybut = input("Czy chcesz podać atrybut wygładzenia? (T/N) ")
    except ValueError:
        print("Wprowadzono nie poprawną wartość")
        continue
    if czyWprowadzaszAtrybut == "T":
        while 1:
            try:
                if czyParzysta == "T":
                    break
                l = int(input("Podaj atrybut okresu wygładzania l: "))
            except ValueError:
                print("Atrybut wygładania może być tylko liczbą! Wprowadź ponownie.")
                continue

            if l<2:
                print("Atrybut wygładzania l musi byc >= 2! Wprowadź ponownie.")
                continue
            elif l > n:
                print("Atrybut wygładzania l nie może być większy niż liczba elementów próby! Wprowadź ponownie.")
                continue
            elif l%2==0:
                czyParzysta = input("Czy atrybut ma byc na pewno liczbą parzystą? (T/N) ")
                if czyParzysta == "T":
                    print("Atrybut wygładzania l = ", l)
                else:
                    continue
            else:
                print("Atrybut wygładzania l = ", l)
                break

    elif czyWprowadzaszAtrybut == "N":
        print("Atrybut wygładzania przyjął wartośc domyślną =",l)
        break
    else:
        print("Atrybut wygładania może być tylko litera T - TAK lub N - NIE! Wprowadź ponownie.")
        continue