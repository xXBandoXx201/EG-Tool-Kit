#!/usr/bin/python
#coding: utf-8
#Code By : Gad
import requests, json

logo = """ 
 ______ _____ _______          _ _  ___ _   
|  ____/ ____|__   __|        | | |/ (_) |  
| |__ | |  __   | | ___   ___ | | ' / _| |_ 
|  __|| | |_ |  | |/ _ \ / _ \| |  < | | __|
| |___| |__| |  | | (_) | (_) | | . \| | |_ 
|______\_____|  |_|\___/ \___/|_|_|\_\_|\__|   \n                                   
                         Facebook Tool Kit By Gad\n
https://www.facebook.com/AhmedGadga , @Gad990>>>> Telegrame
"""
print(logo)
Rating = print('1.Rating FaceBook page By Token>>')
auto_share = print('2.Auto Share By Token>>')
auto_like = print('3.Auto Like By Token>>')
auto_follow = print('4.Auto Follow By Token>>')
auto_poke = print('5.Auto Poke By Token >>>>>')

chosse = input('Enter Number>>')

if(int(chosse)== 1):
    id_page = input('Enter ID >>')
    rat = input('Enter Ratting >>')
    token = input('Enter token Folder >>')
    var = open(token, 'r').readlines()
    for line in var:
        token = line.strip()
        url = 'https://graph.facebook.com/' + id_page + '/ratings?Name=goodpagegoodpostsgoodadminsgoodpagegoodpostsgoodadmins&rating=' + rat + '&access_token=' + token + '&method=post'
        http = requests.post(url)
        content = http.content
        data = json.loads(content.decode("utf-8"))
        print(data)
elif (int(chosse) == 2):
    id_post = input('Enter ID Of Post >>')
    token = input('Enter token Folder >>')
    var = open(token, 'r').readlines()
    for line in var:
        token = line.strip()
        url = 'https://graph.facebook.com/'+id_post+'/sharedposts?access_token=' + token + '&method=post'
        http = requests.post(url)
        content = http.content
        data = json.loads(content.decode("utf-8"))
        print(data)
elif (int(chosse) == 3):
    id_post = input('Enter ID Of Post >>')
    token = input('Enter token Folder >>')
    var = open(token, 'r').readlines()
    for line in var:
        token = line.strip()
        url = 'https://graph.facebook.com/'+id_post+'/likes?access_token='+token+'&method=post'
        http = requests.post(url)
        content = http.content
        data = json.loads(content.decode("utf-8"))
        print(data)
elif(int(chosse)== 4):
    id_profile = input('Enter ID Of profile >>')
    token = input('Enter token Folder >>')
    var = open(token, 'r').readlines()
    for line in var:
        token = line.strip()
        url = 'https://graph.facebook.com/'+id_profile+'/subscribers?access_token='+token+'&method=post'
        http = requests.post(url)
        content = http.content
        data = json.loads(content.decode("utf-8"))
        print(data)
elif(int(chosse)== 5):
    id_profile = input('Enter ID Of profile >>')
    token = input('Enter token Folder >>')
    var = open(token, 'r').readlines()
    for line in var:
        token = line.strip()
        url = 'https://graph.facebook.com/'+id_profile+'/pokes?access_token='+token+'&method=post'
        http = requests.post(url)
        content = http.content
        data = json.loads(content.decode("utf-8"))
        print(data)
