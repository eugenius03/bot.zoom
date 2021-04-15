import discord
from discord.ext import commands, tasks
from config import settings
import json
import aiohttp
from datetime import datetime
import aiocron


bot = commands.Bot(command_prefix = settings['prefix'])


@bot.command()
async def fox(ctx):
	response = requests.get('https://some-random-api.ml/img/fox')
	json_data = json.loads(response.text)

	embed = discord.Embed(color = 0xff9900, title = 'Random fox')
	embed.set_image(url = json_data['link'])
	await ctx.send(embed = embed)
	print ('+')

@bot.command()
async def багдан(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
      # This time we'll get the fact request as well!
      request2 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request2.json()

   embed = discord.Embed(title="Мать багдана!", color= 0xfc7f03)
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)

@bot.command()
async def расписание(ctx):
	await ctx.send('1.8.30-9.00')
	await ctx.send('2.9.20-9.50')
	await ctx.send('3. 10.10-10.40')
	await ctx.send('4. 11.00-11.30')
	await ctx.send('5.11.50-12.20')
	await ctx.send('6.12.40-13.10')
	await ctx.send('7. 13.30-14.00')

@bot.command()
async def физика(ctx):
  await ctx.send('Понеділок. Ідентификатор: 791 1173 5768. Код доступа: 7')
  await ctx.send('Четвер. Ідентификатор: 715 4522 1921. Код доступа: 7')

@bot.command()
async def английский_ЛП(ctx):
  await ctx.send('https://us04web.zoom.us/j/9525026828?pwd=aVQ4bGtvbU5NSk9Oc0pic2hZalhsZz09')
  await ctx.send('Идентификатор конференции: 952 502 6828. Код доступа: t1Ep0p')

@bot.command()
async def ОЗ(ctx):
  await ctx.send('https://us04web.zoom.us/j/74605810628?pwd=RC95T0lveHMwQ2NNZXpTZy9xTWxCdz09')
  await ctx.send('Meeting ID: 746 0581 0628. Passcode: G7cuvF')

@bot.command()
async def история(ctx):
  await ctx.send('https://us04web.zoom.us/j/4623021161?pwd=T3lCZVYzRXdlRXFQQWJUbHl4UWdtZz09')
  await ctx.send('Идентификатор конференции: 462 302 1161. Код доступа: 7LvnaX')

@bot.command()
async def география(ctx):
  await ctx.send('https://us04web.zoom.us/j/71336607212?pwd=cG9PaGdxSTZ2Rm5XeUVPRU5ROWpXdz09')
  await ctx.send('Идентификатор конференции: 713 3660 7212. Код доступа: D049RH')

@bot.command()
async def математика(ctx):
  await ctx.send('https://us04web.zoom.us/j/77080060700?pwd=cVNnV1lJbE5ScHZJVDNwVFRQQW1yUT09')
  await ctx.send('Идентификатор конференции: 770 8006 0700. Код доступа: Wmkv1h ')


@bot.command()
async def заруб(ctx):
  await ctx.send('https://us04web.zoom.us/j/79636494514?pwd=SlZ3ME9DSUJYNU1vaCtHSW5HcGVDZz09')
  await ctx.send('Идентификатор конференции: 796 3757 1497. Код доступа: bhQ53Y')

@bot.command()
async def укр_мова(ctx):
  await ctx.send('https://us04web.zoom.us/j/77772274632?pwd=T3hPUHA2bURZRStpMnhCUlBvcGVtZz09')
  await ctx.send('Идентификатор конференции: 777 7227 4632. Код доступа: G6Ji4R')

@bot.command()
async def укр_лит(ctx):
  await ctx.send('https://us04web.zoom.us/j/72181596875?pwd=Yk8vdHdTVUtSOFV1SHdYbFA0TEJoQT09')
  await ctx.send('Идентификатор конференции: 721 8159 6875. Код доступа: pS00hX')

@bot.command()
async def биология(ctx):
  await ctx.send('https://us04web.zoom.us/j/72873324305?pwd=UjBVeTlFRU5VWU4zN2Mzb0F2NjNoZz09')
  await ctx.send('Идентификатор конференции: 728 7332 4305. Код доступа: 8BLshM')

@bot.command()
async def инфа_1(ctx):
  await ctx.send('https://us04web.zoom.us/j/72337929789?pwd=aFoveU00SnVzVVZ2Y1dWVnhKa2NLZz09')
  await ctx.send('Идентификатор конференции: 723 3792 9789. Код доступа: 5EvfCK')

