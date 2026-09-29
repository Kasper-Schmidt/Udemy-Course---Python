new_string = input("Input a string: ")

if new_string < "hello":
    print(f"Your word {new_string} comes before hello")
else:
    print(f"{new_string} does not come before hello")


# Python sammenligner fra venstre mod højre i alfabetisk rækkefølge.
# Eksempel: new_string = "house"
# h == h
# Bogstavet "o" kommer efter "e".
# Derfor kommer "house" efter "hello".
# Alle uppercase-bogstaver kommer før lowercase-bogstaver.