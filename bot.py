#-*- coding:utf-8 -*-

import os
import discord
from discord.ext import commands, tasks
from datetime import datetime
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from se_util import count_str_in_list, get_auctions_from_player, return_item_info
from se_util import getUserid



client = commands.Bot(command_prefix='h!')
@client.event
async def on_ready():
    game = discord.Game("Skyblock Auction 탐색")
    await client.change_presence(status = discord.Status.online, activity = game)



#id : 895892266013585419
#token : ODk1ODkyMjY2MDEzNTg1NDE5.YV_KsQ.PIfi0u8vsx5qEeUEeZeu3Jtogo8 

api = "2c10d5fc-f22f-4730-af44-9a24e2852b40"
db_url = "https://hypixel-skyblock-user-default-rtdb.firebaseio.com/"

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "hypixel-skyblock-user",
    "private_key_id": "7abf55291f8b0cff143f6e0e213dc251f02ca5cb",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCqbBtC7+7zDwK3\nQeu77yH59ln2w+22UZYLD4bonMyiM58Hsd9mwOvLdMzH4aD/fi83A0wHCxlCha3o\nOpphv7YtLzmUQeaPthYD7IETLvs3tn9v3eGTIncjaoVsuk203iiM3jw9QE9wxCf8\nwGfH+Wb7tqAMTzWDXoLEBDCY4uAaC/r/liZiY/yvzzQt8qVydV146OqRDL0+fEcB\nDZJuow6IAc+obwC2Y2kErPjTG/yf9WtpGR2FVdLKOAYJRoZD17L1ICc/BQCAqKFv\nfuajfMBQHrSZY0j0YwnvEk9cLHcCrGzOaogDUYMD/8Q6U9GdzLW0EO3GlZSvOisd\n5iJWXz2fAgMBAAECggEASxAmycrokoIwDgupCzP+4RxS78/Iqh8xWVnTcC1wLJlU\nGI2N+rJKqWiesgN9aEtp/G8lU4zd6WD8AmedjCRm12wPjm+gX/gxpjTLfWmaGSX2\n54zxSF9L3nuSnRtKErovXiycl9X1p5OekUMl8vy1EXWU9RcGWQCN1EyMIyr6zj1z\noJF6Oi6oV7R7U71cGTfYrdYN43qNzYvtKtuDudye/i3DH7M7NARixOhPZHl05uYj\nv8DCBnInpM7b4O3oYjB+xnvxJ9i7eOKnCSlzq57lrJMwahxAkV6FgHpqlQCWYns2\nXzagyLq+2B+6opnQIXEpDbaeTVM2slbOL6g20LstEQKBgQDoFg943Lqb6GlfA3dO\n+VNsUx0ynbXEQyhpFZF2PLgWgsuLnhgtVfXQNMfzxDwKNIPG3N1EWoRAAG6Lzq1f\nk9Qnk1L+acgi+9KbJonGjPrFgBP9fs25ULMRStMXGT1eUXF4L4JGpIfb4fGnJxKW\nl1JASIFgdKCWOUPIcvnTuHA+swKBgQC7+3vngf/72fYUYQ2HVXa1aWvDXBLVOQmY\nXZl1vNBxubdPQUkf5rzAMd1s9IucyBx2nA0Bqw5203MFRasJR03ECyGlB7yB+x+0\njc8JTc6cQr1/KspAiQBG+kXTiZacgVNs22HKSfNkYWg2IoXCpmcRTdYTISqc9rh+\n9ExL12/7ZQKBgBSOp64v9wOKUZMN7op7QS1uKz7pg0kwHas5MtpDRJcR3M+wIDob\nzBs2IaPw9NR+lFGQDLVaQy6cGy6dDvRRVtBul0JbwlN+9MezYS7KHAhUcPDaQ4Sv\npjzY4NvB65KoKiHYK3Twa+xJFiuVJWtbWfjBs1wE2JiV1/AwZvqe8qpLAoGBAIFK\nV48D/58l6zVbByYEpu/hAQhNxHo4j5vnDIxJAAioFicBnRy+4yVBZqzwiTGdBM6j\nR+LU1s7tYdfHcfqguyDSEyLhbkrsAIN7YWFhzW/2C0VylcbLM5Cdw/bZU+hynoFp\nZhnuwONSh41sMxmMv6jMIyfnENsCaiSPPAaRt2htAoGBAM8zXWtpJqEh5qQA1XkP\nu03HoME69Hh8AdAXphWHdsBbAjCAweCXjvNs94vlKnxsi3YlYQQIrvNs1Bj9uxKE\n6jMCRHRiubrTE09GHn8YTHP9lp/eEznaT94idSjPDfK31AbXAnjH4uHTk6QKSZ7b\n85WtPAJmbZ0ToUXwJ84v8yPp\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-s186u@hypixel-skyblock-user.iam.gserviceaccount.com",
    "client_id": "117855260035479658358",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-s186u%40hypixel-skyblock-user.iam.gserviceaccount.com"
    })

