# Ədədi massiv əsasında faylı yaratmaq
with open('ededler.txt', 'w') as file:
    for i in range(20):
        file.write(str(i) + '\n')

# Faylın oxunması və 4<X<12 şərtinə uyğun ədədlərin yeni fayla yazılması
cem = 0
with open('ededler.txt', 'r') as file:
    with open('uygun_ededler.txt', 'w') as uygun_file:
        for line in file:
            x = int(line.strip())
            if 4 < x < 12:
                uygun_file.write(str(x) + '\n')
                cem += x

print("Uyğun ədədlər yeni fayla yazıldı.")
print("Cəm:", cem)
