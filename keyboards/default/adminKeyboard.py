from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.regionData import tashkent, Qoraqalpogiston, xorazm, navoiy, buxoro, samarqand, qashqadaryo, surxondaryo, \
    jizzax, sirdaryo, toshvil, namangan, fargona, andijon, viloyat

saqlash = ReplyKeyboardMarkup(
    keyboard=[
        ["Save data✅","❌Cancel❌"]
    ],
    resize_keyboard=True
)

adminButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send Users"),
            KeyboardButton(text="Statistic")
        ],
        [
         KeyboardButton(text="🔙exit")
         ]
    ],
    resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙ortga")
        ]
    ],
    resize_keyboard=True
)

bekor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bekor Qilish\取消")
        ]
    ],
    resize_keyboard=True
)

tugatish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rasm yuborishni yakunlash✅ 完成上傳✅")
        ]
    ],
    resize_keyboard=True
)

postButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏡 Arenda\租赁"),
            KeyboardButton(text="🏘 Kunlik\日租")
        ],
        [
            KeyboardButton(text="🏠 Sotish\出售")
        ],
        [KeyboardButton(text="🔙exit")]
    ],
    resize_keyboard=True
)

placeButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="KV"),
            KeyboardButton(text="UY"),
            KeyboardButton(text="YER")
        ],
        [
            KeyboardButton(text="OFFICE"),
            KeyboardButton(text="Magazine")
        ],
        [
            KeyboardButton(text="BOZOR"),
            KeyboardButton(text="ZAVOD")
        ],
        [
            KeyboardButton(text="🔙 Back")
        ]
    ],
    resize_keyboard=True
)

keys = []
for item in tashkent:
    btn = KeyboardButton(text=item)
    keys.append(btn)
regionButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10]
        ],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in Qoraqalpogiston:
    btn = KeyboardButton(text=item)
    keys.append(btn)
qoraqalpoqBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10], keys[11]
        ],
        [keys[12], keys[13]],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in xorazm:
    btn = KeyboardButton(text=item)
    keys.append(btn)
xorazmBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10]
        ],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in navoiy:
    btn = KeyboardButton(text=item)
    keys.append(btn)
navoiyBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7]
        ],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in buxoro:
    btn = KeyboardButton(text=item)
    keys.append(btn)
buxoroBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10]
        ],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in samarqand:
    btn = KeyboardButton(text=item)
    keys.append(btn)
samarqandBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10], keys[11]
        ],
        [keys[12], keys[13]],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in qashqadaryo:
    btn = KeyboardButton(text=item)
    keys.append(btn)
qashqadaryoBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10], keys[11]
        ],
        [keys[12], keys[13]],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in surxondaryo:
    btn = KeyboardButton(text=item)
    keys.append(btn)
surxondaryoBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10], keys[11]
        ],
        [keys[12]],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in jizzax:
    btn = KeyboardButton(text=item)
    keys.append(btn)
jizzaxBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10], keys[11]
        ],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in sirdaryo:
    btn = KeyboardButton(text=item)
    keys.append(btn)
sirdaryoBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9],
        ],
        [ "🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in toshvil:
    btn = KeyboardButton(text=item)
    keys.append(btn)
toshvilBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10], keys[11]
        ],
        [keys[12], keys[13]],

        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)
keys = []
for item in namangan:
    btn = KeyboardButton(text=item)
    keys.append(btn)
namanganBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10]
        ],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)
keys = []
for item in fargona:
    btn = KeyboardButton(text=item)
    keys.append(btn)
fargonaBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10], keys[11]
        ],
        [keys[12], keys[13], keys[14]],
        ["🏛 Bosh menu"]
    ],
    resize_keyboard=True
)
keys = []
for item in andijon:
    btn = KeyboardButton(text=item)
    keys.append(btn)
andijonBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10], keys[11]
        ],
        [keys[12], keys[13]],
        [ "🏛 Bosh menu"]
    ],
    resize_keyboard=True
)

keys = []
for item in viloyat:
    btn = KeyboardButton(text=item)
    keys.append(btn)
viloyatBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            keys[0], keys[1], keys[2]
        ],
        [
            keys[3], keys[4], keys[5]
        ],
        [
            keys[6], keys[7], keys[8]
        ],
        [
            keys[9], keys[10], keys[11]
        ],
        [keys[12], keys[13]],
        ["🔙 Back"]
    ],
    resize_keyboard=True
)