firebase_admin.initialize_app(cred,{
    'databaseURL' : db_url
}) 


@client.command(name="가입")
async def reg(ctx, *text):
    user_keys = []
    txt = text[0]
    user_name = txt
    user_uuid = getUserid(user_name)
    user_id = ctx.author.id

    ref = db.reference()
    dic = ref.get()

    for key in dic.keys():
        user_keys.append(key)
    
    if str(user_id) in user_keys:
        embed = discord.Embed(title = "Failed Signup",
        description = "Hypixel Skyblock Auction", color = discord.Color.red()
        )
        embed.add_field(name="Already Signup %s!!!" %txt, value="SMH", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/895904324071358464/895953384220274688/scary_bmh.png")

    elif str(user_id) not in user_keys:
        embed = discord.Embed(title = "Success Signup",
        description = "Hypixel Skyblock Auction", color = discord.Color.green()
        )
        embed.add_field(name="Hello %s!" %txt, value="Welcome", inline=False)
        embed.set_thumbnail(url="https://cravatar.eu/helmhead/%s/68.png" %txt)
        # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/895904324071358464/895952842039390228/bmh1.png")

        ref = db.reference()
        ref.update({'%s'%user_id:{'username':user_name, 'useruuid':user_uuid, 
        '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, 
        '8':0, '9':0, '10':0, '11':0, '12':0, '13':0, '14':0, 
        '15':0, '16':0, '17':0, '18':0, '19':0, '20':0, '21':0,
        '22':0, '23':0, '24':0, '25':0, '26':0, '27':0, '28':0}})

    await ctx.send(embed=embed)

def return_link(iauuid):
    from selenium import webdriver
    from bs4 import BeautifulSoup

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("disable-gpu") 
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    options.add_experimental_option('prefs', prefs)

    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)


    # driver = webdriver.Chrome('./chromedriver.exe', options=options)
    driver.get('https://auctions.craftlink.xyz/auctions/%s' %iauuid)
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    link = str(soup.select_one('#root > div.bg-gray-800.h-screen > div.mx-3.sm\:mx-auctionPage.py-5 > div.flex.justify-between > div.flex.flex-row.items-center > img'))
    imlink = link[28:-3]

    if 'not_found' in imlink:
        return_link(iauuid)
    else:
        return imlink

@tasks.loop(seconds=30)
async def sell():
    global api
    user_keys = []
    ref = db.reference()
    dic = ref.get()

    for key in dic.keys():
        user_keys.append(key)
    
    for user_id in user_keys:
        ref = db.reference()
        data = ref.child(str(user_id)).get()  # data - 딕셔너리
        username = data['username']
        useruuid = data['useruuid']

        ah_data = (get_auctions_from_player(api,useruuid)) #ah_data - list

        if "true" in ah_data[0]:
            del ah_data[0]
            
            num1 = 0
            lis1 = []
            for i in ah_data:
                if '},{"_id"' in i:
                    lis1.append(num1)
                num1 += 1

            m1 = 0

            for i in lis1:
                k = ah_data[i+m1]
                l = k.split('},{')
                ah_data[i+m1] = l[0]
                ah_data.insert(i+m1+1, l[1])
                m1 += 1         

            item_list = []
            ah_count = count_str_in_list(ah_data, '"_id":"')

            num2 = 0
            lis2 = []
            for i in ah_data:
                if '"_id":"' in i:
                    lis2.append(num2)
                num2 += 1
            
            for i in range(1,ah_count+1):
                if i == ah_count :
                    item_list.append(ah_data[lis2[i-1]:])
                else:
                    item_list.append(ah_data[lis2[i-1]:lis2[i]])

            item = {}
            for i in range(1,ah_count+1):
                item[i] = return_item_info(item_list[i-1])

            #여기서부터 파이어베이스에 있는 데이터와 비교하기
            #if 1) 파이어베이스에 아무런 데이터도 존재하지 않는다면?
            #if 2) 파이어베이스에 아이템 정보가 일치하는 것이 있다면?

            #if 1)
            ref = db.reference()
            data = ref.child(str(user_id)).get()
            data_list = []

            for item_num in range(1,29):
                ref = db.reference('/%d' %int(user_id))
                data_list.append(ref.child(str(item_num)).get())

            if data_list[0] == 0:  
                for i in range(1, ah_count+1):
                    ref = db.reference('/%s/%s' %(user_id,i))
                    ref.update(item[i])

            
            #if 2)
            else:
                #item : api서버에서 가져온 "현재" *딕셔너리 - 딕셔너리*
                #data_list : firebase 서버에서 가져온 "과거" *리스트 - 딕셔너리*
                for n in range(1, len(item)+1):
                    get_item = item.get(n)
                    if data_list[n-1] != 0:
                        if get_item.get('_id') == data_list[n-1]['_id']:
                            if get_item.get('claimed_bidders') != data_list[n-1]['claimed_bidders']:
                                user = await client.fetch_user(user_id)

                                iname = get_item.get('item_name')
