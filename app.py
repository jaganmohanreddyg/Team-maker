import random
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
put_text("Online Team maker").style("color:#5EBEC4; font-size:30px ;font-weight: bold")
info = input_group("Group inputs", [
	input('Enter names in the same manner as shown below', name='txt',placeholder="perlu type chey ra huka EX:{raakhi,shakthi,rabhasa}",style="color:#F92C85;font-weight: bold"),
	input('Enter team size', name='ts',style="color:#F92C85;font-weight: bold")])

# txt="jagan,jaggu,anu,lax,narayana,adi,geetha,krishna,krish"
mem = info['txt'].split(",")

t=int(len(mem)/int(info['ts']))

for i in range(0,t):
    tm=""
    for j in range(0,int(info['ts'])):
        tm=tm+str(mem.pop(random.randrange(len(mem))))+" "

    put_text("TEAM"+str(i+1)+" => "+tm).style("color:#5EBEC4; font-size:30px ;font-weight: bold")

put_image(open("mg.jpg",'rb').read(),width="",height="")


