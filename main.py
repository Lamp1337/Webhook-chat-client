from dhooks import Webhook
import os

os.system("cls & title Webhook chat client & color d")
link = input("Enter Webhook Link : ")

hook = Webhook(link)
os.system('cls')
print("""---------------------
Webhook chat client
---------------------""")

while True:
    try:
        msg = input("Message: ")
        hook.send(msg)
    except:
        pass
