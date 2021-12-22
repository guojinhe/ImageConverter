# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:18:06 2021

@author: guojinhe
"""

#import
import tkinter as tk
from tkinter import ttk    ##Combobox
import cv2
import glob #img scanner

##Converter

def convert(source_folder_path,destination_folder_path,source_mode,destination_mode):
    
    modes = {
        ".Png":".png",
        ".Jpg/.Jepg":".jpg"
        }
    
    # img name scan
    dirPathPattern = source_folder_path + r'\*'+modes[source_mode]
    scan_result = glob.glob(dirPathPattern)


    for f in scan_result:
        # Load .png image
        img = cv2.imread(f)
    
        # Get img name(without path)
        f_e = [0]*(len(f)-len(source_folder_path)-5)

        for i in range(len(source_folder_path)+1, len(f)-4):
            f_e[i-len(source_folder_path)-1] = f[i]
       
        #f_e to img_name (conv to string)
        img_name = str(f_e[0])
        for i in range(1,len(f_e)):
            img_name += str(f_e[i])
        
        #set path to end folder
        f = destination_folder_path + '\\' + img_name
        # Save .jpg image
        cv2.imwrite(f + modes[destination_mode], img)

##DoneButton funtion 
def DoneButton_event():
    
    source_folder_path = source_var.get()
    destination_folder_path = destination_var.get()
    source_mode = Mode_Source.get()
    destination_mode = Mode_Destination.get()
    
    try:
        convert(source_folder_path,destination_folder_path,source_mode,destination_mode)
        tk.messagebox.showinfo('message',"Success!")
    except:
        tk.messagebox.showinfo('message',"SomeThingWrong!")
        
##background
root = tk.Tk()
root.title('ImageFormatConverter')
root.geometry('400x300')

##text
Toplabel_1 = tk.Label(root, text='ImageFormatConverter',font=('Arial', 18))
Toplabel_1.pack()

Toplabel_2 = tk.Label(root, text='made by PotatoCraft',font=('Arial', 9))
Toplabel_2.pack()


##select mode and input Source folder and Destination folder  
source_var = tk.StringVar()
destination_var = tk.StringVar()

#select Source  mode
Toplabel_Mode_Source = tk.Label(root, text='Select Source Mode:',font=('Arial', 12))
Toplabel_Mode_Source.pack()

Mode_Source = ttk.Combobox(root,
                                 values=[
                                    ".Jpg/.Jepg", 
                                    ".Png"],
                            state="readonly")
Mode_Source.pack()

#input Source  folder path
Source_Path_Inputlabel = tk.Label(root, text='Source Folder Path:',font=('Arial', 12))
Source_Path_Inputlabel.pack()
PicFrom = tk.Entry(root, textvariable=source_var)
PicFrom.pack()

#select Destination mode
Toplabel_Mode_Destination = tk.Label(root, text='Select Destination Mode:',font=('Arial', 12))
Toplabel_Mode_Destination.pack()

Mode_Destination = ttk.Combobox(root,
                                 values=[
                                    ".Jpg/.Jepg", 
                                    ".Png"],
                            state="readonly")
Mode_Destination.pack()

#input Destination folder path
Destination_Path_Inputlabel = tk.Label(root, text='Destination Folder Path:',font=('Arial', 12))
Destination_Path_Inputlabel.pack()
PicTo = tk.Entry(root, textvariable=destination_var )
PicTo.pack()



##setting done button
DoneButton= tk.Button(root, text='button', command=DoneButton_event)
DoneButton.pack()

root.mainloop()