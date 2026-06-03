from adress import Address
from Mail import Mailing

t_adress = Address("123456", "Звездный г", "Млечная ул", "7 д", "кв 1")
f_adress = Address("789456", "Болото с", "Грустный пер", "13 д", "кв 4")

my_mail = Mailing(t_adress, f_adress, 1200, "ab-27")

print(my_mail)