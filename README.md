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


## 2019.09.21-25
### Python - zasady języka
1. Ogólnie wykonuje polecenia w kolejności ich zapisania
2. Obowiązują zasady kolejności wykonywania działań
3. Wartość x zapisana jako ostania jest nadrzędna ("kasuje" pozostałe wczesniej zdefiniowane wartości x)  
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

4. Separator dziesiętny: domyślnie kropka - jeśli chcę przecinek???
5. Kolejność wykonywania kodu: od najniższego poziomu
        > print(type(x))
        > najpierw "type" a potem "print"
  
6. Operatory porównania (ang. comparison operators)
    - równości: ==
    - nierówności: !=
    - większości: >
    - mniejszości: <  
    - więsze lub równe: >=  
    - mniejsze lub równe: <=  
      
INNE ZNAKI    
    - przypisania: =
    - "to" :) - na końcu warunku: :
  
7. Stringi
    - stringów nie można odejmować i dzielić :)
    - stringi można dodawać i mnożyć :)  
        x = "Hello world"  
        x = x + " Yay"  

        x = "Hello world " * 2  
  
8. Funkcja input
    - x = input()
    - Program czeka na wpisanie wartości
    - Wszystko traktuje jako ciąg znaków string (nawet liczby)
  
9. !!!! zapis      x = x + 2      oznacza to samo co      x += 2
  
10. Funkcja int 
    - konwersja string do int
    - zakomunikuje błąd, jeśli wpiszemy coś innego (np. Anna; 10,5; 10.5) niż liczbę całkowitą przy następującym kodzie:  
        x = input()  
        x = int(x)  
        x += 2  
        print(x)  
        print(type(x))  
  
11. Funkcja float 
    - konwersja string do float
    - można wpisać jako x: liczbę całkowitą lub niecałkowitą  
        x = input()  
        x = float(x)  
        x += 2  
        print(x)  
        print(type(x))  
        
     - Jak zmienić separator dziesiętny? W funkcji input trzeba wpisywać liczby zmiennoprzecinkowe z kropką jako separatorem dziesiętnym. Czy i jak można zmienić ustawienia, żeby można było wpisać liczbę zmiennoprzecinkową z przecinkiem?  
     ODP. Nie można pisać liczb zmiennoprzecinkowych z przecinkienm w programowaniu, bo takie rozwiązanie, generowałoby dużo błędów. Istnieją przypadki dla których musisz rozdzielić poszczególnie przekazywane parametry i dla takich momentów jest zarezerwowany przecinek, np. print("parametr1", "parametr2"). Raczej w każdym języku tak jest. Zwyczajnie przecinek jest zbyt potrzebny do innych operacji, a kropka jest czytelniejsza w zapisie liczb :slightly_smiling_face:
Nie mniej, oczywiście da się uwzględnić, że użytkownik będzie chciał użyć przecinka zamiast kropki.
W takim wypadku trzeba by było użyć coś w stylu: float(zmienna.replace(',','.')) Dzięki temu jeżeli w zmiennej jest np. '3,2', to program to zmieni na '3.2' i prze konwertuje na float.

12. Wypisywanie fragmentów stringów
    - wypisując pierwszy znak stringa, trzeba wpisać 0 [zero]
    - wypisując więcej znaków, zaczynać od 1 [jedynki], np. [1:3]
  
    - Co to robi? Na pewno nie wypisuje wyrazu przy tym zapisie. ODP. Prowadzący kurs blędnie określił, co się stanie. Funkcja wypisuje ZNAK a nie wyraz.  
        x = "Ala ma kota a kot ma Alę :)"  
        y = x[-2]  
        print(y)  
        print(type(x))  
  
13. Python "widzi" **wcięcia wierszy** i od tego może zależeć, czy coć wykona czy nie
    - "Gotowe" zostanie wypisane niezależnie od tego, czy x będzie się równać 5!!!!  
        x = 10  
        if x == 5:  
            print("Zgadza się")  
            print("Tak")  

        print("Gotowe")  
  

14. **bool a string**  
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
  
  
  
