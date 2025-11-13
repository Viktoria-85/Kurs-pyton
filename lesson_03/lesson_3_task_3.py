from address import Address
from mailing import Mailing


# Создаем адреса
to_address = Address("123469", "Орёл", "Олимпийская", "29", "31")
from_address = Address("654044", "Новокузнецк", "Мира", "25", "115")

# Создаем экземпляр класса Mailing
mailing = Mailing(to_address, from_address, 325, "TRACK123456789")
#Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>,
# <дом> -<квартира>. Стоимость <стоимость> рублей.

print((f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
       f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
       f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
       f"{mailing.to_address.house}"
       f" - {mailing.to_address.apartment}. "
       f"Стоимость {mailing.cost} рублей."))