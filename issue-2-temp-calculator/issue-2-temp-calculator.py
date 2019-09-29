print("KALKULATOR TEMPERATUR")
print("Wybierz rodzaj konwersji:")
print("1 - stopnie Celsjusza na Farenheita")
print("2 - stopnie Farenheita na Celsjusza")

type_conversion = input("Wpisz interesujący cię rodzaj konwersji (oznaczenie liczbowe): ")

while type_conversion != "1" or type_conversion != "2":
    type_conversion = input("Podana konwersja nie istnieje. Wybierz konwersję z listy: ")
    if type_conversion == "1" or type_conversion == "2":
        break

temperature_value = float(input("Wpisz wartość: "))

if type_conversion == "1":
    degrees_farenheit = temperature_value * 1.8 + 32
    print("Odpowiedź: {}°C to {}°F".format(temperature_value, degrees_farenheit))

elif type_conversion == "2":
    degrees_celsius = (temperature_value - 32) / 1.8
    print("Odpowiedź: {}°F to {}°C".format(temperature_value, degrees_celsius))
