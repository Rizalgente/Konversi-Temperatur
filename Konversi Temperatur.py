print("======PROGRAM KONVERSI SUHU======\n".center(55))
print("1. Celcius\n2. Reamur\n3. Fahrenheit\n4. Kelvin\n")

while True:
    suhu = int(input("Masukan Nomor Temperatur Yang Akan Di Konversi:\n"))
    if suhu == 1:
     print("====KONVERSI SUHU CELCIUS====\n")
     celcius = float(input("Masukan suhu dalam Celcius: "))
     print("suhu yang anda masukan adalah: {} Celcius\n".format(celcius))

     print("====HASIL DARI KONVERSI====\n")

     reamur = (4 / 5) * celcius
     print('suhu Reamur adalah:', reamur, "Reamur")

     fahrenheit = (9 / 5) * celcius + 32
     print('suhu Fahrenheit adalah:', fahrenheit, "Fahrenheit")

     kelvin = celcius + 273
     print('suhu Kelvin adalah;', kelvin, "Kelvin\n")
    elif suhu == 2:
        print("====KONVERSI SUHU REAMUR====\n")
        reamur = float(input("Masukan suhu dalam Reamur: "))
        print("suhu yang anda masukan adalah: {} Reamur\n".format(reamur))


        print("====HASIL DARI KONVERSI====\n")

        celcius = (5/4) * reamur
        print('suhu Celcius adalah:', celcius, "celcius")

        fahrenheit = 9 / 4 * (reamur + 32)
        print('suhu Fahrenheit adalah:', fahrenheit, "Fahrenheit")

        kelvin = 5 / 4 * reamur + 273
        print('suhu Kelvin adalah;', kelvin + 273, "Kelvin\n")

    elif suhu == 3:
        print("====KONVERSI SUHU FAHRENHEIT====\n")
        fahrenheit = float(input("Masukan suhu dalam Fahrenheit: "))
        print("suhu yang anda masukan adalah: {} Fahrenheit\n".format(fahrenheit))

        print("====HASIL DARI KONVERSI====")

        celcius = 5/9 * (fahrenheit - 32)
        print('suhu Celcius adalah:', celcius, "celcius")

        reamur = 4/9 * (fahrenheit - 32)
        print('suhu Reamur adalah:', fahrenheit, "Reamur")

        kelvin = 5 / 9 * (fahrenheit - 32)
        print('suhu Kelvin adalah;', kelvin + 273, "Kelvin\n")
    elif suhu == 4:
        print("====KONVERSI SUHU KELVIN====\n")

        kelvin = float(input("Masukan suhu dalam Kelvin: "))
        print("suhu yang anda masukan adalah: {} Kelvin\n".format(kelvin))

        print("====HASIL DARI KONVERSI====\n")

        celcius = kelvin - 273
        print('suhu Celcius adalah:', celcius, "celcius")

        reamur = 4 / 5 * (kelvin - 273)
        print('suhu Reamur adalah:', reamur, "Reamur")

        fahrenheit = kelvin - 273
        print('suhu Fahrenheit adalah:', (9 / 5) * fahrenheit + 32, "fahrenheit\n")
        continue
    else:
        print("Input Yang Tersedia Hanya 1 Sampai 4")