#                                 iauuid = get_item.get('uuid')
                                iamount = get_item.get('amount')
                                itier = get_item.get('tier')

                                imlink = return_link(iauuid)
                                
                                embed = discord.Embed(title = "%s님의 %s (%s)가 %s coin에 판매되었습니다." %(username, iname, itier, iamount),
                                description = "Hypixel Skyblock Auction" , color = 0xf64f59
                                )
                                # embed.add_field(name="아래의 링크를 통해 아이템 정보를 확인하세요!", value="https://auctions.craftlink.xyz/auctions/%s" %iauuid, inline=False)
                                embed.set_thumbnail(url="%s" %imlink)
                                await user.send(embed=embed)

                for j in range(1, len(item)+1):
                    ref = db.reference('/%s/%s' %(user_id, j))
                    ref.delete()
                    ref = db.reference('/%s' %(user_id))
                    ref.update({j:0})

                for j in range(1, len(item)+1):
                    ref = db.reference('/%s/%s' %(user_id, j))
                    ref.update(item.get(j))




    

@client.command(name='restart')
async def test(ctx, *text):
    pw = text[0]

    if str(pw) == "6213":
        sell.stop()
        time.sleep(0.3)
        sell.restart()
        print("restart process")
        embed = discord.Embed(title = "Sussess Restart",
        description = "ReStart Loop" , color = discord.Color.dark_gold()
        )

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title = "Wrong PassWord",
        description = "ReStart Loop" , color = discord.Color.dark_red()
        )

        await ctx.send(embed=embed)

@client.command(name='stop')
async def test(ctx, *text):
    pw = text[0]
    
    if str(pw) == "6213":
        sell.stop()
        print("stop process")

        embed = discord.Embed(title = "Sussess Stop",
        description = "Stop Loop" , color = discord.Color.dark_gold()
        )

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title = "Wrong PassWord",
        description = "Stop Loop" , color = discord.Color.dark_red()
        )

        await ctx.send(embed=embed)

@client.command(name='start')
async def test(ctx, *text):
    pw = text[0]
    
    if str(pw) == "6213":
        sell.start()
        print("start process")
        embed = discord.Embed(title = "Sussess Start",
        description = "Start Loop" , color = discord.Color.dark_gold()
        )

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title = "Wrong PassWord",
        description = "Start Loop" , color = discord.Color.dark_red()
        )

        await ctx.send(embed=embed)

    

 

@client.command(name="도움말")
async def help(ctx):
    embed = discord.Embed(title = "Bot Command Info",
    description = "Hypixel Skyblock Auction" , color = discord.Color.blurple()
    )

    embed.add_field(name="```h!가입 (Nickname)```", value="`Signup Bot Service`", inline=False)
    embed.set_footer(text="Made by. hanwn", icon_url="https://cdn.discordapp.com/attachments/895904324071358464/895960333007613972/512xnewhypixel.png")
    
    await ctx.send(embed=embed)

@client.command(name="명령어")
async def help(ctx):
    embed = discord.Embed(title = "Bot Command Info",
    description = "Hypixel Skyblock Auction" , color = discord.Color.blurple()
    )

    embed.add_field(name="```h!가입 (Nickname)```", value="`Signup Bot Service`", inline=False)
    embed.set_footer(text="Made by. hanwn", icon_url="https://cdn.discordapp.com/attachments/895904324071358464/895960333007613972/512xnewhypixel.png")
    
    
    await ctx.send(embed=embed)

client.remove_command("help")
@client.command(name="help")
async def help(ctx):
    embed = discord.Embed(title = "Bot Command Info",
    description = "Hypixel Skyblock Auction" , color = discord.Color.blurple()
    )


    embed.add_field(name="```h!가입 (Nickname)```", value="`Signup Bot Service`", inline=False)
    embed.set_footer(text="Made by. hanwn", icon_url="https://cdn.discordapp.com/attachments/895904324071358464/895960333007613972/512xnewhypixel.png")
    
    await ctx.send(embed=embed)

@client.command(name="?")
async def help(ctx):
    embed = discord.Embed(title = "Bot Command Info",
    description = "Hypixel Skyblock Auction" , color = discord.Color.blurple()
    )

    embed.add_field(name="```h!가입 (Nickname)```", value="`Signup Bot Service`", inline=False)
    embed.set_footer(text="Made by. hanwn", icon_url="https://cdn.discordapp.com/attachments/895904324071358464/895960333007613972/512xnewhypixel.png")
    
    await ctx.send(embed=embed)
    
@client.command(name="command")
async def help(ctx):
    embed = discord.Embed(title = "Bot Command Info",
    description = "Hypixel Skyblock Auction" , color = discord.Color.blurple()
    )

    embed.add_field(name="```h!가입 (Nickname)```", value="`Signup Bot Service`", inline=False)
    embed.set_footer(text="Made by. hanwn", icon_url="https://cdn.discordapp.com/attachments/895904324071358464/895960333007613972/512xnewhypixel.png")
    
    await ctx.send(embed=embed)


client.run(os.environ['token'])
