import telepot
import time
from telepot.loop import MessageLoop

bot = telepot.Bot("442666691:AAG_7-BFUlaEq5QkVEyLAwXOIWUg_3dIreA")

def calcular_nota(resto):
	notas = resto.split(' ')
	suma = 0.0
	for nota in notas:
		nota = float(nota)
		if nota > 7:
			nota = nota / 10.0
		suma += nota
	promedio = suma / len(notas)
	if len(notas) > 2:
		#promedio * 0.6 + examen * 0.4 >= 3.95
		return (3.95 - promedio * 0.6) / 0.4
	else:
		return (3.95 - promedio * 0.5) / 0.5


def handle(msg):
	chat_id = msg['chat']['id']
	mensaje = msg['text']
	mensaje_separado = mensaje.split(' ', 1)
	comando = mensaje_separado[0]
	resto = mensaje_separado[1]
	if comando.startswith('/nota'):
		nota = calcular_nota(resto)
		if nota > 7:
			bot.sendMessage(chat_id, 'gg')
		else:
			respuesta = "La nota que necesitas es un " + str(nota)
			bot.sendMessage(chat_id, respuesta)

MessageLoop(bot, handle).run_as_thread()

while 1:
	time.sleep(10)
