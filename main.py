"""
Bankomat Programmasi

Bankomat nima qiladi?
1. Pul yechib beradi
2. Kartadan-kartaga pul o'tkazish
3. Balansni ko'rib berish
4. Paynet (click)
"""


def raqam_sorash(xabarnoma, raqamlar_soni):
    while True:
        karta = input(f"{xabarnoma} [{'0'*raqamlar_soni}]: ")
        if len(karta.strip().lstrip('0')) != raqamlar_soni:
            continue
        return karta.strip()

# TODO: Kartani qabul qilish
def kartani_qabul_qilish():
    print("Kartani tiqing")
    return raqam_sorash("Karta raqami", 1)

# TODO: Ko'dni kiriting
def parol_sorash():
    print("Parol kiriting")
    return raqam_sorash("Parol", 4)

# TODO: Menyu
# TODO: Balans malumotlarini olish
# TODO: Pulni yechib olish
# TODO: Pulni chiqarib berish
# TODO: Pul o'tkazmasi


def bankomat():
    pass


kartani_qabul_qilish()
parol_sorash()
