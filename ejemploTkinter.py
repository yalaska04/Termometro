from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    size = '1024x768'
    
    def __init__(self):
        Tk.__init__(self)# instancia de Tk modificada de manera que yo soy la ventana/no tengo una ventana (quito root)
        
#       self.root = Tk()

        self.geometry(self.size) # crea ventana
        self.title('Mi ventana')
        self.configure(bg = 'blue')
    
    def start(self):
        self.mainloop() # que empiece a funcionar la pantalla
        

if __name__ == '__main__':
    app = mainApp()
    app.start() 

tkk.Button
ttk.Radiobutton
ttk.Entry