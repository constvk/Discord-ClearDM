import discord
import os
import datetime
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred
from colorama import Fore, init
init(convert=True)

print(f"[{Fore.RED}^{Fore.RESET}] TOKEN")
token = input("[>] ")


print(" ")
print(f"[{Fore.RED}^{Fore.RESET}] PREFIXO")
prefix = input("[>] ")


os.system('cls')

print(" ")
class MyClient(discord.Client):
  async def on_connect(self):
    os.system('cls')
    print(" ")
    print(f"{Fore.RED}  █████╗ ██╗    ██╗ █████╗ ██╗████████╗██╗███╗   ██╗ ██████╗  {Fore.RESET}")
    print(f"{Fore.RED} ██╔══██╗██║    ██║██╔══██╗██║╚══██╔══╝██║████╗  ██║██╔════╝  {Fore.RESET}")
    print(f"{Fore.RED} ███████║██║ █╗ ██║███████║██║   ██║   ██║██╔██╗ ██║██║  ███╗ {Fore.RESET}")
    print(f"{Fore.RED} ██╔══██║██║███╗██║██╔══██║██║   ██║   ██║██║╚██╗██║██║   ██║ {Fore.RESET}")
    print(f"{Fore.RED} ██║  ██║╚███╔███╔╝██║  ██║██║   ██║   ██║██║ ╚████║╚██████╔╝ {Fore.RESET}")
    print(f"{Fore.RED} ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝  {Fore.RESET}")
    print(f"{Fore.WHITE} ----------------------------- / ---------------------------- {Fore.RESET}")
    print("     ")
    print("    Youtube: Const | Discord: Const#9999 ")
    print("     ")
    print(f"[{Fore.RED}!{Fore.RESET}] Logado com Sucesso!")
    print(f"[{Fore.RED}/{Fore.RESET}] {prefix}help")
    print("     ")
    print(f"{Fore.WHITE} ----------------------------- / ---------------------------- {Fore.RESET}")
    print("     ")
# Reg.comandos
  async def on_message(self, message):
    if message.author != client.user:
      return
    if message.content == f"{prefix}help":
      await help(message)
    if message.content == f"{prefix}apagar":
      await channelclear(message)

# log cliente
async def logout(message):
  await message.delete()
  await client.logout()
  print(f"\n Cliente Logado com Sucesso!")

# comando de help
async def help(message):
  await message.delete()
  emHelp = discord.Embed(
    description = f"""
**
[-] {prefix}help
Mostra esta mensagem.
 
[-] {prefix}apagar
Limpar suas mensagens no canal.
**
    """)
  emHelp.set_author(name = "Comandos", icon_url = client.user.avatar_url, url = "https://media.discordapp.net/attachments/820955486606196736/832416377444499506/36b87512eb2ac4dd49550b6c00a2c86a.png")
  emHelp.set_footer(text = "Youtube: Const")
  try:
    await message.channel.send(embed = emHelp, delete_after = 15)
  except:
    await message.channel.send(
      """
**
[-] {prefix}help
Mostra esta mensagem.
 
[-] {prefix}apagar
Limpar suas mensagens no canal.
**
""",
     delete_after = 15
    )

async def channelclear(message):
  await message.delete()
  print(f"[{Fore.RED}+{Fore.RESET}] Deletando...")
  async for message in message.channel.history(limit=None):
    if message.author == client.user and message.type == discord.MessageType.default:
      await message.delete()
  print(f"[{Fore.RED}!{Fore.RESET}] Tarefa Concluida!\n")

client = MyClient()
try:
  client.run(token, bot = False)
except discord.LoginFailure:
  print(f"Client failed to log in. [Invalid token]")
except discord.HTTPException:
  print(f"Client failed to log in.[Unknown Error]")
