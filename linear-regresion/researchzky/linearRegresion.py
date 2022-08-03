import matplotlib.pyplot as plt
import numpy as np


class SimpleLinearRegresion():

    def __init__(self,data):
        
        x,y = [],[]
        for i in data:
            x.append(i[0])
            y.append(i[1])
        
        self.x = x
        self.y = y
        self.sigma_x = sum(x)
        self.sigma_y_ = sum(y)
        self.sigma_x_pangkat_2 = sum([i**2 for i in x])
        self.sigma_y_pangkat_2 = sum([i**2 for i in y])
        self.sigma_xy = sum([i[0]*i[1] for i in data])

    def konstanta(sigma_y,sigma_x,len,sigma_x_pangkat_2,sigma_xy):
        return  ((sigma_y*sigma_x_pangkat_2)-(sigma_x*sigma_xy))/((len*sigma_x_pangkat_2)-sigma_x**2)

    def koefisien_regresi (len,sigma_xy,sigma_x,sigma_y,sigma_x_pangkat_2):
        return (((len*sigma_xy)-(sigma_x*sigma_y)))/((len*sigma_x_pangkat_2)-sigma_x**2)

    def prediksi(a,b,x):
        y = a + b * x
        return print(f'jika x nya {x} maka prediksi y nya adalah {y}')
    
    def show(self,x):

        a = SimpleLinearRegresion.konstanta(sigma_y=self.sigma_y_,sigma_x=self.sigma_x,len=len(self.x),sigma_x_pangkat_2=self.sigma_x_pangkat_2,sigma_xy=self.sigma_xy)
        b = SimpleLinearRegresion.koefisien_regresi(len=len(self.x),sigma_xy=self.sigma_xy,sigma_x=self.sigma_x,sigma_y=self.sigma_y_,sigma_x_pangkat_2=self.sigma_x_pangkat_2)

        result = SimpleLinearRegresion.prediksi(a=a,b=b,x=x)

        x_vis = np.array([0,50]).reshape(-1,1)
        y_vis = np.array([0.17857143, 48.39285714])


        plt.scatter(x=self.x,y=self.y)
        plt.title("generate data")
        plt.plot(x_vis,y_vis,'-r')
        plt.xlabel("X")
        plt.ylabel("Y")        
        plt.xlim(0,10)
        plt.ylim(0,10)
        plt.grid(True)
        plt.show()


        

        return result
    
