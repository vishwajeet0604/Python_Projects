# Importing Libraries 
import io
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import webbrowser

# Defining a Class
class NewsApp:
    def __init__(self):
        # Fetch Data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=99115dbd82d64b9badb83d588c5887a3').json()

        # Initial GUi

        self.load_gui()


        # Load the 1st news item
        self.load_news_item(0)


    def load_gui(self):
        self.root  = Tk()
        self.root.geometry('500x600')
        self.root.resizable(0,0)
        self.root.configure(background= 'black')
        self.root.title('NewsApp')
        
        # Clear the Screen
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

    
        self.clear()

        #IMAGE EXTRACTION OF NEWS
        try:
            img_url =  self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            img=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img)
        #If image is not available then it will fetch from below link.
        except:
            img_url = 'https://image.shutterstock.com/image-vector/no-image-available-vector-illustration-260nw-744886198.jpg'
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(img)

        label = Label(self.root,image= photo)
        label.pack(pady=(4,10))

        #HEADINGS AND DETAILS OF NEWS
        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=400,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana,15'))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',wraplength=400, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana,12'))

        frame = Frame(self.root,bg='white')
        frame.pack(expand=True,fill=BOTH)

        # Impelementing the Buttons
        if index !=0:
            prev = Button(frame,text='Prev',width =24,height=3,command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=24, height=3,command=lambda:self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame, text='Next', width=24, height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()
    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()