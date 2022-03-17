jsons = [
    {
        "holderName": "Вячеслав Александрович",
        "holderPhone": "0003",
        "equipmentTitle": "Ракетка",
        "equipmentCount": 2
    },
    {
        "holderName": "Альберт Андреевич",
        "holderPhone": "0001",
        "equipmentTitle": "Мяч",
        "equipmentCount": 3
    },
    {
        "holderName": "Вячеслав Александрович",
        "holderPhone": "0003",
        "equipmentTitle": "Палатка",
        "equipmentCount": 6
    },
    {
        "holderName": "Альберт Андреевич",
        "holderPhone": "0001",
        "equipmentTitle": "Удочка",
        "equipmentCount": 2
    },
    {
        "holderName": "Иван Вячеславович",
        "holderPhone": "0002",
        "equipmentTitle": "Мангал",
        "equipmentCount": 1
    },
    {
        "holderName": "Альберт Андреевич",
        "holderPhone": "0001",
        "equipmentTitle": "Спальник",
        "equipmentCount": 5
    },
    {
        "holderName": "Иван Вячеславович",
        "holderPhone": "0002",
        "equipmentTitle": "Рюкзак",
        "equipmentCount": 10
    },
    {
        "holderName": "Иван Вячеславович",
        "holderPhone": "0002",
        "equipmentTitle": "Дождевик",
        "equipmentCount": 10
    },
    {
        "holderName": "Вячеслав Александрович",
        "holderPhone": "0003",
        "equipmentTitle": "Компас",
        "equipmentCount": 1
    },
    {
        "holderName": "Альберт Андреевич",
        "holderPhone": "0001",
        "equipmentTitle": "Термос",
        "equipmentCount": 4
    }
]

def new_class(class_name: str):

    def constructor(self, attrs: dict):
        for key in attrs.keys():
            self.__dict__[key] = attrs[key]

    return type(class_name, (object, ),  {"__init__": constructor})

# method 1
cn = "Custom"
Custom_class = new_class(cn)
new_obj = Custom_class({'a' : 1, 'b' : 2})
print(type(new_obj))
print(new_obj.a)
print(new_obj.b)

# method 2
setattr(new_obj, 'c', 5)
setattr(new_obj, 'd', 6)
print(new_obj.c)
print(new_obj.d)

Holder = new_class('Holder')
objs_from_json = [Holder(json) for json in jsons]
print(type(objs_from_json[0]))
print(objs_from_json[0])
print(objs_from_json[1].holderName)

def desearialize_manual(jsons):
    def add_item(item, items: list, key):
        if len(items):
            for i in items:
                if i[key] == item[key]:
                    break
            else:
                items.append(item)
        else:
            items.append(item)
        return items

    holder, equipment = [], []
    for json in jsons:
        holders, equipments = dict(), dict()
        for key in json.keys():
            if key.startswitch('holder'):
                holder[key]= json[key]
            else:
                equipment[key] = json[key]
        
        holders = add_item(holder, holders, 'holderPhone')
        equipments = add_item(equipment, equipments, 'equipmentTitle')

    holder_objs = [new_class('Holder')(json) for json in holders]
    equipment_objs = [new_class('equipment')(json) for json in equipments]

    return holder_objs, equipment_objs

print(desearialize_manual(jsons))