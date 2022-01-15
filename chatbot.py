from tkinter import *
root = Tk()
def send():
   send= "You=>"+e.get()
   txt.insert(END,"\n"+send)
   if(e.get()=="hello"):
       txt.insert(END,"\n"+"Bot=>Hello")
   elif(e.get()=="hi"):
       txt.insert(END,"\n"+"Bot=>hi")
   elif(e.get()=="hey"):
       txt.insert(END,"\n"+"Bot=>what's up")
   elif(e.get()=="who created you"):
       txt.insert(END,"\n"+"Mk Mach did it")
   elif(e.get()=="what's the weather in embu?"):
       txt.insert(END,"\n"+"Bot=>The weather in embu is amazing as obvious")
   elif(e.get()=="How are you?"):
       txt.insert(END,"\n"+"Bot=>I'm fine, thanks you. how about you")
   elif(e.get()=="I'm fine, thanks"):
       txt.insert(END,"\n" +"Bot=>It's my pleasure having chat with you. besides, how can i help you, please?")
   elif(e.get()=="what's the price of HP laptop?"):
       txt.insert(END,"\n"+"Bot=>it's 65k with its transportation cost")
   elif(e.get()=="thanks you"):
       txt.insert(END,"\n"+"Bot=> You're welcome. please, make an arrangement to buy it")
   else:
       txt.insert(END,"\n"+"Bot=> I can't get you, please. come up again.")
   e.delete(0,END)
txt = Text(root)
txt.grid(row=0,column=0,columnspan=3)
e=Entry(root,width=100)
send=Button(root,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.bind('<Return>',send)
root.mainloop()
