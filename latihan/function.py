# len()
nama = 'lorem ipsum'
print("Panjang string", len(nama))
# filter
umur = [5, 12, 17, 18, 24, 32]


def checkNumber(x):

    if x >= 18:
        return False
    else:
        return True


dewasa = filter(checkNumber, umur)
print("kategori dewasa : ")
for x in dewasa:
    print(x)
