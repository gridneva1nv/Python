from adress import Address
from Mail import Mailing

t_adress = Address("123456", "Звездный г", "Млечная ул", "7 д", "кв 1")
f_adress = Address("789456", "Мечта с", "Грустный пер", "13 д", "-")

my_mail = Mailing(t_adress, f_adress, 1200, "ab-27")
