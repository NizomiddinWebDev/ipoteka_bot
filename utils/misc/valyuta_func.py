import requests
from data import const_data as const


async def get_currency(lang):
    lang_name = f"CcyNm_{lang.upper()}"
    url, codes, flags, text, c = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/", ['840', '978', '643'], ["🇺🇸", "🇪🇺",
                                                                                                         "🇷🇺"], "", 0
    result = requests.get(url).json()
    for i in result:
        if i["Code"] in codes:
            text += f"{flags[c]} {i[lang_name]} = <strong>{i['Rate']}</strong>\t ({i['Diff']})\n\n"
            c += 1
    return f"{const.CURRENCY[lang]}  {i['Date']}\n\n{text}"
