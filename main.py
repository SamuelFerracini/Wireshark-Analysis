import os
import datetime

now = datetime.datetime.now()

def paga_pal_muleque():
	os.system('clear')
	print('Analisador de rede e salvamento de dados (Baseado no Conte)')
	print('				Developed by: Pedro && Samuel')
	print('1 . Analise padrao (ip, host, protocolo)')
	print('2 . Apenas Ips e seus devidos Hosts')
	print('3 . Sair')
	o = raw_input('Resposta: ')
	if o == '1':
		analise_padrao()
	elif o == '2':
		analise_ips()
	elif o == '3':
		exit()
	else:
		print('Resposta invalida.')
		raw_input('Aperte enter para escolher novamente. ')
		os.system('clear')
		paga_pal_muleque()

def analise_padrao():
	os.system('clear')
	print('			Analise padrao')
	print('Sera analisado e salvo os dados de ip src, ip dst, protocol e entre outros.')
	print('Digite o tempo da analise em segundos')
	t = int(raw_input('Duracao: '))
	if t > 1 and t < 300:
		nome = raw_input('Digite o nome do arquivo para salvar os dados: ')
		path = '.'
		files = os.listdir(path)
		i=0
		for name in files:
			if name == nome:
				i=i+1
		if i != 0:
			print('Arquivo ja criado com o mesmo nome')
			raw_input('Aperte enter para voltar.')
			i=0
			analise_padrao()
		else:
			comando = "sudo tshark -i 'ens33' -a duration:" + str(t) + " > " + nome
			os.system(comando)
			
			
			menu_fim()
	else:
		print("Tempo de analise invalido")
		raw_input('Aperte enter para voltar. ')
		analise_padrao()
def menu_fim():
	os.system('clear')
	o = 0
	print("Concluido com exito!!")
	print('1 . Menu Principal')
	print('2 . Sair')
	o = raw_input('Resposta: ')
	if o == '1':
		paga_pal_muleque()
	elif o == '2':
		exit()
	else:
		print('Resposta invalida.')
		raw_input('Aperte enter para escolher novamente. ')
		os.system('clear')
		menu_fim()

def analise_ips():
	os.system('clear')
	print('			Analise de ips')
	print('Sera analisado e salvo apenas os dados de ip num determinado range, o que voce fara com isso nao implica na empresa, nao assumo esse B.O.')
	print('Digite o primeiro ip da rede (xxx.xxx.xxx.xxx)')
	ip1 = raw_input('Ip: ')
	print('Digite o o primeiro ip da rede (xxx.xxx.xxx.xxx)')
	ip2 = raw_input('Ip: ')
	
	print('Digite o tempo da analise em segundos')
	t = int(raw_input('Duracao: '))
	if t > 1 and t < 300:
		nome = raw_input('Digite o nome do arquivo para salvar os dados: ')
		path = '.'
		files = os.listdir(path)
		i=0
		for name in files:
			if name == nome:
				i=i+1
		if i != 0:
			print('Arquivo ja criado com o mesmo nome')
			i=0
		else:
			comando1 = "sudo tshark -f 'ip' -i 'ens33' -Tfields -eip.src -Y 'ip.src >= "

			comando2= " && ip.src <= "

			comando3= " -a duration:" + str(t) + " >> " + nome
			comando4 = comando1 + ip1 + comando2 + ip2 + "'" + comando3
			os.system(comando4)
			with open(nome) as f:
				c = f.readlines()
			c = [x.strip() for x in c]
			c.sort()
			vet = []
			x = 1
			for x in range(len(c)):
				if c[x] != c[x-1]:
					vet.append(c[x])
			f = open(nome, "w")
			f.write("Horario e dia da analise: %d/%d/%d - %d:%d:%d" %(now.day, now.month, now.year, now.hour, now.minute, now.second))
			f.write("\n\nIps encontrados: " + str(vet))
			f.write("\n\n")
			for x in range(len(vet)):
				os.system('nmblookup -A ' + vet[x] + " >> " + nome)
			f.write("\n\n")
			f.write("Lista de ips\n")
			os.system("arp -n >> " + nome)
			f.close()
			menu_fim()
	else:
		print("Tempo de analise invalido")

paga_pal_muleque()
		
