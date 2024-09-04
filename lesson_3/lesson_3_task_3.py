from Address import Address
from Mailing import Mailing

to_ad = Address('238863', 'Астрахань', 'Зеленгинская', '15', '22')

from_ad = Address('778873', 'п-о Крым', 'Астраханская', '27', '11')

Mailing = Mailing(to_ad, from_ad, '15000', '000120030')

print(f'отправление {Mailing.track} из {Mailing.to_ad} в {Mailing.from_ad}'
      f' Cтоимость {Mailing.cost} рублей.')
