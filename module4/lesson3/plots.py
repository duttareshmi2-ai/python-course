class Objects():
    import matplotlib.pyplot as plt
    import numpy as np
    plt.style.use("dark_background")
    def __init__(self,figure=plt.figure(),np=np,plt=plt):
        figure.canvas.manager.set_window_title("3D Objects")
        figure.set_facecolor("black")
        self.ax1 = figure.add_subplot(121 , projection = "3d")
        self.ax2 = figure.add_subplot(122 , projection = "3d")
        self.numpy=np
        self.sphere()
        self.cube()
        plt.show()
    def sphere(self):
        u = self.numpy.linspace(0 , self.numpy.pi , 100)
        v = self.numpy.linspace(0 , self.numpy.pi*2 , 100)
        x = self.numpy.outer(self.numpy.sin(u) , self.numpy.cos(v))
        y = self.numpy.outer(self.numpy.sin(u) , self.numpy.sin(v))
        z = self.numpy.outer(self.numpy.cos(u) , self.numpy.ones_like(v))
        self.ax1.plot_surface(x , y , z , cmap = "plasma" , edgecolor="none")
        self.ax1.set_box_aspect([1 , 1 , 1])
    def cube(self):
        r = [-1 , 1]
        for s in r :
            self.ax2.plot_surface(self.numpy.array([[s,s],[s,s]]),
                     self.numpy.array([[-1,1],[-1,1]]),
                     self.numpy.array([[-1,-1],[1,1]]),
                     color="red", alpha=0.9)
            self.ax2.plot_surface(self.numpy.array([[-1,1],[-1,1]]),
                     self.numpy.array([[s,s],[s,s]]),
                     self.numpy.array([[-1,-1],[1,1]]),
                     color="orange", alpha=0.9)
            self.ax2.plot_surface(self.numpy.array([[-1,1],[-1,1]]),
                     self.numpy.array([[-1,1],[-1,1]]),
                     self.numpy.array([[s,s],[s,s]]),
                     color="yellow", alpha=0.9)
Objects()