import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import TextBox,Button

def addBinary(a,b):
        a = int(a,2)
        b = int(b,2)
        res=bin(a+b)[2:];
        if(a+b>2**16-1):
            res=bin(a+b-2**16+1)[2:]
            while(len(res)<16):
                res="0"+res
        return res

def inverse(str):
    invStr=""
    for eachbit in str:
        if eachbit=="1":
           invStr+="0"
        else:
           invStr+="1"
    return invStr


def submit():
    sum1=addBinary(textbox1.text,textbox2.text)
    sum2=addBinary(sum1,textbox3.text)
    inv=inverse(sum2)
    res=addBinary(inv,sum2)
    return res

textbox1 = TextBox(plt.axes([0.3, 0.8, 0.5, 0.075]), 'number1',"0110011001100000")
textbox2 = TextBox(plt.axes([0.3, 0.7, 0.5, 0.075]), 'number2',"0101010101010101")
textbox3 = TextBox(plt.axes([0.3, 0.6, 0.5, 0.075]), 'number3',"1000111100001100")
textbox4 = TextBox(plt.axes([0.3, 0.5, 0.5, 0.075]), "result",submit())
plt.show()

