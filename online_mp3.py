# _*_ coding:utf-8 _*_
from tkinter import *
import tkMessageBox
import urllib
import json
import mp3play

def music():
    text = entry.get()
    text = text.encode('utf-8')
    text = urllib.quote(text)
    if not text:
        tkMessageBox.showinfo('温馨提示', '您可以输入以下内容进行搜索\n1.歌曲名\n2.歌手名\n3.部分歌词')
        return
    html=urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=9' %text).read()
    text = json.loads(html)
    list_s = text['result']['songs']
    list_url = []
    global list_url
    list_name = []
    global list_name
    listbox.delete(0,listbox.size())
    for i in list_s:
        listbox.insert(END,i['name']+ "("+i['artists'][0]['name']+")")
        list_url.append(i['audio'])
        list_name.append(i['name'])

def play(event):
    global mp3
    sy = listbox.curselection()[0]
    mp3 = mp3play.load(list_url[sy])
    mp3.play()
    urllib.urlretrieve(list_url[sy], list_name[sy] + '.mp3')

root = Tk()
root.title("Tkinter Music")
root.geometry('+300+100')
entry = Entry(root)
entry.pack()
button = Button(root,text='搜索歌曲',command=music)
button.pack()
listbox = Listbox(root,width=50)
listbox.bind('<Double-Button-1>',play)
listbox.pack()
mainloop()
