import discord
from discord.ext import commands, tasks
from random import choice
import secreto

client = commands.Bot(command_prefix='.')
token = secreto.seu_token()
status = ['Tá precisando de mim para  algo?', 'Se precisar, estou aqui']


@client.event
async def on_ready():
    change_status.start()
    print('Poseidonbot está conectado ao Discord')
    print(client.user.name)
    print(client.user.id)
    print('-----LF------')


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


@client.command(name='ping', comandos='Esse comando retorna o ping')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latência: {round(client.latency * 1000)}ms')


@client.command(name='ola', comandos='Esse comando retorna uma mensagem de boas-vindas')
async def ola(ctx):
    respostas_ola = ['Por que você me acordou tão cedo?', 'Dá um oi mas num dá um bom dia. Cadê a educação?']
    await ctx.send((choice(respostas_ola)))


@client.command(name='bomdia', comandos='Esse comando retorna uma mensagem de bom dia')
async def bomdia(ctx):
    respostas_bomdia = ['Bom dia pro senhor também', 'Bom dia, como que você tá?']
    await ctx.send((choice(respostas_bomdia)))


@client.command(name='boatarde', comandos='Esse comando retorna uma mensagem de boa tarde')
async def boatarde(ctx):
    respostas_boatarde = ['Boa tarde pro senhor também', 'Boa tarde, como que você tá?']
    await ctx.send((choice(respostas_boatarde)))


@client.command(name='boanoite', comandos='Esse comando retorna uma mensagem de boa noite')
async def boanoite(ctx):
    respostas_boanoite = ['Boa noite pro senhor também', 'Boa noite, como que você tá?']
    await ctx.send((choice(respostas_boanoite)))


@client.command(name='segunda', comandos='Esse comando retorna horário de segunda pela manhã')
async def segunda(ctx):
    await ctx.send('https://i.ibb.co/1mbLBXp/Segunda-Manh.png')


@client.command(name='segtarde', comandos='Esse comando retorna horário de segunda pela tarde')
async def segtarde(ctx):
    await ctx.send('https://i.ibb.co/ZVyg6MT/Segunda-Tarde.png')


@client.command(name='terca', comandos='Esse comando retorna horário de terça')
async def terca(ctx):
    await ctx.send('https://i.ibb.co/nLZNLmF/Terca.png')


@client.command(name='quarta', comandos='Esse comando retorna horário de quarta')
async def quarta(ctx):
    await ctx.send('https://i.ibb.co/d2B23K6/Quarta.png')


@client.command(name='quinta', comandos='Esse comando retorna horário de quinta pela manhã')
async def quinta(ctx):
    await ctx.send('https://i.ibb.co/ZNy8TrC/Quinta.png')


@client.command(name='quitarde', comandos='Esse comando retorna horário de quinta pela tarde')
async def quitarde(ctx):
    await ctx.send('https://i.ibb.co/ZcVkPc4/Quinta-tarde.png')


@client.command(name='sexta', comandos='Esse comando retorna horário de quinta pela tarde')
async def sexta(ctx):
    await ctx.send('https://i.ibb.co/kBcgfRC/Sexta.png')


@client.command(name='aula', comandos='Esse comando retorna horário e link das aulas do Colégio Opção')
async def aula(ctx):
    await ctx.send('Aulas do Colégio Opção de segunda à sexta das 7:10 às 12:20 \n '
                   'Link do Meet: https://meet.google.com/hhn-iuhw-hi')


@client.command(name='aulatarde', comandos='Esse comando retorna horário e link das aulas do Colégio Opção à tarde')
async def aulatarde(ctx):
    await ctx.send('Aulas do Colégio Opção de tarde às segundas e quintas das 14:00 às 18:20 \n '
                   'Link do Meet: https://meet.google.com/hhn-iuhw-hib')


@client.command(name='ccaa', comandos='Esse comando retorna horário e link das aulas do CCAA')
async def ccaa(ctx):
    await ctx.send('Aulas do CCAA às terças e sextas às 16h \n'
                   'Link do Zoom: https://zoom.us/j/95878430985?pwd=Mk8rQ0RTaVF5Lzk3bFliTTY1NUFFUT0')


