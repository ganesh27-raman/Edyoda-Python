class Power:
   def pow_num(self, x, n):
        # if the x is 0 or 1 or n=1, the answer will 0 or 1 only
        if x==0 or x==1 or n==1:  
            return x
        # if the power of anything with zero will be always 1
        if n==0:
            return 1
        #if the power number is negative, the answer will come like (1/x^n)
        if n<0:
            return 1/self.pow_num(x,-n)

        val = self.pow_num(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(Power().pow_num(10, 2))
print(Power().pow_num(2, -3))
print(Power().pow_num(3, 2))