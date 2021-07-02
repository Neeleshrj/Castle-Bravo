import time
import yagmail

def logo():
    print("   _____          _   _        ____                       ")
    time.sleep(0.5)
    print("  / ____|        | | | |      |  _ \                      ")
    time.sleep(0.5)
    print(" | |     __ _ ___| |_| | ___  | |_) |_ __ __ ___   _____  ")
    time.sleep(0.5)
    print(" | |    / _` / __| __| |/ _ \ |  _ <| '__/ _` \ \ / / _ \ ")
    time.sleep(0.5)
    print(" | |___| (_| \__ \ |_| |  __/ | |_) | | | (_| |\ V / (_) |")
    time.sleep(0.5)
    print("  \_____\__,_|___/\__|_|\___| |____/|_|  \__,_| \_/ \___/ ")
    time.sleep(0.5)
    print("                                                          ")

    print("                  _.-^^---....,,--       ")
    print("              _--                  --_  ")
    print("             <                        >)")
    print("             |                         | ")
    print("              \._                   _./  ")
    print("                 ```--. . , ; .--'''       ")
    print("                       | |   |             ")
    print("                    .-=||  | |=-.   ")
    print("                    `-=#$%&%$#=-'   ")
    print("                       | ;  :|     ")
    print("              _____.,-#%&$@%#&#~,._____")
    menu()

def launchmenu(sender,reciever,subject,body,nukes):
    print("Sender:",sender)
    print("Reciever:",reciever)
    print("Subject:",subject)
    print("Body:",body)
    print("Nukes:",nukes)
    print('Enter 1 to Confirm and Launch')
    print('Enter 2 to re enter information')
    choice = input()
    if choice == '1':
        for i in range(nukes*10):
            yagmail.SMTP(sender).send(reciever,subject,body)
    elif choice == '2':
        inputs()
    else:
        print('Error')
        launchmenu(sender,reciever,subject,body,nukes)

    
def inputs():
    print('Enter the sender email')
    sender = input()
    print('Enter the reciever email')
    reciever = input()
    print('Enter the subject of the email')
    subject = input()
    print('Enter the body of the email')
    body = input()
    print("Amount of times to Nuke? 1 Nuke = 10 emails")
    nukes = int(input())

    launchmenu(sender,reciever,subject,body,nukes)
    

def menu():
    print("[1] Enter 1 to input details")
    print("[2] Enter any other key to exit")
    choice = input()
    if choice == '1':
        inputs()
    else:
        exit()

logo()
