from Address import Address
from Mailing import Mailing

to_ad = Address('148863', 'Астрахань', 'Зеленгинская', '15', '22')

from_ad = Address('128873', 'п-о Крым', 'Астраханская', '27', '11')

Mailing = Mailing(to_ad, from_ad, '11:00', '15 000')

print(f' отправление {Mailing.to_ad} из {Mailing.from_ad}'
                           f' в {Mailing.cost}. стоимость {Mailing.track} рублей.')