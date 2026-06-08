from smartphone import Smartphone

catalog = [Smartphone("Samsung", "N123", "71234567890"),
           Smartphone("Nokia", "M6", "72345678901"),
           Smartphone("Phillipse", "Xeon", "71235678901"),
           Smartphone("Realme", "X13", "72341567809"),
           Smartphone("NoName", "A17", "71232304569")]

for item in catalog:
    print(f"{item.brand} - {item.model}. {item.number}")