@bot.command()
async def химия(ctx):
  await ctx.send('https://us04web.zoom.us/j/78486165193?pwd=bHRDOGozeTdxNHBxK0VLTVoxNGc0Zz09')
  await ctx.send('Идентификатор конференции: 784 8616 5193. Код доступа: 9VT6w1')

@bot.command()
async def немецкий_1(ctx):
  await ctx.send('-')
  await ctx.send('-')

@bot.command()
async def праця(ctx):
  await ctx.send('https://us04web.zoom.us/j/77910918580?pwd=Nnl6am5GSGRqa2FjY3c2b2pMWDJSQT09')
  await ctx.send('Идентификатор конференции: 779 1091 8580. Код доступа: 0Z8ypT')

@bot.command()
async def мистецтво(ctx):
  await ctx.send('-')
  await ctx.send('-')

@bot.command()
async def физра(ctx):
  await ctx.send('https://us05web.zoom.us/j/87276036504?pwd=b0NzRFd1akpwOGZzMmtzSjVkL3JVUT09')
  await ctx.send('Идентификатор конференции: 872 7603 6504. Код доступа: NTrig7')

@bot.command()
async def право(ctx):
  await ctx.send('-')
  await ctx.send('Индентификатор конференции: 535 632 5355. Код доступа: bLwh9A')

@bot.command()
async def деман(ctx):
  await ctx.send('самп')

@bot.command()
async def английский_ЛО(ctx):
  await ctx.send('Код: 4294474020. Пароль 4Qj4cL')

@bot.command()
async def инфа_2(ctx):
  await ctx.send('Идентификатор конференции: 761 9784 4597. Код доступа: 7cpYAi')
  await ctx.send('https://us04web.zoom.us/j/76197844597?pwd=NG5SME9sOVRyaEFmMnBzT3lVWCs1Zz09')


