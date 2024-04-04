#7 A(n) ədədi massivinin(siyahının) elementlərinin ədədi ortasını hesablayan alqoritm tərtib etməli
def ədəd_ortasi(list):
    ədəd_sayi = len(list)
    siyahinin_cemi = sum(list)
    return siyahinin_cemi / ədəd_sayi if ədəd_sayi > 0 else None

# Siyahı daxil edilir
list = [1, 2, 3, 4, 5,8]

# Ədəd ortası hesablanır və ekrana çap edilir
print("Siyahinin ədədi ortasi:", ədəd_ortasi(list))