15. WHY????? W warunkach najpierw podaje się prawdę?  
        ODP. Operacje zaraz po if-ie (z wcieciem do if-a) wykonują się, jeżeli warunek zwraca True!
    KOD 3  
    if 0:  
        print("Zgadza się")  
    else:  
        print("Nie zgadza się")  

    RUN 3  
    Nie zgadza się  
  
  
16. [LISTY]  
    KOD 4  
    Produkty = []  
    print(Produkty)  
    print(type(Produkty))  
    RUN 4  
    []  
    <class 'list'>  
      
    - WAŻNE! Python rozróżnia wielkość liter.
    - wypisując pierwszy element listy, trzeba wpsać 0 [zero], kolejny 1 itd.
    - wypisując element, licząc od końca, to -1

    - funkcje
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
  
  
17. (TUPLE)
    - listy [] można edytować a tupli () nie - tuple są "szybsze" :)  
  
18. {SŁOWNIKI}  
    - (dict) - zestaw kluczy i wartości
        > person = {"wiek": 20, "imię": "Ania", "nazwisko": "Kowalska"}  
          print(person["wiek"])
  
    - WAŻNE rodzaje nawiasów:    print(person["wiek"])    ale    print(person.get("wzrost", 25))
  
    - funkcje
            - clear - usuwanie całości
            - copy - kopiowanie
            - get - po przecinku można dać wartość, którą ma zwrócić, jeżeli nie znajdzie danego elementu
            - keys - 
            - values - lista wartości
            - items
  
  
19. PĘTLE
    - kod, który wykonuje się więcej niż jeden raz
    - iteracja (ang. iteration) – czynność powtarzania tej samej operacji w pętli z góry określoną liczbę razy lub aż do spełnienia określonego warunku. Mianem iteracji określa się także operacje wykonywane wewnątrz takiej pętli.
  
    - **while** 
        - wykonuje się, dopóki nie zostanie spełniony określony warunek
        - definiowanie zminnej, która przerywa pętlę

        - Niekończąca się historia - warunek nigdy nie zostanie spełniony  
            i = 0  
            while i < 10:  
                print(i)  

        - Poniższa pętla za każdym razem po zakończeniu cyklu na nowo definiuje pojęcie sumy. Początek cyklu zaczyna się od sumy równej ostatniemu wynikowi działania.  
            suma = 0  
            while True:  
                print("Wpisz liczbę")  
                x = input()  
                suma += int(x)  
                print(suma)  

        - Wynikiem poniższej pętli jest błąd. Lista zawiera mniej niż 10 el.?  
            lista = ["a","b","c","d"]  
            i = 0  
            while i < 10:  
                print(lista[i])  
                i +=1  


    - **for**
        - Jaka jest definicja "litery", "fruit" dla Pythona??  
                lista = ["a","b","c","d","e","f","g","h","i","j","k"]  
                for litera in lista:  
                    print(litera)  
                
                fruits = ['apple', 'orange', 'pear', 'banana', 'apple']  
                for fruit in fruits:  
                    print(fruit)  
  
    - funkcja **range**
        - generuje listę wg zdefiniowanych argumentów
        - maksymalnie można zdefiniować 3 argumenty
        - for i in range(10): - wygeneruje listę od 0 do 9 (zero liczy się jako pierwsza w kolejnosci cyfra)
        - for i in range(5,10): - wygeneruje listę od 5 do 9 (dlaczego od 5 a nie od 4???)
        - for i in range(5,10,2): - wygeneruje listę od 5 do 9, ale cyfry będą się zwiększały o 2 (the same why??)
        
   - **if**
        -     jesli po "if" jest tylko jedna funkcja, można ją umiescić w tej samej linijce, np.
    if fruit == "orange": continue  
    if fruit == "banana": break  
     
   - funkcja **enumerate**
        - loop control statements - terminy służące do przerwania pętli  
                fruits = ['apple', 'orange', 'pear', 'banana', 'apple']  
                for i, fruit in enumerate(fruits):  
                    if i == 3:  
                        break  
                    print(i)  
                    print(fruit)  
        
    - funkcja **format**
                x = "Hello {} {}"
                y = x.format("world", 5.5)
                print(x)
                print(y)
                
    - to nie jest pętla - sprawdza jedynie, czy coś jest na liście!!  
        if "orange" in fruits:
            print("znaleziono")
        else:
            print("nie znaleziono")
            
    - operatory logiczne (ang. logical operators)  
        - and
        - or
        - and not
        
  
