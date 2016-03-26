# recive un entero y retorna en romanos
class Conversor():
    NATURAL = 0
    ROMANO = ''
    ROMA = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    #        0    1    2    3    4    5    6

    def __init__(self,num):
        self.natural=num
        self.romano=Conversor.ROMA
        Conversor.calculadora(num)

    def calculadora(self,natural):

        r=[]
        #print(int((num%10)))        #cuatro
        #print(int((num/10)%10))        #tres
        #print(int((num/100)%10))       #dos
        #print(int((num/1000)%10))      #uno

        for x in range(int((natural/1000)%10)):              #L
            r.append(self.romano[3])
        for j in range(int((natural/100)%10)):               #X
            r.append(self.romano[2])
        for i in range(int((natural/10)%10)):                #V
            r.append(self.romano[1])
        for i in range(int((natural%10))):                   #I
            r.append(self.romano[0])
        return r

            #      I == 1
            #      V == 5
            #      X == 10
            #      L == 50
            #      C == 100
            #      D == 500
            #      M == 1000
if __name__=="__main__":
    o = Conversor(1234)
    print(o)

