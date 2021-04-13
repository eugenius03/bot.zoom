import discord
from discord.ext import commands
from config import settings
import json
import requests
import aiohttp

slova = ['бб я спать','всем бб я спать','кровать','бб всем']
bot = commands.Bot(command_prefix = settings['prefix'])
spin = ['спин']
horny = ['скиньте','фулл']
hueta = ['-search']

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
async def алгебра(ctx):
  await ctx.send('-')
  await ctx.send('-')

@bot.command()
async def геометрия(ctx):
  await ctx.send('-')
  await ctx.send('-')

@bot.command()
async def заруб(ctx):
  await ctx.send('-')
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
  await ctx.send('-')
  await ctx.send('-')

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


bot.run(settings['token'])