@client.command(name='conversacao', comandos='Esse comando retorna horário e link das aulas do CCAA de conversação')
async def conversacao(ctx):
    await ctx.send('Aula de coversação do CCAA às terças das 18:00 às 19:30 \n '
                   'Link do Zoom: https://zoom.us/j/96406311855?pwd=aWo4VSsvTXlqcmdwWXQ2ak9GZ3FUQT09')


@client.command(name='f1calendario', comandos='Esse comando retorna o calendário da F1')
async def f1calendario(ctx):
    await ctx.send('https://i.ibb.co/FHqRVBj/F1-calend-rio.png')


@client.command(name='f1bahrein', comandos='Esse comando retorna os horários dos treinos no Bahrein da F1')
async def f1bahrein(ctx):
    await ctx.send('Horário do GP do Bahrein 🇧🇭\n'
                   'https://i.ibb.co/2S9yCYG/Tracado-Grand-Prix-300x169.png\n'
                   '''
Sexta-feira – 26/03/2021:
8h30 às 9h30 – Treino Livre 1 – Resultado
12h às 13h – Treino Livre 2 – Resultado

Sábado – 27/03/2021:
9h às 10h – Treino Livre 3 – Resultado
12h às 13h – Qualificação – Resultado

Domingo – 28/03/2021:
12h – Corrida''')


@client.command(name='f1emiliaromanha', comandos='Esse comando retorna os horários dos treinos na Emilia-Romanha da F1')
async def f1emiliaromanha(ctx):
    await ctx.send('Horário do GP da Emilia-Romanha 🇮🇹\n'
                   'https://i.ibb.co/0nHcvhm/image.png\n'
                   '''

Sexta-feira – 16/04/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 17/04/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 18/04/2021:
10h – Corrida''')


@client.command(name='f1portugal', comandos='Esse comando retorna os horários dos treinos em Portugal da F1')
async def f1portugal(ctx):
    await ctx.send('Horário do GP de Portugal 🇵🇹\n'
                   'https://i.ibb.co/QKqs1Z6/image.png\n'
                   '''

Sexta-feira – 30/04/2021:
7h30 às 8h30 – Treino Livre 1
11h às 12h – Treino Livre 2

Sábado – 01/05/2021:
8h às 9h – Treino Livre 3
11h às 12h – Qualificação

Domingo – 02/05/2021:
11h – Corrida''')


@client.command(name='f1espanha', comandos='Esse comando retorna os horários dos treinos na Espanha da F1')
async def f1espanha(ctx):
    await ctx.send('Horário do GP da Espanha 🇪🇸\n'
                   'https://i.ibb.co/ZNRG9DG/image.png\n'
                   '''

Sexta-feira – 07/05/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 08/05/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 09/05/2021:
10h – Corrida''')


@client.command(name='f1monaco', comandos='Esse comando retorna os horários dos treinos em Mônaco da F1')
async def f1monaco(ctx):
    await ctx.send('Horário do GP de Mônaco 🇲🇨\n'
                   'https://i.ibb.co/58Tjkw3/Monoco-Circuit.png\n'
                   '''

Quinta-feira – 20/05/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 22/05/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 23/05/2021:
10h – Corrida''')


@client.command(name='f1azerbaijao', comandos='Esse comando retorna os horários dos treinos no Azerbaijão da F1')
async def f1azerbaijao(ctx):
    await ctx.send('Horário do GP do Azerbaijão 🇦🇿\n'
                   'https://i.ibb.co/NnVXtFv/Baku-Circuit.png\n'
                   '''
Sexta-feira – 04/06/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 05/06/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 07/06/2021:
9h – Corrida''')


@client.command(name='f1canada', comandos='Esse comando retorna os horários dos treinos no Canadá da F1')
async def f1canada(ctx):
    await ctx.send('Horário do GP do Canadá 🇨🇦\n'
                   'https://i.ibb.co/9TqbVrM/Canada-Circuit.png\n'
                   '''

Sexta-feira – 11/06/2021:
12h30 às 13h30 – Treino Livre 1
16h às 17h – Treino Livre 2

Sábado – 12/06/2021:
12h às 13h – Treino Livre 3
15h às 16h – Qualificação

Domingo – 13/06/2021:
15h – Corrida''')


