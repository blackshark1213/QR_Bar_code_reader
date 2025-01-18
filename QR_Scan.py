# ! NOTE ->  change path of image save as per your file.

import tkinter as tk

def gui(text_):
    root = tk.Tk()
    root.geometry('720x100')
    root.minsize(200,100)
    lab1 = tk.Label(text=f"{text_}",font=('Arial',25))
    lab1.pack()
    root.mainloop()
    pass
if __name__== '__main__':  
    import cv2
    import os
    import time as t 
    from PIL import Image
    from colorama import Fore as color
    from pyzbar.pyzbar import decode
    
    cap=cv2.VideoCapture(0)
    while True:
        ret,fm = cap.read()
        gray = cv2.cvtColor(fm, cv2.COLOR_BGR2GRAY)
        cv2.imshow('camera',gray)
        cv2.waitKey(100)
        
        if ret:
            cv2.imwrite('/tmp/QR_Scan.png',fm)
            data = decode(Image.open('/tmp/QR_Scan.png'))
            data=str(data)
            find =None
            if ((('D'or'd') in data)):
                break
            if cv2.waitKey(1) & 0xFF == ord("q") or 0xFF == ord('Q'):
                exit(0)
    store=[]

    txt =None
    try:
            find=data.index("b'")
            find2=data.index('type')
            print(color.GREEN+"Full QR Data \n\t"+data)
            print("\nQR Data : \t")
            for i in range (find+1,find2-2):
                    # print(data[i],end='')
                    store.append(data[i])
            txt=''.join(store)
            print(color.BLUE+f'{txt}')
            t.sleep(100)
            # gui(txt) 
    except:
        print("Error while reading QR")

    # Delete picture 
    os.system('rm /tmp/QR_Scan.png')
