
import random


import discord
from discord.ext import commands
from discord import utils
import os





Armor = ["Стеганый","Кожаный","Шкурный","Чешуйчатый","Кираса","Полулаты","Колечный","Латы", "Щит"]
Armor_Exept = ["Кираса","Полулаты","Латы","Щит"]
Weapon = ["Боевой посох","Булава","Дубинка","Кинжал","Копье","Легкий молот","Метательное копье","Палица","Ручной топор","Серп","Арбалет, легкий","Дротик","Короткий лук","Праща",
          "Алебарда","Боевая кирка","Боевой молот","Боевой топор","Глефа","Двуручный меч","Длинное копье","Длинный меч","Кнут","Короткий меч","Молот",
          "Моргенштерн","Рапира","Пика","Секира","Скимитар","Трезубец","Цеп","Сеть","Длинный лук","Вилка","Вилы","Вилка","Вилка","Вилка","Вилка","Вилка","Револьвер","Мушкет","Пиво"]
Dices = ["d2 ","d4 ","d6 ","d8 "]
Damage_Types = ["огонь","холод","кислотный","молнией","ядом","некротический","молнией","Светой"]
Cantrips = ["Брызги кислоты","Волшебная рука","Вспышка мечей","Громовой клинок","Звон по мёртвым","Иссушающий укол","Лоссо молнии","Леденящее прикосновение","Луч холода",
            "Мистический заряд","Обморожение","Огненный снаряд","Раскат Грома","Священное Пламя","Слово сияния","Терновый кнут","Шквал"]
Commands = ["!break","!chest"]

def int_roles(user: discord.Member):
    ret = []
    for i in range(0,len(user.roles)):
        ret.append(user.roles[i].id)
    return ret

def has_role(user: discord.Member, role: int):
    return  role in int_roles(user)


def item():
    out = ""

    if bool(random.randint(0,1)):
        ench = random.randint(0,3)
        out += Weapon[random.randint(0, len(Weapon) - 1)]
        if ench in [1,3]:
            out += " +" + str(random.randint(1,4-ench)) + Dices[random.randint(0, len(Dices) - 1)] + Damage_Types[random.randint(0, len(Damage_Types) - 1)]


        if ench in [2,3]:
            out += ", заговор: " + Cantrips[random.randint(0, len(Cantrips) - 1)]
    else:
        out= "Доспех "
        arm = Armor[random.randint(0, len(Armor) - 1)]
        if not (arm in Armor_Exept):
            out += arm
        else:
            out= arm

    out += "; " + "\n"



    return out

def chest(count: int):
    r = ""
    for i in range(0,count):
        r+=item()
    return r



def command(inp):
    rooms = inp.split(" ")
    if rooms[0] == "!break":
        return "b"
    elif rooms[0] == "!chest":
        cnt = int()
        try:
            if len(rooms[1]) < 3:
                try:
                    cnt = int(rooms[1])
                except:
                    cnt = random.randint(0,4)
                if cnt > 32:
                    return ", ты ёба? Возьми свои 32 и проваливай! Твой лут:" + "\n" + chest(32)
            else:
                return ", ты ёба? Возьми свои 32 и проваливай! Твой лут:" + "\n" + chest(32)
        except:
            cnt = random.randint(1, 4)
        return ", твой лут:" + "\n" + chest(cnt)
    elif not (rooms[0] in Commands):
        rooms[0] = int(rooms[0])

    if isinstance(rooms[0], int):
        for i in range(0,int(rooms[0])):
            print(str(i+1),random.randint(0,1))



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        #print('809437955331981374' in message.author.roles)
        if not has_role(message.author,812568275518226443):
            await message.channel.send('{0.author.mention}'.format(message) + command('{0.content}'.format(message)))

client = MyClient()
#client.run('ODEyNTY2NDM5MDMzOTYyNTA2.YDCndw.G0C9YkJuh9kdtACl1r3F-nrteRA')

token = os.environ.get('BOT_TOKEN')
client.run(str(token))


