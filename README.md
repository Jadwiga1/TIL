# TIL
> Today I Learned

A collection of links and concise write-ups on small things I learn day to day across a variety of languages and technologies.

## Day 1

Todo - #1

Todo - #2

- [5 Reasons Why You're NOT Becoming a Programmer](https://www.youtube.com/watch?v=HJtNUW6kk1E)
- [What do programmers actually do?](https://www.youtube.com/watch?v=FVdQETvHBoE) 
- [Front end vs Back end | Blonde Dictionary explanation](https://www.youtube.com/watch?v=NlpK0-TLrjw)
- [What is Git and Github? Source Control — Coding For Beginners](https://www.youtube.com/watch?v=3bchX_7ANQc)
- [How to create a repository on github](https://help.github.com/en/articles/create-a-repo)
- [Praktyczny kurs Git - #1/12 Czym jest Git?](https://www.youtube.com/watch?v=D6EI7EbEN4Q&t=19s)


## Day 2
- Python - download
- PyCharm - download
- [Kurs Python 3 [#1] Instalacja środowiska, PyCharm](https://www.youtube.com/watch?v=NN5Pht2FRWs)

IDE - Integrated Development Environment (Zintegrowane środowisko programistyczne)


## Day 3
- [POIT 009: Programowanie frontendu aplikacji webowych - Krzysztof Kempiński](https://www.youtube.com/watch?v=vtn7UhAJrDU)


## Day 4
- Słownik Python (https://python101.readthedocs.io/pl/latest/podstawy/gloss_python.html)

## 2019.09.06-15
KSIĄŻKA
Mistrz czystego kodu. Kodeks postepowania profesjonalnych programistów (ang. The Clean Coder: A Code of Conduct for Professional Programmers
Robert C. Martin
Helion S.A. 2013 (ISBN: Mobi: 978-83-246-7536-4)

1. Etyka zawodowa
- styczeń 1986 roku - rozbicie promu kosmicznego Challenger
2. Object Mentor
- firma skupiająca doswiadczonych inżynierów oprogramowania i managerów z tej branży (założycielem i prezes jest "Wujek Bob")
3. Przykładowe
- COBOL, FORTRAN, BAL, PDP-8, PDP-11, C, C++, Java, Ruby, Smalltalk, asembler, FitNesse, .NET, Lips, Clojure
4. Profesjonalizm, odpowiedzialność
5. Uszkodzenie funkcji i/lub struktury kodu
- funkcja - testy
- struktura - elastyczna struktura kodu - Zginać kod! - BEZLITOSNA REFAKTORYZACJA ("reguła skauta") - "dany moduł zawsze pozostaw czystszy, niż go zostawiłeś"
6. Testowanie
- ma obejmować cały kod (100% :)
- testy jednostkowe
- testy akceptacyjne
7. TDD (Test Driven Development - programowanie sterowane testami)
8. Dokształcanie
- różnica między maszynami stanu Mealy'ego i Moora; procedura quicksort; analiza transformacji; funkcjonalna dekompozycja za pomocą diagramu przepływu danych; wędrowne dane (ang. tramp data); conascence; tablice Parnasa; 
- wzorce projektowe (24 wzorce z książki GOF; wzorce z książki POSA)
- zasady projektowania (zasady SOLID)
- metody: metodologia XP, Scrum, Lean, Kanban, wodospadu, analizy strukturalnej, projektowania strukturalnego
- dziedziny: technika TDD, projektowania obiektowego, programowania strukkturalnego, ciągłej integracji, programowania w parach
- artefakty: UML, DFD, wykresy struktur, sieć Petriego, diagramy i tabele przejść stanów, diagramy przepływu, tabele decyzji
- współpraca z innymi programistami
- uczenie innych
9. Ćwicz jak muzyk (kata)
- Gra w kręgle (Bowling game); Czynnik pierwszy (Prime factor)
- KATA - prosty problem programistyczny
10. Poznaj specyfikę dziedziny, dla której tworzysz kod (np. turystyka, medycyna)
11. Pokora, asertywność, kompromis, komunikacja w zespole
12. Próbowanie :D - deklaracje
13. Wymagania klienta - możliwość realizacji 
14. Prosta aplikacja ;)
15. Bohater dnia codziennego - dyscyplina
16. Elektroniczny recepcjonicta (Bob - wspóltwórca)
17. Język zobowiazań
- Książka: "Powiedz. Zamierzaj. Zrób." Roy Osherove
- Słowa kluczowe świadczące o BRAKu zobowiązania:
-- trzeba by, musiałby, mam nadzieję, dobrze by było, powinniśmy
- Praawidłowe sformułowanie zobowiązania:
-- Ja (...) to zrobię do (...)
    > "Ja (imię Pana Młodego) biorę Ciebie (imię Panny Młodej) za żonę i ślubuję Ci miłość, wierność i uczciwość małżeńską oraz to, że Cię nie opuszczę aż do śmierci."]
18. Wykrywanie własnych błędów ("pisanie na klawiaturze")
19. "chodzi [...] o takie ukształtowanie kodu, żeby sam ujawniał Twoje zamiary"
20. Higiena pracy
- nie pisz kodu, kiedy jesteś zmęczony
- dyscyplina
- rozwiąż/odsuń zmartwienia ["Hakuna matata"]
- koncentracja
- stan hiperproduktywności (ang. flow) - wg  niektórych programistów "strefa" (ang. zone)
    > "Kod napisany w strefie na pewno powstaje szybciej, ale później treba go częściej poprawiać."
 
    > Strefa jest stanem niekomunikatywnym.
 
    > Programowanie w parach właściwie wyklucza wejście w strefę (praca w parach wymaga ciągłej i intensywnej komunikacji."
- muzyka
- przerwy
- kreatywne zajęcia
- kodowanie to maraton a nie sprint
- prysznic
- jazda do domu
21. Spóźnienia
- wczesne wykrywanie i informowanie
22. Gotowy produkt
- co to znaczy?
23. Wzajemna pomoc
24. Mentor
25. GOTO vs. TDD
26. TDD - 3 zasady


# 2019.09.21
1. Python - zasady języka
- ogólnie wykonuje polecenia w kolejności ich zapisania
- obowiązują zasady kolejności wykonywania działań
- wartość x zapisana jako ostania jest nadrzędna ("kasuje" pozostałe wczesniej zdefiniowane wartości x)
KOD 1
x = 10
print(x)
x = 15
print(x)
x = x + 2
print(x)
x = x + 2 * 2
print(x)

RUN 1
10
15
17
21

- separator dziesiętny: domyślnie kropka - jeśli chcę przecinek???
- kolejność wykonywania kodu: od najniższego poziomu
        > print(type(x))
        > najpierw "type" a potem "print"

ZNAKI
- przypisania: =
- równości: ==
- nierówności: !=
- "to" :) - na końcu warunku: :
- większości: >
- mniejszości: <
        
- stringów nie można odejmować i dzielić :)
- stringi można dodawać i mnożyć :)
x = "Hello world"
x = x + " Yay"

x = "Hello world " * 2

- funkcja "input"
x = input()
Program czeka na wpisanie wartości
wszytsko traktuje jako ciąg znaków (nawet liczby)

- !!!! zapis 
x = x + 2
oznacza to samo co
x += 2


- funkcja int - konwersja string do int
zakomunikuje błąd, jeśli wpiszemy cos innego (np. Anna; 10,5; 10.5) niż liczbę całkowitą przy następującym kodzie:
x = input()
x = int(x)
x += 2
print(x)
print(type(x))


- funkcja float - konwersja string do float
można wpisać jako x: liczbę całkowitą lub niecałkowitą
x = input()
x = float(x)
x += 2
print(x)
print(type(x))

- wypisywanie fragmentów stringów
> wypisując pierwszy znak stringa, trzeba wpsać 0 [zero]
> wypisując więcej znaków, zaczynać od 1 [jedynki], np. [1:3]

- Co to robi??? Na pewno nie wypisuje wyrazu przy tym zapisie.
x = "Ala ma kota a kot ma Alę :)"
y = x[-2]
print(y)
print(type(x))


- "Gotowe" zostanie wypisane niezależnie od tego, czy x będzie się równać 5!!!!
x = 10
if x == 5:
    print("Zgadza się")
    print("Tak")

print("Gotowe")


- Python "widzi" wcięcia wierszy i od tego może zależeć, czy coć wykona lub nie

- bool a string
KOD 2
x = "daj"
print(type(x))

if bool(x):
    print("Zgadza się")
else:
    print("Nie zgadza się")

print(type(x))

print("Gotowe")


RUN 2
<class 'str'>
Zgadza się
<class 'str'>
Gotowe



- WHY????? W warunkach najpierw podaje się prawdę?
KOD 3
if 0:
    print("Zgadza się")
else:
    print("Nie zgadza się")
    
RUN 3
Nie zgadza się




- lista
KOD 4
Produkty = []
print(Produkty)
print(type(Produkty))
RUN 4
[]
<class 'list'>
WAŻNE! Python rozróżnia wielkość liter.
> wypisując pierwszy element listy, trzeba wpsać 0 [zero], kolejny 1 itd.
> wypisując element, licząc od końca, to -1

FUNKCJE
- append - dodaje element (pojedynczy?) do listy na końcu
- clear - czyści listę
- count - liczy ile razy "mleko" pojawia się na liście
- append - można dodać inną listę
- index - podaje, na jakiej pozycji występuje dany element
- insert - można cos dodać na jakiejś pozycji
- pop - usuwanie elementu o danej pozycji, np. 1 (pamiętać, że liczy się od 0!)
- remove - usuwanie elementu o danej nazwie

KOD 5
Produkty = ["mleko","jaja","ryby","mleko"]
Produkty.remove("mleko")
print(Produkty)
RUN 5
['jaja', 'ryby', 'mleko']


- TUPLE: listy [] można edytować a tupli () nie - tuple są "szybsze" :)

- SŁOWNIK {} (dict) - zestaw kluczy i wartości
> person = {"wiek": 20, "imię": "Ania", "nazwisko": "Kowalska"}
print(person["wiek"])

WAŻNE rodzaje nawiasów:
print(person["wiek"]) 
ale
print(person.get("wzrost", 25))


FUNKCJE
- clear - usuwanie całości
- copy - kopiowanie
- get - po przecinku można dać wartość, którą ma zwrócić, jeżeli nie znajdzie danego elementu
- keys - 
- values - lista wartości
- items

2. Klasy zmiennych
Liczbowe
- integer (int) - liczba całkowita
- float (complex) - zmiennoprzecinkowe
        Python automatycznie dokonuje konwersji podczas wykonywania dzielenia: integer > float

- string (str) - ciąg znaków
- boolean (bool) - prawda/fałsz (typ logiczny)
- list - lista
- dictionary (dict) - słownik
- dict_keys




