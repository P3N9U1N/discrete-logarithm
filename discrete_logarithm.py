import labmath

class DiscreteLogarithm:
    """Class for calculating the discrete logarithm. It is efficient if the multiplicative order is a smooth number.
    """
    @property
    def base(self):
        return self.__base
    @property
    def mod(self):
        return self.__mod
    @property
    def order(self):
        return self.__order
   
    def __init__(self,base:int,mod:int):
        """Parameters
        ----------
        base : int      
        mod : int
        Must be a prime
        """
        self.__base=base
        self.__mod=mod        
        self.__order=labmath.multord(base,mod)
        self.__factors=list(labmath.primefac(self.__order))
        
        

        #for c in range(mod):
        #    v=pow(base,c,mod)
        #    print(v)

        d=self.order
        factors=self.__factors      
        self.__giant_steps={}
        giant_steps=self.__giant_steps
        for f in factors:    
            d=d//f
            cache={}
            giant_steps[d]=cache
            size=pow(base,d,mod)
            value=1
            for i in range(f-1,-1,-1):                
                value= (value*size) % mod
                cache[value]=i
            base=pow(base,f,mod)  
        pass


 
 

    def calc(self,value:int)->int:
        "Calculates discrete logarithm. Returns -1 if no result exists."
        mod=self.mod
        d=self.order
        factors=self.__factors
        giant_steps=self.__giant_steps
        base=self.base
        steps=0
        step=1       
        for f in factors:    
            d=d//f
            cache=giant_steps[d]
            start=pow(value,d,mod)    
            if start != 1:
                size=pow(base,d,mod)

                offset=cache.get(start)
                if offset is None: return -1 

                value=(value*pow(base,offset,mod)) % mod
                steps=steps+step*offset 

            base=pow(base,f,mod)   
            step*=f
        return self.order-steps


