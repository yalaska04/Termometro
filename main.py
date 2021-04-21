import pygame, sys
from pygame.locals import *

class Termometro():
    
    def __init__(self):
        self.costume = pygame.image.load('imagenes/termo1.png')
        
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        
        return "{:10.2f}".format(resultado) 

class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad='C'):
        self.__costumes = []
        self.__costumes.append(pygame.image.load('imagenes/posiF.png'))
        self.__costumes.append(pygame.image.load('imagenes/posiC.png'))
        
        self.__tipoUnidad = unidad
        
    def costume(self):
        if self.__tipoUnidad == 'F':
            return self.__costumes[0]
        else:
            return self.__costumes[1]
    # como hemos creado  __tipoUnidad como atributo privado, para acceder a él
    # necesitamos un getter
    def unidad(self):
        return self.__tipoUnidad
    
    # para cambiar barra de F a C o C a F
    def change(self):
        if self.__tipoUnidad == 'F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
        
    

class NumberInput():
    __value = 0
    __strValue = ''
    __position = [0, 0]
    __size = [0, 0]
    __pointsCount = 0 
    
    def __init__(self, value =0):
        self.__font = pygame.font.SysFont('Arial', 24)
        # gestionar error
        self.value(value)
        
        '''
        No queremos repetirnos/este código lo tenemos en value:
        try:
            self.__value = int(value)
            self.__strValue = str(value)
        except:
            pass
        '''
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointsCount == 0): # para poder introducir decimales
                self.__strValue += event.unicode# para poder añadir nums al rect.
                self.value(self.__strValue)# actualiza el valor de value
                if event.unicode == '.':
                    self.__pointsCount += 1
            elif event.key == K_BACKSPACE:
                if self.__strValue[-1] == '.':
                    self.__pointsCount -= 1 # si el pointsCount es != 0 entonces viene aquí y se resta uno. Así que no se pueden meter más de 1 decimal
                self.__strValue = self.__strValue[:-1]# para poder borrar con la tecla borrado
                self.value(self.__strValue)
                        
     
    def render(self):
         # renderizar el bloque de texto/rectángulo transparente/como cuando creamo screen y luego hacemos blit
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        # queremos que el bloque sea un rectángulo
        # renderizamos el rectángulo
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        '''
        return {
            'fondo': rect,
            'texto': textBlock
            }
        '''
    
        return(rect, textBlock)
    
    # validaciones/setter para cambiar los valores de los atributos:
    def value(self, val=None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = float(val)
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
                    
            except:
                pass
         
    def width(self, val=None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
    
    def height(self, val=None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
        
     
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass
            
    def posX(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
    
    def posY(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
        
     
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass
        
class mainApp():
    termómetro = None
    entrada = None
    selector = None
    
    def __init__(self):
        # Aquí tengo que llamar a todas las clases que he definido anteriormente como atributos
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption('Termómetro')
        
        self.termometro = Termometro()
        self.entrada = NumberInput('0')
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28))
        
        self.selector = Selector()
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event) # me pasas el evento a on_event entrada 
                
                # cambia de unidades y cambia el valor del rectángulo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    print(temperatura)
                    self.entrada.value(temperatura)
            
            #pintamos el fondo de pantalla:
            self.__screen.fill((244, 236, 203))
    
            # pintamos el termómetro en su posición        
            self.__screen.blit(self.termometro.costume, (50, 34))
            
            # pintamos el cuadro de texto
            text = self.entrada.render() # obtenemos rectángulo blanco y foto de texto y lo asignamos a text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) # creamos el rectángulo blanco con sus datos (posición y tamaño) text[0]
            self.__screen.blit(text[1], self.entrada.pos())# pintamos la foto del texto (text[1])
            
            # pintamos el selector
            self.__screen.blit(self.selector.costume(), (112,153))
            
            pygame.display.flip()
                      
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()
