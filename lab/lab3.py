#7.İki ölçülü A(n,m) ədədi massivinin hər bir cüt sətrindəki elementlərinin cəmini hesablayan alqoritm tərtib etməli.
def cüt_sətrlər_ümumi(n, m, A):
    cüt_sətrlər = []
    for i in range(n):
        if i % 2 == 1:  # 0-dan başlayan indekslərdə cütlərin yerini tapırıq
            sətr_ümumi = sum(A[i])
            cüt_sətrlər.append(sətr_ümumi)
    return cüt_sətrlər

# Nümunə olaraq, A matrisini təyin edirik və funksiyamızı çağırırıq
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [11,22,66],
    [1,2,3]
]
n = 6  # sətr sayı
m = 3  # sütun sayı
print(cüt_sətrlər_ümumi(n, m, A))
