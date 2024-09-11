from smartphone import smartphone

catalog = []

Myphone1 = smartphone('nokia', '5230', '+79608633947')
Myphone2 = smartphone('nokia', '6280', '+79618633948')
Myphone3 = smartphone('nokia', '5200', '+79648633949')
Myphone4 = smartphone('nokia', '5630', '+79658633941')
Myphone5 = smartphone('nokia', '5228', '+79678633942')

catalog.append(Myphone1)
catalog.append(Myphone2)
catalog.append(Myphone3)
catalog.append(Myphone4)
catalog.append(Myphone5)

for phone in catalog:
    print(f"{phone.Bphone} {phone.Mphone} {phone.Nphone}")