#### Klasy zmiennych
    Liczbowe
    - integer (int) - liczba całkowita
    - float (complex) - zmiennoprzecinkowe  
            Python automatycznie dokonuje konwersji podczas wykonywania dzielenia: integer > float

    - string (str) - ciąg znaków
    - boolean (bool) - prawda/fałsz (typ logiczny)
    - list - lista
    - dictionary (dict) - słownik
    - dict_keys


- [GIT - formatowanie tekstu](https://github.com/zozlak/MLAK/wiki/1.5.1-Formatowanie-tekstu)
- [spoko rozpisane są tutaj podstawy EN](https://www.programiz.com/python-programming)


Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:

1. and	- A logical operator
2. as	- To create an alias
3. assert	- For debugging
4. break	- To break out of a loop
5. class	- To define a class
6. continue	- To continue to the next iteration of a loop
7. def	- To define a function
8. del	- To delete an object
9. elif	- Used in conditional statements, same as else if
10. else	- Used in conditional statements
11. except	- Used with exceptions, what to do when an exception occurs
12. False	- Boolean value, result of comparison operations
13. finally	- Used with exceptions, a block of code that will be executed no matter if there is an exception or not
14. for	- To create a for loop
15. from	- To import specific parts of a module
16. global	- To declare a global variable
17. if	- To make a conditional statement
18. import	- To import a module
19. in	- To check if a value is present in a list, tuple, etc.
20. is	- To test if two variables are equal
21. lambda	- To create an anonymous function
22. None	- Represents a null value
23. nonlocal	- To declare a non-local variable
24. not	- A logical operator
25. or	- A logical operator
26. pass	- A null statement, a statement that will do nothing
27. raise	- To raise an exception
28. return	- To exit a function and return a value
29. True	- Boolean value, result of comparison operations
30. try	- To make a try...except statement
31. while	- To create a while loop
32. with	- Used to simplify exception handling
33. yield	- To end a function, returns a generator



- [Python Keywords](https://www.w3schools.com/python/python_ref_keywords.asp) - w3schools
- [Installing GitBash on Windows 10](https://liveoncode.com/installing-gitbash-on-windows-10/) - Live on Code
- [Git Bash, Bash Basics](https://www.youtube.com/watch?v=oQc-2gsjgDg) - Mario Kaack
- [Jak dodać pliki do repozytorium na GitHubie?](https://www.youtube.com/watch?v=RFihMCC4f_s) - Bede Programistka
- [Podstawy Pythona](https://tutorial.djangogirls.org/pl/python_introduction/) - Django
- [Python Tutorial for Beginners [Full Course] 2019](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=1438s) - EN, 6hrs


## 2019.10.17  
#8CodiblyTechTalks - JS  
18:00  
Codibly Headquarters, (Długa Skład), Długa 72, Kraków  
1. Managing user permissions in React applications (PL)  
    Dawid Hen - Senior Frontend Developer  
2. Advanced React Hooks concepts (PL)  
    Dawid Jaracz - Frontend Developer  
3. Refactoring overgrown React components (PL)  
    Łukasz Ostrowski - Frontend Developer  
    
## 2019.10.20
1. Kurs Python 3 [#12] Data i czas(https://www.youtube.com/watch?v=s7R5KThCbGo)  
2. Perl(https://pl.wikipedia.org/wiki/Perl)  
– interpretowany, dynamiczny język programowania wysokiego poziomu autorstwa Larry’ego Walla

## 2019.10.21
1. Kurs Python 3 [#12] Data i czas(https://www.youtube.com/watch?v=s7R5KThCbGo)  
2. Slack(https://www.itworld.com/article/3446881/slack-rolls-out-new-salesforce-integrations-launches-workflow-builder.html) rolls out new Salesforce integrations, launches Workflow Builder
