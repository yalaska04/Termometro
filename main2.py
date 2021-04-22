from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    __temperaturaAnt = '' 
    
    def __init__(self):
        Tk.__init__(self)
        self.title('Termómetro')
        self.geometry('210x150')
        self.configure(bg='#ECECEC')
        self.resizable(0,0)
        
        self.temperatura = StringVar(value='') # variable de control (instancia) que admite cadenas como valor
        self.temperatura.trace('w', self.validateTemperature) # cada vez que sobre la variable temperatura se hace una modificación, me llama a la función validateTemperature
        self.tipoUnidad = StringVar(value='C')
        
        self.createLayout()
        
    def createLayout(self):
        # Buscar en la documentación
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10) # creamos el cuadrado de texto
        
        self.lblUnidad = ttk.Label(self, text='Grados').place(x=10, y=45)
        # ttk.Radiobutton = crear objeto Radiobutton
        self.rb1 = ttk.Radiobutton(self, text = 'Fahrenheit', variable=self.tipoUnidad, value='F', command=self.selected).place(x=20, y=70) 
        self.rb2 = ttk.Radiobutton(self, text = 'Celsius', variable=self.tipoUnidad, value='C', command=self.selected).place(x=20, y=95)

    def start(self):
        self.mainloop()
    
    def validateTemperature(self, *args):  # *args = espero una lista de datos (la tupla puede ir vacía)
        nuevoValor = self.temperatura.get() # cadena con lo que entra
        print('nuevoValor', nuevoValor, 'vs valorAnterior', self.__temperaturaAnt)
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor # mantenemos un valor anterior como backup que vamos actualizando
            print('fija valorAnterior a', self.__temperaturaAnt)
        except:
            self.temperatura.set(self.__temperaturaAnt) # recuperamos valor anterior
            print('recupera valor anterior', self.__temperaturaAnt)
    
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        
        self.temperatura.set(resultado)
        
if __name__ == '__main__':
    app = mainApp()
    app.start()