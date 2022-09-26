import telebot
from telebot import types
from os import listdir
import config

bot = telebot.TeleBot(token=config.API_KEY)
	
@bot.message_handler(commands = ['start'])
def start(message: telebot.types.Message):  ### previous bug (message) -> solved (message: tlebot.types.Message)
	send_mess = f"<b>Ողջույն {message.from_user.first_name} {message.from_user.last_name}</b>!\nՑանկանու՞մ եք օգտվել մեր տուր-արշավներից։"
	
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
	btn1 = types.KeyboardButton('ԱՅՈ')
	btn2 = types.KeyboardButton('ՈՉ')
	fb = types.KeyboardButton('/facebook')
	markup.add(btn1, btn2, fb)

	bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup)

@bot.message_handler(commands = ['facebook'])
def open_website(message: telebot.types.Message):
	send_mess = 'Մեր մասին կարող եք տեղեկանալ նաև ֆեյսբուքյան էջից։'

	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton('Անցնել հղումով։', url="https://www.facebook.com/onewaytour"))
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types = ['text'])
def text(message: telebot.types.Message):
	get_message_bot = message.text.strip().upper()

	if get_message_bot == 'ԱՅՈ':
		send_mess = "Շատ լավ։ Ու՞ր կուզենայիք գնալ։"
		
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
		hh = types.KeyboardButton('ՀՀ ՄԱՐԶԵՐ ԵՎ ԱՐՑԱԽ')
		abroad = types.KeyboardButton('ԱՐՏԵՐԿԻՐ')
		markup.add(hh, abroad)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup)

	elif get_message_bot == 'ՀՀ ՄԱՐԶԵՐ ԵՎ ԱՐՑԱԽ':
		send_mess = "Ընտրեք մարզը։"

		markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
		btn1 = types.KeyboardButton('ԼՈՌԻ')
		btn2 = types.KeyboardButton('ՏԱՎՈՒՇ')
		btn3 = types.KeyboardButton('ՇԻՐԱԿ')
		btn4 = types.KeyboardButton('ԱՐԱԳԱԾՈՏՆ')
		btn5 = types.KeyboardButton('ԿՈՏԱՅՔ')
		btn6 = types.KeyboardButton('ԱՐՄԱՎԻՐ')
		btn7 = types.KeyboardButton('ԱՐԱՐԱՏ')
		btn8 = types.KeyboardButton('ՎԱՅՈՑ ՁՈՐ')
		btn9 = types.KeyboardButton('ՍՅՈՒՆԻՔ')
		btn10 = types.KeyboardButton('ԳԵՂԱՐՔՈՒՆԻՔ')
		btn11 = types.KeyboardButton('ԱՐՑԱԽ')
		btn = types.KeyboardButton('ՆԱԽՈՐԴ ՄԵՆՅՈՒ')
		contact = types.KeyboardButton('ԿԱՊ ՄԵԶ ՀԵՏ')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn, contact)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup)

	elif message.text == 'ԼՈՌԻ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"

		directory = "media/lori"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

	elif message.text == 'ՏԱՎՈՒՇ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"

		directory = "media/tavush"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

	elif message.text == 'ԱՐԱԳԱԾՈՏՆ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"

		directory = "media/aragacotn"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')
		

	elif message.text == 'ԳԵՂԱՐՔՈՒՆԻՔ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"

		directory = "media/gegharquniq"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')
	
	elif message.text == 'ԿՈՏԱՅՔ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"
		
		directory = "media/kotayq"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

	elif message.text == 'ՇԻՐԱԿ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"

		directory = "media/shirak"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')


	elif message.text == 'ՍՅՈՒՆԻՔ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"

		directory = "media/syuniq"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')


	elif message.text == 'ՎԱՅՈՑ ՁՈՐ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"
		
		directory = "media/vayocdzor"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

	elif message.text == 'ԱՐՑԱԽ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"

		directory = "media/artsakh"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

	elif message.text == 'ԱՐՄԱՎԻՐ':
		send_mess = "Այս պահին այդ ուղղությամբ տուրեր չկան։"

		directory = "media/armavir"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

	elif message.text == 'ԱՐԱՐԱՏ':
		send_mess = "Այս պահին այդ ուղղությամբ տուրեր չկան։"

		directory = "media/ararat"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

	elif message.text == 'ԱՐՏԵՐԿԻՐ':
		send_mess = "Առաջարկում ենք Ձեզ հետևյալ տարբերակները։"

		markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
		btn = types.KeyboardButton('ՆԱԽՈՐԴ ՄԵՆՅՈՒ')
		contact = types.KeyboardButton('ԿԱՊ ՄԵԶ ՀԵՏ')
		markup.add(btn, contact)

		directory = "media/arterkir"
		photos = list()
		formats = ['.jpg', '.jpeg', '.png']
		for i in formats:
			for j in filter(lambda x: x.endswith(i), listdir(directory)):
				photos.append(j)
		for i in photos:
			with open(f"{directory}/{i}", 'rb') as photo:
				bot.send_photo(chat_id=message.chat.id, photo=photo)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')
		
	elif message.text == 'ՆԱԽՈՐԴ ՄԵՆՅՈՒ':
		send_mess = "Տեսեք մեր մյուս առաջարկները։"

		markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
		hh = types.KeyboardButton('ՀՀ ՄԱՐԶԵՐ ԵՎ ԱՐՑԱԽ')
		abroad = types.KeyboardButton('ԱՐՏԵՐԿԻՐ')
		markup.add(hh, abroad)

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup)

	elif message.text == 'ԿԱՊ ՄԵԶ ՀԵՏ':
		send_mess = "Հասցե։				\nՀեռ․				\nԷլ․ Փոստ։				"

		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')

	else:
		send_mess = 'Միշտ ուրախ կլինենք տեսնել Ձեզ մեր արշավներին։'
		bot.send_message(message.chat.id, send_mess, parse_mode = 'html')
	

bot.polling(non_stop = True, interval=0)