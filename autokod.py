
import telebot
from telebot import types


kods_dict = {
1: "Республика Адыгея",
2: "Республика Башкортостан",
3: "Республика Бурятия",
4: "Республика Алтай",
5: "Республика Дагестан",
6: "Республика Ингушетия",
7: "Кабардино-Балкарская Республика",
8: "Республика Калмыкия",
9: "Карачаево-Черкесская Республика",
10: "Республика Карелия",
11: "Республика Коми",
12: "Республика Марий-Эл",
13: "Республика Мордовия",
14: "Республика Саха-Якутия",
15: "Республика Северная Осетия-Алания",
16: "Республика Татарстан",
17: "Республика Тува",
18: "Удмуртская Республика",
19: "Республика Хакасия",
20: "Чеченская Республика (В 2000 году все номера заменили на новые с кодом 95)",
21: "Чувашская Республика",
22: "Алтайский край",
23: "Краснодарский край",
24: "Красноярский край",
25: "Приморский край",
26: "Ставропольский край",
27: "Хабаровский край",
28: "Амурская область",
29: "Архангельская область",
30: "Астраханская область",
31: "Белгородская область",
32: "Брянская область",
33: "Владимирская область",
34: "Волгоградская область",
35: "Вологодская область",
36: "Воронежская область",
37: "Ивановская область",
38: "Иркутская область",
39: "Калининградская область",
40: "Калужская область",
41: "Камчатский край (до 2007 года — Камчатская область)",
42: "Кемеровская область",
43: "Кировская область",
44: "Костромская область",
45: "Курганская область",
46: "Курская область",
47: "Ленинградская область",
48: "Липецкая область",
49: "Магаданская область",
50: "Московская область",
51: "Мурманская область",
52: "Нижегородская область",
53: "Новгородская область",
54: "Новосибирская область",
55: "Омская область",
56: "Оренбургская область",
57: "Орловская область",
58: "Пензенская область",
59: "Пермский край (до 2005 года — Пермская область)",
60: "Псковская область",
61: "Ростовская область",
62: "Рязанская область",
63: "Самарская область",
64: "Саратовская область",
65: "Сахалинская область",
66: "Свердловская область",
67: "Смоленская область",
68: "Тамбовская область",
69: "Тверская область",
70: "Томская область",
71: "Тульская область",
72: "Тюменская область",
73: "Ульяновская область",
74: "Челябинская область",
75: "Забайкальский край (до 2008 года — Читинская область)",
76: "Ярославская область",
77: "Москва",
78: "Санкт-Петербург",
79: "Еврейская автономная область",
80: "бывший Агинский Бурятский автономный округ (с 2008 года в составе Забайкальского края)",
81: "бывший Коми-Пермяцкий автономный округ (с 2005 года в составе Пермского края)",
82: "Республика Крым (с 2014 года, до 2007 года номера выдавались в Корякском автономном округе)",
83: "Ненецкий автономный округ",
84: "бывший Таймырский автономный округ (с 2007 года в составе Красноярского края)",
85: "бывший Усть-Ордынский Бурятский автономный округ (с 2008 года в составе Иркутской области)",
86: "Ханты-Мансийский автономный округ",
87: "Чукотский автономный округ",
88: "бывший Эвенкийский автономный округ (с 2007 года в составе Красноярского края)",
89: "Ямало-Ненецкий автономный округ",
90: "Московская область (с 2001 года)",
91: "Калининградская область (код используется только на экспортных транзитных номерах)",
92: "Севастополь (с 2014 года)",
93: "Краснодарский край (с 2005 года)",
94: "Байконур (территории, находящиеся за пределами РФ)",
95: "Чеченская республика (с 2000 года)",
96: "Свердловская область (с 2006 года)",
97: "Москва (с 2002 года)",
98: "Санкт-Петербург (с 2004 года)",
99: "Москва (с 1998 года)",
102: "Республика Башкортостан (с 2006 года)",
113: "Республика Мордовия (с 2009 года)",
116: "Республика Татарстан (с 2006 года)",
121: "Чувашская Республика (с 2008 года)",
122: "Алтайский край (с 2019 года)",
123: "Краснодарский край (с 2011 года)",
124: "Красноярский край (с 2009 года)",
125: "Приморский край (с 2005 года)",
126: "Ставропольский край (с 2013 года)",
134: "Волгоградская область (с 2012 года)",
136: "Воронежская область (с 2010 года)",
138: "Иркутская область (с 2013 года)",
142: "Кемеровская область (с 2011 года)",
147: "Ленинградская область (с 2019 года)",
150: "Московская область (с 2006 года)",
152: "Нижегородская область (с 2009 года)",
154: "Новосибирская область (с 2010 года)",
156: "Оренбургская область (с 2020 года)",
159: "Пермский край (с 2007 года)",
161: "Ростовская область (с 2007 года)",
163: "Самарская область (с 2006 года)",
164: "Саратовская область (с 2005 года)",
173: "Ульяновская область (с 2007 года)",
174: "Челябинская область (с 2007 года)",
177: "Москва (с 2005 года)",
178: "Санкт-Петербург (с 2010 года)",
186: "Ханты-Мансийский автономный округ (с 2012 года)",
190: "Московская область (с 2009 года)",
193: "Краснодарский край (с 2019 года)",
196: "Свердловская область (с 2013 года)",
197: "Москва (с 2010 года)",
198: "Санкт-Петербург (с 2018 года)",
199: "Москва (с 2007 года)",
702: "Республика Башкортостан (с 2019 года)",
750: "Московская область (с 2013 года)",
716: "Республика Татарстан (с 2017 года)",
761: "Ростовская область (с 2019 года)",
763: "Самарская область (с 2017 года)",
774: "Челябинская область (с 2020 года)",
777: "Москва (с 2013 года)",
790: "Московская область (с 2020 года)",
797: "Москва (с 2020 года)",
799: "Москва (с 2017 года)",
}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    message_text = message.text.lower()
    
    #print(f"user: ({message.from_user.first_name}, {message.from_user.last_name}, {message.from_user.username}, {message.from_user.id})\ntext: {message.text}\n----")
    log = f"user: {message.from_user.first_name}, {message.from_user.last_name}, {message.from_user.username}, {message.from_user.id}\ntext: {message.text}"
    bot.send_message('356646868', log)

    if message_text == '/start' or message_text == '/help':
        bot.send_message(message.from_user.id, f'Здравствуй, {message.from_user.first_name}!\n\nВведи код региона автомобильного номера.')

    else:
        try:
            kod = int(message_text)
            bot.send_message(message.from_user.id, f'{kod} - {kods_dict[kod]}')
        except ValueError:
            bot.send_message(message.from_user.id, "Необходимо ввести число!")
        except KeyError:
            bot.send_message(message.from_user.id, "Такого кода ещё нет.")
        except:
            bot.send_message(message.from_user.id, "Ошибка. Сообщите разработчику.")
                    

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)