@client.command(name='f1franca', comandos='Esse comando retorna os horários dos treinos na França da F1')
async def f1franca(ctx):
    await ctx.send('Horário do GP da França 🇫🇷\n'
                   'https://i.ibb.co/rw2VpLZ/image.png\n'
                   '''

Sexta-feira – 25/06/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 26/06/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 27/06/2021:
10h – Corrida''')


@client.command(name='f1austria', comandos='Esse comando retorna os horários dos treinos na Áustria da F1')
async def f1austria(ctx):
    await ctx.send('Horário do GP da Áustria 🇦🇹\n'
                   'https://i.ibb.co/3dThwGg/image.png\n'
                   '''

Sexta-feira – 02/07/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 03/07/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 04/07/2021:
10h – Corrida''')


@client.command(name='f1inglaterra', comandos='Esse comando retorna os horários dos treinos na Inglaterra da F1')
async def f1inglaterra(ctx):
    await ctx.send('Horário do GP da Inglaterra 🇬🇧󠁧\n'
                   'https://i.ibb.co/xFtfh8y/image.png\n'
                   '''

Sexta-feira – 16/07/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 17/07/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 18/07/2021:
11h – Corrida''')


@client.command(name='f1hungria', comandos='Esse comando retorna os horários dos treinos na Hungria da F1')
async def f1hungria(ctx):
    await ctx.send('Horário do GP da Hungria 🇭🇺\n'
                   'https://i.ibb.co/GCdkDpg/image.png\n'
                   '''

Sexta-feira – 30/07/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 31/07/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 01/08/2021:
10h – Corrida''')


@client.command(name='f1belgica', comandos='Esse comando retorna os horários dos treinos na Bélgica da F1')
async def f1belgica(ctx):
    await ctx.send('Horário do GP da Bélgica 🇧🇪\n'
                   'https://i.ibb.co/ypN88LN/Belgium-Circuit.png\n'
                   '''

Sexta-feira – 27/08/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 28/08/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 29/08/2021:
10h – Corrida''')


@client.command(name='f1holanda', comandos='Esse comando retorna os horários dos treinos na Holanda da F1')
async def f1holanda(ctx):
    await ctx.send('Horário do GP da Holanda 🇳🇱\n'
                   'https://i.ibb.co/f90QPFt/Netherlands-Circuit.png\n'
                   '''

Sexta-feira – 03/09/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 04/09/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 05/09/2021:
10h – Corrida''')


@client.command(name='f1italia', comandos='Esse comando retorna os horários dos treinos na Itália da F1')
async def f1italia(ctx):
    await ctx.send('Horário do GP da Itália 🇮🇹\n'
                   'https://i.ibb.co/YbDSPrP/image.png\n'
                   '''

GP da Itália

Sexta-feira – 10/09/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 11/09/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 12/09/2021:
10h – Corrida''')


@client.command(name='f1russia', comandos='Esse comando retorna os horários dos treinos na Rússia da F1')
async def f1russia(ctx):
    await ctx.send('Horário do GP da Rússia 🇷🇺\n'
                   'https://i.ibb.co/m4F2tHv/Russia-Circuit.png\n'
                   '''

Sexta-feira – 24/09/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 25/09/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 26/09/2021:
9h – Corrida''')


@client.command(name='f1cingapura', comandos='Esse comando retorna os horários dos treinos em Cingapura da F1')
async def f1cingapura(ctx):
    await ctx.send('Horário do GP de Cingapura 🇸🇬\n'
                   'https://i.ibb.co/grm4Zrt/image.png\n'
                   '''

Sexta-feira – 01/10/2021:
6h às 7h – Treino Livre 1
9h30 às 10h30 – Treino Livre 2

Sábado – 02/10/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 03/10/2021:
9h – Corrida''')


@client.command(name='f1japao', comandos='Esse comando retorna os horários dos treinos no Japão da F1')
async def f1japao(ctx):
    await ctx.send('Horário do GP de Japão 🇯🇵\n'
                   'https://i.ibb.co/JxFSLQm/Japan-Circuit.png\n'
                   '''
Quinta-feira – 07/10/2021:
23h30 às 0h30 – Treino Livre 1

Sexta-feira – 08/10/2021:
3h às 4h – Treino Livre 2

Sábado – 09/10/2021:
0h às 1h – Treino Livre 3
3h às 4h – Qualificação

Domingo – 10/10/2021:
2h – Corrida''')


