from time import sleep
import requests as r



while True:
	if (r.get('https://shopdt.ru').status_code == 200):
		print('Ping: Ok')
		break
	else:
		print('Ping: Fail')
		sleep(2)