@bot.command()
async def кровать(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/720363306828693515/829308710181928980/EXv4iBvWoAE9zjD.jpg')

@bot.command()
async def спин(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/720363306828693515/830541831220625408/image0.png')

CHANNEL_ID_1 = 831595207836565565

@aiocron.crontab('20 8 * * 1')
async def monday():
    channel = bot.get_channel(CHANNEL_ID_1)
    await channel.send('1. Географія')
    await channel.send('2. Фізика')
    await channel.send('3-4. Біологія')
    await channel.send('5-6. Укр.мова')
    await channel.send('7. Історія/Мистецтво')

@aiocron.crontab('20 8 * * 2')
async def tuesday():
    channel = bot.get_channel(CHANNEL_ID_1)
    await channel.send('1-2. Математика')
    await channel.send('3. Заруб.літ')
    await channel.send('4. Англ.мова')
    await channel.send('5-6. Інформат.')
    await channel.send('7. Геогр/ОЗ')

@aiocron.crontab('25 8 * * 3')
async def wednesday():
    channel = bot.get_channel(CHANNEL_ID_1)
    await channel.send('1-2. Хімія')
    await channel.send('3-4. Математика')
    await channel.send('5. Праця')
    await channel.send('6. Укр.літ')
    await channel.send('7. Заруб.літ')

@aiocron.crontab('20 8 * * 4')
async def thursday():
    channel = bot.get_channel(CHANNEL_ID_1)
    await channel.send('1-2. Історія')
    await channel.send('3-4. Фізика')
    await channel.send('5-6. Англ. мова')
    await channel.send('7. Фіз-ра')

@aiocron.crontab('20 8 * * 5')
async def friday():
    channel = bot.get_channel(CHANNEL_ID_1)
    await channel.send('1-2. Англ мова')
    await channel.send('3. Укр літ')
    await channel.send('4. Право')
    await channel.send('5-6 Нім.мова')
    await channel.send('7. Фіз-ра')

@bot.command()
async def команды(ctx):
  await ctx.send('.багдан, .fox, .спин, .физика, .английский_ЛО, .английский_ЛП, .ОЗ, .история, .кровать, .география, .физра, .инфа_1, .инфа_2, .немецкий_1, .деман, .право, .праця, .химия, .биология, .укр_лит, .укр_мова, .заруб, .математика')

fizika = 'Понеділок. Ідентификатор: 791 1173 5768. Код доступа: 7'
fizika2 = 'Четвер. Ідентификатор: 715 4522 1921. Код доступа: 7'
angl_1_1 = 'https://us04web.zoom.us/j/9525026828?pwd=aVQ4bGtvbU5NSk9Oc0pic2hZalhsZz09'
angl_1_2 = 'Идентификатор конференции: 952 502 6828. Код доступа: t1Ep0p'
oz = 'https://us04web.zoom.us/j/74605810628?pwd=RC95T0lveHMwQ2NNZXpTZy9xTWxCdz09'
oz2 = 'Meeting ID: 746 0581 0628. Passcode: G7cuvF'
history = 'https://us04web.zoom.us/j/4623021161?pwd=T3lCZVYzRXdlRXFQQWJUbHl4UWdtZz09'
history2 = 'Идентификатор конференции: 462 302 1161. Код доступа: 7LvnaX'
geography = 'https://us04web.zoom.us/j/71336607212?pwd=cG9PaGdxSTZ2Rm5XeUVPRU5ROWpXdz09'
geography2 = 'Идентификатор конференции: 713 3660 7212. Код доступа: D049RH'
matesha = 'https://us04web.zoom.us/j/77080060700?pwd=cVNnV1lJbE5ScHZJVDNwVFRQQW1yUT09'
matesha2 = 'Идентификатор конференции: 770 8006 0700. Код доступа: Wmkv1h'
zarub = 'https://us04web.zoom.us/j/79636494514?pwd=SlZ3ME9DSUJYNU1vaCtHSW5HcGVDZz09'
zarub2 = 'Идентификатор конференции: 796 3757 1497. Код доступа: bhQ53Y'
ukr_mova = 'https://us04web.zoom.us/j/77772274632?pwd=T3hPUHA2bURZRStpMnhCUlBvcGVtZz09'
ukr_mova2 = 'Идентификатор конференции: 777 7227 4632. Код доступа: G6Ji4R'
ukr_lit = 'https://us04web.zoom.us/j/72181596875?pwd=Yk8vdHdTVUtSOFV1SHdYbFA0TEJoQT09'
ukr_lit2 = 'Идентификатор конференции: 721 8159 6875. Код доступа: pS00hX'
biology = 'https://us04web.zoom.us/j/72873324305?pwd=UjBVeTlFRU5VWU4zN2Mzb0F2NjNoZz09'
biology2 = 'Идентификатор конференции: 728 7332 4305. Код доступа: 8BLshM'
infa_1_1 = 'https://us04web.zoom.us/j/72337929789?pwd=aFoveU00SnVzVVZ2Y1dWVnhKa2NLZz09'
infa_1_2 = 'Идентификатор конференции: 723 3792 9789. Код доступа: 5EvfCK'
himiya = 'https://us04web.zoom.us/j/78486165193?pwd=bHRDOGozeTdxNHBxK0VLTVoxNGc0Zz09'
himiya2 = 'Идентификатор конференции: 784 8616 5193. Код доступа: 9VT6w1'
deutsch = '-'
deutsch2 = '-'
trud = 'https://us04web.zoom.us/j/77910918580?pwd=Nnl6am5GSGRqa2FjY3c2b2pMWDJSQT09'
trud2 = 'Идентификатор конференции: 779 1091 8580. Код доступа: 0Z8ypT'
risovanie = '-'
risovanie2 = '-'
fizra = 'https://us05web.zoom.us/j/87276036504?pwd=b0NzRFd1akpwOGZzMmtzSjVkL3JVUT09'
fizra2 = 'Идентификатор конференции: 872 7603 6504. Код доступа: NTrig7'
pravo = 'Индентификатор конференции: 535 632 5355. Код доступа: bLwh9A'
angl_2 =  'Код: 4294474020. Пароль 4Qj4cL'
infa_2_1 = 'https://us04web.zoom.us/j/76197844597?pwd=NG5SME9sOVRyaEFmMnBzT3lVWCs1Zz09'
infa_2_2 = 'Идентификатор конференции: 761 9784 4597. Код доступа: 7cpYAi'

CHANNEL_ID = 775262111378702336 

@aiocron.crontab('28 5 * * 1')
async def urok_1_1():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(geography)
    await channel.send(geography2)

@aiocron.crontab('18 9 * * 1')
async def urok_1_2():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(fizika)

@aiocron.crontab('08 7 * * 1')
async def urok_1_3():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(biology)
    await channel.send(biology2)

@aiocron.crontab('58 7 * * 1')
async def urok_1_4():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(biology)
    await channel.send(biology2)

@aiocron.crontab('48 8 * * 1')
async def urok_1_5():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(ukr_mova)
    await channel.send(ukr_mova2)

@aiocron.crontab('38 9 * * 1')
async def urok_1_6():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(ukr_mova)
    await channel.send(ukr_mova2)

@aiocron.crontab('28 10 * * 1')
async def urok_1_7():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("История: ", history)
    await channel.send(history2)
    await channel.send("Мистецтво: ", risovanie)
    await channel.send(risovanie2)

@aiocron.crontab('28 5 * * 1')
async def urok_2_1():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(matesha)
    await channel.send(matesha2)

@aiocron.crontab('18 6 * * 1')
async def urok_2_2():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(matesha)
    await channel.send(matesha2)

@aiocron.crontab('08 7 * * 1')
async def urok_2_3():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(zarub)
    await channel.send(zarub2)

@aiocron.crontab('58 8 * * 1')
async def urok_2_4():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(angl_1_1)
    await channel.send(angl_1_2)
    await channel.send(angl_2)

@aiocron.crontab('48 8 * * 1')
async def urok_2_5():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Инфа 1 группа: ', infa_1_1)
    await channel.send(infa_1_2)
    await channel.send('Инфа 2 группа: ', infa_2_1)
    await channel.send(infa_2_2)

@aiocron.crontab('38 9 * * 1')
async def urok_2_6():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Инфа 1 группа: ', infa_1_1)
    await channel.send(infa_1_2)
    await channel.send('Инфа 2 группа: ', infa_2_1)
    await channel.send(infa_2_2)

@aiocron.crontab('28 10 * * 1')
async def urok_2_7():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('География: ', geography)
    await channel.send(geography2)
    await channel.send('ОЗ:', oz)
    await channel.send(oz2)


@aiocron.crontab('28 5 * * 1')
async def urok_3_1():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(himiya)
    await channel.send(himiya2)

@aiocron.crontab('18 6 * * 1')
async def urok_3_2():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(himiya)
    await channel.send(himiya2)

@aiocron.crontab('08 7 * * 1')
async def urok_3_3():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(matesha)
    await channel.send(matesha2)

@aiocron.crontab('58 7 * * 1')
async def urok_3_4():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(matesha)
    await channel.send(matesha2)

@aiocron.crontab('48 8 * * 1')
async def urok_3_5():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(trud)
    await channel.send(trud2)

@aiocron.crontab('38 9 * * 1')
async def urok_3_6():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(ukr_lit)
    await channel.send(ukr_lit2)

@aiocron.crontab('28 10 * * 1')
async def urok_3_7():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(zarub)
    await channel.send(zarub2)

@aiocron.crontab('28 5 * * 1')
async def urok_4_1():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(history)
    await channel.send(history2)

@aiocron.crontab('18 6 * * 1')
async def urok_4_2():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(history)
    await channel.send(history2)

@aiocron.crontab('08 7 * * 1')
async def urok_4_3():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(fizika2)

@aiocron.crontab('58 7 * * 1')
async def urok_4_4():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(fizika2)

@aiocron.crontab('48 8 * * 1')
async def urok_4_5():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Англ ЛП: ', angl_1_1)
    await channel.send(angl_1_2)
    await channel.send('Англ ЛО: ', angl_2)

@aiocron.crontab('38 9 * * 1')
async def urok_4_6():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Англ ЛП: ', angl_1_1)
    await channel.send(angl_1_2)
    await channel.send('Англ ЛО: ', angl_2)


@aiocron.crontab('28 10 * * 1')
async def urok_4_7():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(fizra)
    await channel.send(fizra2)

@aiocron.crontab('28 5 * * 1')
async def urok_5_1():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Англ ЛП: ', angl_1_1)
    await channel.send(angl_1_2)
    await channel.send('Англ ЛО: ', angl_2)

@aiocron.crontab('18 6 * * 1')
async def urok_5_2():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Англ ЛП: ', angl_1_1)
    await channel.send(angl_1_2)
    await channel.send('Англ ЛО: ', angl_2)

@aiocron.crontab('08 7 * * 1')
async def urok_5_3():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(ukr_lit)
    await channel.send(ukr_lit2)

@aiocron.crontab('58 7 * * 1')
async def urok_5_4():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(pravo)

@aiocron.crontab('48 8 * * 1')
async def urok_5_5():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(deutsch)
    await channel.send(deutsch2)

@aiocron.crontab('38 9 * * 1')
async def urok_5_6():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(deutsch)
    await channel.send(deutsch2)

@aiocron.crontab('28 10 * * 1')
async def urok_5_7():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(fizra)
    await channel.send(fizra2)































bot.run(settings['token'])

