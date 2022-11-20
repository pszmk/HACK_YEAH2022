clothing_items = [
{
"name": "dress for a special occasion",
"recommendation":"Rent clothes for special occasions.",
"cathegory": "clothing",
"score": 80
},
{
"name": "chain store t-shirt",
"recommendation": "Consider wearing high-quality clothing or buying from second hand.",
"cathegory": "clothing",
"score": 50
},
{
"name": "second hand t-shirt",
"recommendation": "",
"cathegory": "clothing",
"score": 50
},
{
"name": "high quality durable t-shirt",
"recommendation":"",
"cathegory": "clothing",
"score": 100
}]

food_items = [
{
"name": "poultry",
"recommendation":"",
"cathegory": "food",
"score": 50
},
{
"name": "pork",
"recommendation":"Consider replacing it witch poultry. Poultry is the moust environmental friendly meat.",
"cathegory": "food",
"score": 40
},
{
"name": "beef",
"recommendation":"Consider replacing it with poultry. Poultry is the moust environmental friendly meat.",
"cathegory": "food",
"score": 30
},
{
"name": "bottle of water",
"recommendation":"Consider using a reusable bottle. Plastic bottles are realy envarimental unfriendly.",
"cathegory": "food",
"score": 50
},
{
"name": "mushrooms",
"recommendation":"",
"cathegory": "food",
"score": 100
},
{
"name": "bean",
"recommendation":"",
"cathegory": "food",
"score": 90
},
{
"name": "lentil",
"recommendation":"",
"cathegory": "food",
"score": 90
},
{
"name": "lupinus",
"recommendation":"",
"cathegory": "food",
"score": 90
},
{
"name": "pea",
"recommendation":"",
"cathegory": "food",
"score": 90
},
{
"name": "peanut",
"recommendation":"",
"cathegory": "food",
"score": 90
},
{
"name": "soybeans",
"recommendation":"Consider eatin pulses instead. Soybeams require a lot of water to grow.",
"cathegory": "food",
"score": 20
},
{
"name": "fish",
"recommendation":"Consider eating pulses instead. Popular fish are geting overfished.",
"cathegory": "food",
"score": 30
},
{
"name": "rice",
"recommendation":"Consider replaceing it with potatoes. Rice require a lot of water to grow.",
"cathegory": "food",
"score": 20
},
{
"name": "potato",
"recommendation":"",
"cathegory": "food",
"score": 80
},
{
"name": "banana",
"recommendation":"Consider replaycing it with apples. Bananas require a lot of water to grow.",
"cathegory": "food",
"score": 50
},
{
"name": "apple",
"recommendation":"",
"cathegory": "food",
"score": 75
},
{
"name": "peache",
"recommendation":"Consider replaicing it with pears. Peaches require a lot of water to grow.",
"cathegory": "food",
"score": 50
}]

hygene_items = [
{
"name": "plastic razor",
"recommendation": "Consider using reusable razor. Non-plastic Safety Razors can last a long time and are better for the environment.",
"cathegory": "hygene",
"score": 20
},
{
"name": "reusable razor",
"recommendation":"",
"cathegory": "hygene",
"score": 100
},
{
"name": "electric razor",
"recommendation":"",
"cathegory": "hygene",
"score": 80
},
{
"name": "plastic toothbrush",
"recommendation":"Consider using wooden toothbrush. Stay clear of products like plastic toothbrushes that will never really decompose in landfills. You can switch to biodegradable bamboo toothbrushes instead.",
"cathegory": "hygene",
"score": 30
},
{
"name": "wooden toothbrush",
"recommendation":"",
"cathegory": "hygene",
"score": 100
},
{
"name": "electric toothbrush",
"recommendation":"",
"cathegory": "hygene",
"score": 50
},
{
"name": "organic soap",
"recommendation":"",
"cathegory": "hygene",
"score": 100
},
{
"name": "regular soap",
"recommendation":"Consider using organic soap. Many commercial soaps will also contain toxic chemicals that wash down the drain and pollute the waterways and negatively affect marine life.",
"cathegory": "hygene",
"score": 50
},

{
"name": "regular shampoo in single-use bottle",
"recommendation":"Consider using organic soap or shampoo in reusable bottle. You can buy reusable tin containers to store the shampoo.",
"cathegory": "hygene",
"score": 50
},
{
"name": "regular shampoo in reusable bottle",
"recommendation":"Consider using organic soap.",
"cathegory": "hygene",
"score": 50
},
{
"name": "organic shampoo in single-use bottle",
"recommendation":"Consider using soap in reusable bottle.",
"cathegory": "hygene",
"score": 80
},
{
"name": "organic shampoo in reusable bottle",
"recommendation":"",
"cathegory": "hygene",
"score": 100
}]


# for item in food_items:
#     print(item["name"])

y = {
"clothing":[{
"name": "buying new clothes",
"category": "clothes",
"solutions": [
{
"name": "check in database if you really need it",
"score": "90",
},
{
"name": "buy it second-hand",
"score": "100",
},
{
"name": "postpone purchase",
"score": "50",
}
]
},
{
"name": "dressing up for special occasion",
"category": "clothes",
"solutions": [
{
"name": "rent formal clothes",
"score": "80",
}
]
},
{
"name": "getting rid of old clothes",
"category": "clothes",
"solutions": [
{
"name": "sell them",
"score": "100",
},
{
"name": "give them away",
"score": "100",
},
{
"name": "use them as rags",
"score": "80",
}
]
}],
"food": [
{
"name": "food shopping",
"category": "food",
"solutions": [
{
"name": "use your own bags",
"score": "60",
}
]
},
{
"name": "drinks",
"category": "food",
"solutions": [
{
"name": "buy drinks in glass bottles",
"score": "70",
}
]
}],
"hygiene": [{
"name": "brushing teeth",
"category": "hygiene",
"solutions": [
{
"name": "use wooden toothbrush",
"score": "70",
},
{
"name": "use cup for water",
"score": "60",
},
{
"name": "use wooden toothbrush and cup for water",
"score": "100",
}
]
},
{
"name": "shaving",
"category": "hygiene",
"solutions": [
{
"name": "use safety razor",
"score": "65",
}
]
},
{
"name": "bathing",
"category": "hygiene",
"solutions": [
{
"name": "take shower",
"score": "70",
},
{
"name": "using zero waste cosmetics",
"score": "80",
},
{
"name": "take shower and use zero waste cosmetics",
"score": "90",
}
]
},
{
"name": "maquillage",
"category": "hygiene",
"solutions": [
{
"name": "use zero waste cosmetics",
"score": "80",
}
]
}]
}

print(y)
print(y['clothing'])
print(y['food'])
print(y['hygiene'])