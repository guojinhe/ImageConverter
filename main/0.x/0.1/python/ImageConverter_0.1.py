# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:57:21 2021

@author: guojinhe
"""
#import
import tkinter as tk
import cv2
import glob #img scanner

##Converter

def convert(start_folder_path,end_folder_path):

    # img name scan
    dirPathPattern = start_folder_path + r'\*.png'
    scan_result = glob.glob(dirPathPattern)


    for f in scan_result:
        # Load .png image
        img = cv2.imread(f)
    
        # Get img name(without path)
        f_e = [0]*(len(f)-len(start_folder_path)-5)

        for i in range(len(start_folder_path)+1, len(f)-4):
            f_e[i-len(start_folder_path)-1] = f[i]
       
        #f_e to img_name (conv to string)
        img_name = str(f_e[0])
        for i in range(1,len(f_e)):
            img_name += str(f_e[i])
        
        #set path to end folder
        f = end_folder_path + '\\' + img_name
        # Save .jpg image
        cv2.imwrite(f + '.jpg', img)

##DoneButton funtion
def DoneButton_event():
    
    start_folder_path = var1.get()
    end_folder_path = var2.get()
    print(start_folder_path)
    print(end_folder_path)
    convert(start_folder_path,end_folder_path)
    tk.messagebox.showinfo('message',"Success")
"""if(start_folder_path == 'awa'):
        tk.messagebox.showinfo('message',"Success")
    else:
        tk.messagebox.showinfo('message',"SomeThingWrong")"""
        
##background
root = tk.Tk()
root.title('ImageFormatConverter')
root.geometry('400x300')

##text
Toplabel_1 = tk.Label(root, text='ImageFormatConverter',font=('Arial', 18))
Toplabel_1.pack()

Toplabel_2 = tk.Label(root, text='made by PotatoCraft',font=('Arial', 9))
Toplabel_2.pack()

##input start folder and end folder  
var1 = tk.StringVar()
var2 = tk.StringVar()

Inputlabel_1 = tk.Label(root, text='Picture(.png) from:',font=('Arial', 12))
Inputlabel_1.pack()
PicFrom = tk.Entry(root, textvariable=var1)
PicFrom.pack()

Inputlabel_2 = tk.Label(root, text='Picture(.jpg) to:',font=('Arial', 12))
Inputlabel_2.pack()
PicTo = tk.Entry(root, textvariable=var2 )
PicTo.pack()



##setting done button
DoneButton= tk.Button(root, text='button', command=DoneButton_event)
DoneButton.pack()

root.mainloop()