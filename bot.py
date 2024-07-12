import discord
import config
import random
import runSD
import json
import requests


intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    print("Ready!")

# メッセージの検知
@client.event
async def on_message(message):



    #prompt
    if message.channel.name == 'prompt':
        if message.author == client.user:
            return
        if message.content.startswith('!loras'):
            url = 'http://localhost:7860/sdapi/v1/loras'
            response = requests.get(url, headers={'accept': 'application/json'})
        
            if response.status_code == 200:
                loras = response.json()
                loras_aliases = [f"<lora:{lora['alias']}:1>" for lora in loras]
                await message.channel.send('\n'.join(loras_aliases))
            else:
                await message.channel.send('Failed to retrieve LoRAs.')
            return

        new_prompt = message.content
        try:
            with open('Imgsetting.json', 'r+') as file:
                data = json.load(file)
                data['prompt'] = new_prompt  # promptキーのみを更新
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.truncate()

            await message.channel.send(f'JSONファイルが更新されました: {new_prompt}')
        except Exception as e:
            await message.channel.send(f'エラーが発生しました: {e}')



    #negative 
    if message.channel.name == 'negative-prompt':
        if message.author == client.user:
            return
        new_negative = message.content
        try:
            with open('Imgsetting.json', 'r+') as file:
                data = json.load(file)
                data['negative_prompt'] = new_negative 
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.truncate()

            await message.channel.send(f'JSONファイルが更新されました: {new_negative}')
        except Exception as e:
            await message.channel.send(f'エラーが発生しました: {e}')


        
    #steps
    if message.channel.name == 'steps':
        if message.author == client.user:
            return
        new_steps = message.content
        try:
            with open('Imgsetting.json', 'r+') as file:
                data = json.load(file)
                data['steps'] = new_steps 
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.truncate()

            await message.channel.send(f'JSONファイルが更新されました: {new_steps}')
        except Exception as e:
            await message.channel.send(f'エラーが発生しました: {e}')


    #sampler
    if message.channel.name == 'sampler':
        if "?" in message.content.lower():#プロパティの照会
            url = 'http://localhost:7860/sdapi/v1/samplers'
            headers = {'accept': 'application/json'}

            response = requests.get(url, headers=headers)
            data = response.json()
            await message.channel.send(data)
            return
        if message.author == client.user:
            return
        new_sampler = message.content
        try:
            with open('Imgsetting.json', 'r+') as file:
                data = json.load(file)
                data['sampler_index'] = new_sampler
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.truncate()

            await message.channel.send(f'JSONファイルが更新されました: {new_sampler}')
        except Exception as e:
            await message.channel.send(f'エラーが発生しました: {e}')



    #width
    if message.channel.name == 'width':
        if message.author == client.user:
            return
        new_width = message.content
        try:
            with open('Imgsetting.json', 'r+') as file:
                data = json.load(file)
                data['width'] = new_width
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.truncate()

            await message.channel.send(f'JSONファイルが更新されました: {new_width}')
        except Exception as e:
            await message.channel.send(f'エラーが発生しました: {e}')


    #height
    if message.channel.name == 'height':
        if message.author == client.user:
            return
        new_height = message.content
        try:
            with open('Imgsetting.json', 'r+') as file:
                data = json.load(file)
                data['height'] = new_height
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.truncate()

            await message.channel.send(f'JSONファイルが更新されました: {new_height}')
        except Exception as e:
            await message.channel.send(f'エラーが発生しました: {e}')



    #seed
    if message.channel.name == 'seed':
        if message.author == client.user:
            return
        new_sampler = message.content
        try:
            with open('Imgsetting.json', 'r+') as file:
                data = json.load(file)
                data['seed'] = new_seed
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.truncate()

            await message.channel.send(f'JSONファイルが更新されました: {new_seed}')
        except Exception as e:
            await message.channel.send(f'エラーが発生しました: {e}')



    #checkpoint
    if message.channel.name == 'checkpoint':
        if "?" in message.content.lower():
            url = 'http://localhost:7860/sdapi/v1/sd-models'
            headers = {'accept': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                model_names = [item['model_name'] for item in data]
                await message.channel.send("\n".join(model_names))
            else:
                await message.channel.send(f"Failed to retrieve data with status code {response.status_code}")
            return
        if message.author == client.user:
            return
        new_checkpoint = message.content
        try:
            with open('Imgsetting.json', 'r+') as file:
                data = json.load(file)
                data['sd_model_checkpoint'] = new_checkpoint
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.truncate()

            await message.channel.send(f'JSONファイルが更新されました: {new_checkpoint}')
        except Exception as e:
            await message.channel.send(f'エラーが発生しました: {e}')


    if message.channel.name == 'run':
        if message.author == client.user:
            return
        await message.channel.send("やるよ")
        runSD.Main()
        filepath ='/home/akira/bot/temp/output.png'
        await message.channel.send(file=discord.File(filepath))




# Bot起動
client.run(config.DISCORD_TOKEN)
