class MyComplexNumber:

    def __init__(self,real=0,imag=0): #here self is a reference    #init is used for constructor
        print("MyComplexNumber constructor executing...")
        self.real_part=real
        self.imag_part=imag

    def displayComplex(self):
        print("{0}+{1}j".format(self.real_part,self.imag_part))

cmplx1=MyComplexNumber(40,50)
cmplx1.displayComplex()