@client.command(name='f1eua', comandos='Esse comando retorna os horários dos treinos nos EUA da F1')
async def f1eua(ctx):
    await ctx.send('Horário do GP dos EUA 🇺🇸\n'
                   'https://i.ibb.co/RcMqH86/USA-Circuit.png\n'
                   '''
Sexta-feira – 22/10/2021:
13h30 às 14h30 – Treino Livre 1
17h às 18h – Treino Livre 2

Sábado – 23/10/2021:
15h às 16h – Treino Livre 3
18h às 19h – Qualificação

Domingo – 24/10/2021:
16h – Corrida''')


@client.command(name='f1mexico', comandos='Esse comando retorna os horários dos treinos no México da F1')
async def f1mexico(ctx):
    await ctx.send('Horário do GP do México 🇲🇽\n'
                   'https://i.ibb.co/TbF7g2Z/image.png\n'
                   '''
Sexta-feira – 29/10/2021:
13h30 às 14h30 – Treino Livre 1
17h às 18h – Treino Livre 2

Sábado – 30/10/2021:
13h às 14h – Treino Livre 3
16h às 17h – Qualificação

Domingo – 31/10/2021:
15h – Corrida''')


@client.command(name='f1brasil', comandos='Esse comando retorna os horários dos treinos no Brasil da F1')
async def f1brasil(ctx):
    await ctx.send('Horário do GP do Brasil 🇧🇷\n'
                   'https://i.ibb.co/R6Rw91N/image.png\n'
                   '''
Sexta-feira – 05/11/2021:
11h30 às 12h30 – Treino Livre 1
15h às 16h – Treino Livre 2

Sábado – 06/11/2021:
12h às 13h – Treino Livre 3
15h às 16h – Qualificação

Domingo – 07/11/2021:
14h – Corrida''')


@client.command(name='f1australia', comandos='Esse comando retorna os horários dos treinos na Austrália da F1')
async def f1australia(ctx):
    await ctx.send('Horário do GP da Austrália 🇦🇺\n'
                   'https://i.ibb.co/gbYCRB2/Australia-Circuit.png\n'
                   '''
Quinta-feira – 18/11/2021:
22h30 às 23h30 – Treino Livre 1

Sexta-feira – 19/11/2021:
2h às 3h – Treino Livre 2

Sábado – 20/11/2021:
0h às 1h – Treino Livre 3
3h às 4h – Qualificação

Domingo – 21/11/2021:
3h – Corrida''')


@client.command(name='f1arabiasaudita', comandos='Esse comando retorna os horários dos treinos na Arábia Saudita da F1')
async def f1arabiasaudita(ctx):
    await ctx.send('Horário do GP da Arábia Saudita 🇸🇦\n'
                   'https://i.ibb.co/7VVYd7W/Jeddah-Street-Circuit-No-Turn-Numbers-HD.jpg\n'
                   '''
Sexta-feira – 03/12/2021:
9h30 às 10h30 – Treino Livre 1
13h às 14h – Treino Livre 2

Sábado – 04/12/2021:
10h às 11h – Treino Livre 3
13h às 14h – Qualificação

Domingo – 05/12/2021:
13h – Corrida''')


@client.command(name='f1abudhabi', comandos='Esse comando retorna os horários dos treinos em Abu Dhabi da F1')
async def f1abudhabi(ctx):
    await ctx.send('Horário do GP de Abu Dhabi 🇸🇦\n'
                   'https://i.ibb.co/pw52GvV/Abu-Dhabi-Circuit.png\n'
                   '''
Sexta-feira – 10/12/2021:
6h30 às 7h30 – Treino Livre 1
10h às 11h – Treino Livre 2

Sábado – 11/12/2021:
7h às 8h – Treino Livre 3
10h às 11h – Qualificação

Domingo – 12/12/2021:
10h – Corrida''')

client.run(token)
