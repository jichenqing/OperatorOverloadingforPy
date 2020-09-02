# Submitter: chenqinj(Ji, Sue)
from _hashlib import new

class Poly:
    
    def __init__(self,*terms):
        self._terms=terms
        #print(self._terms)
        if len(self._terms)>1:
            
            for i in range(len(self._terms)):
                if i!=len(self._terms)-1:
                    if self._terms[i][1]<=self._terms[i+1][1]:
                        print('not in order')
                        raise AssertionError

        
        self.terms=dict()
        #print(self._terms)
        
        
        for term in self._terms:   
            
            if type(term)==list:
                for i in term:
                  
                    if len(i)!=0:
                        if type(i[0]) not in (int,float):
                            print('type of coefficient has to be int or float')
                            raise AssertionError
                            
                        if type(i[1])!=int:
                            raise AssertionError
                        if i[1]<0 :
                            pass
                        
                        else:
                            if i[0]!=0:
                                self.terms[i[1]]=i[0]
                    else:
                        self.terms={}  
            else:     
                if len(term)!=0:
                    if type(term[0]) not in (int,float):
                        print('type of coefficient has to be int or float')
                        raise AssertionError
                        
                    if type(term[1])!=int or term[1]<0 :
                        print('type of power has to be int and power has to be greater than 0')
                        raise AssertionError
                    
                    else:
                        if term[0]!=0:
                            self.terms[term[1]]=term[0]
                else:
                    self.terms={}                        
       
               
                    
    def __repr__(self):
        
        return 'Poly'+'{}'.format(self._terms)
    
     
    def __str__(self):
        if len(self.terms)==0:
            return str(0)
        string=''
        for power,coe in sorted(self.terms.items(),key=lambda x:-x[0]):        
            if coe<0:
                if power==0:
                    string+='- {} '.format(-coe)
                if coe==-1:
                    if power==1:
                        string+='- x '
                    if power>1:
                        string+='- x^{} '.format(power)
                else:
                    if power==1:
                        string+='- {}x '.format(-coe)
                    if power>1:
                        string+='- {}x^{} '.format(-coe,power)
            else:
                if coe==1:
                    if power==0:
                        string+='+ {} '.format(coe)
                    if power==1:
                        string+='+ x '.format(coe)
                    if power>1:
                        string+='+ x^{} '.format(power)
                else:
                    if power==0:
                        string+='+ {} '.format(coe)
                    if power==1:
                        string+='+ {}x '.format(coe)
                    if power>1:
                        string+='+ {}x^{} '.format(coe,power)
                
        if string[0]=='+':
            return string[2:-1]
        else:
            return string[0]+string[2:-1]
    
    
    def __bool__(self):
        if self.terms=={}:
            return False
        else:
            return True
        
    def __len__(self):
        po=[]
        if len(self.terms)==0:
            return 0
        for p in self.terms.keys():
            if p!=0:
                return self._terms[0][1]
            else:
                po.append(p)
        if len(po)==len(self.terms):
            return 0
    
        else:
            return self._terms[0][1]
    
    
    def __call__(self,n):
        
        e=self.__str__().replace('x','*('+str(n)+')')
        e=e.replace('^','**')
        return int(eval(e))
       

    def __iter__(self):
#         it=[]
#         print(self.terms)
#         for i in self.terms:
#            
#             it.append((self.terms[i],i))
#             
#         return it
#             

        class PH_iter:
            def __init__(self,term):
#                 self.terms = term          # sharing; sees mutation
                self.t = term  # copying; doesn't see it
                self.pow=sorted(self.t.keys(),key=lambda y:y,reverse=True)
                self._next = 0
             
            def gen_sorted(self,iterable,key=None,reverse=False):
                l = list(iterable)
                sorted(l,key=key,reverse=reverse)
                for i in l:
                    yield i
               
            def __next__(self):
                if self._next == len(self.t)+1:
                    raise StopIteration
                 
                answer = (self.gen_sorted(self.terms,lambda x:x[0],True)[self._next],self.pow[self._next])
                self._next += 1
                return answer
  
            def __iter__(self):
                return self
  
        return PH_iter(self.terms)
     
    
    def __getitem__(self,po):
        if type(po) !=int or po<0:
            raise TypeError
        else:
            if po in self.terms:
                return self.terms[po]
            else:
                return 0
    
    def __setitem__(self,po,nc):
        if type(po) !=int or po<0:
            raise TypeError
        else:
            if nc==0:
             
                for p in self.terms:
                    if self.terms[p]==nc:
                        if nc==0:
                            self.terms.pop(p)
            else:
                self.terms[po]+=nc
      
      
    def __delitem__(self,po):
        if type(po) !=int or po<0:
            raise TypeError
        else:
            if po in self.terms:
                self.terms.pop(po)

    def _add_term(self,co,po):
        #print(self.terms)
        if type(co) not in(int,float) or type(po)!=int or po<0:
            raise TypeError
        else:
            if po not in self.terms:
                if co!=0: 
                   
                    self.terms[po]=co
            else:
                if self.terms[po]+co!=0:
                    self.terms[po]+=co
                else:
                    self.terms.pop(po)
        
    
    def __pos__(self):
       # print({+p:+c for p,c in self.terms.items()})
        new=[]
        for p,c in self.terms.items():
            new.append((+c,+p))
        
        return str(Poly(new))
    def __neg__(self):
        #print({+p:-c for p,c in self.terms.items()})
        new=[]
        for p,c in self.terms.items():
            new.append((-c,p))
        
        return str(Poly(new))
    
    def abs(self):
        new=[]
        for p,c in self.terms.items():
            new.append((abs(c),p))
        
        return str(Poly(new))
    
    def differentiate(self):
        de=[]
        for k in self.terms.keys():
            
            de.append((k*self.terms[k],k-1))
            #de[k-1]=k*self.terms[k]
            #print(de)
        return Poly(de).__str__()
    
    def integrate(self,n=0):
        int=[]
        for k in self.terms:
            #print(k)
            
            int.append((self.terms[k]/(k+1),k+1))
            #int[k+1]=self.terms[k]/(k+1)
            int.append((n,0))
        return str(Poly(int))
    
    def def_integrate(self,n,m):
        
        return int(eval(self.integrate(n)))-int(eval(self.integrate(m)))
        
                
    
    def __add__(self,right):
        left=[]
        for po,co in self.terms.items():
            
            left.append(((co,po)))
        
        p=Poly(left)
        
        if type(right) ==Poly:
            #new=[]
            for po,co in right.terms.items():
                #new.append((po,co))
                
                p._add_term(co,po)
                
            return p

        if type(right) in (int,float):
#             n=left.terms[0]+=right
            left.append((right,0))
            return Poly(left)
            
        else:
            return TypeError
    
#     def __radd__(self,left):
#         
#         right=[]
#         for po,co in self.terms.items():
#             
#             right.append(((co,po)))
#         
#         p=Poly(right)
#         
#         if type(left) in (int,float):
#             right.append(left,0)
#             return Poly(right)
#             
#         else:
#             return TypeError

    def __sub__(self,right):
        left=[]
        for po,co in self.terms.items():
            
            left.append(((-co,po)))
        
        p=Poly(left)
        
        if type(right) ==Poly:
            #new=[]
            for po,co in right.terms.items():
                #new.append((po,co))
                
                p._add_term(-co,po)
                
            return p

        if type(right) in (int,float):
#             n=left.terms[0]+=right
            left.append((-right,0))
            return Poly(left)
            
        else:
            return TypeError
    
#     def __rsub__(self):
#         right=[]
#         for po,co in self.terms.items():
#             
#             right.append(((-co,po)))
#         
#         p=Poly(right)
#         
#         if type(left) in (int,float):
#             right.append(left,0)
#             return Poly(right)
#             
#         else:
#             return TypeError
    
    def __mul__(self,right):
        new={} 
        return Poly(self._terms*right._terms)
    
    def __power__(self,right):
        
        if right>=0:
            for k in self.terms.keys():
                self.terms[k*right]=self.terms[k]
                self.terms.pop(k)
                
        else:
            raise TypeError
    
    def __gt__(self,right):
        if type(right) ==Poly:
            for i in right.terms:
                for k in self.terms:
                    if k>i:
                        return True
                    if k==i:
                        return self.terms[k]>right.terms[i]
                    else:
                        return False
        if type(right) in (int,float):
            for i in self.terms:
                if i>right:
                    return True
                if i==right:
                    return self.terms[i]>right
                else:
                    return False
                    
        else:
            raise TypeError
    
    def __lt__(self,right):
        if type(right) ==Poly:
            for i in right.terms:
                for k in self.terms:
                    if k<i:
                        return True
                    if k==i:
                        return self.terms[k]<right.terms[i]
                    else:
                        return False
        if type(right) in (int,float):
            for i in self.terms:
                if i<right:
                    return True
                if i==right:
                    return self.terms[i]<right
                else:
                    return False
                    
        else:
            raise TypeError
    
    def __ge__(self,right):
        if type(right) ==Poly:
            for i in right.terms:
                for k in self.terms:
                    return k>=i
                        
    
        if type(right) in (int,float):
            for i in self.terms:
                return i>=right
                   
                    
        else:
            raise TypeError
    
    def __le__(self,right):
        if type(right) ==Poly:
            for i in right.terms:
                for k in self.terms:
                    return k<=i
                        
    
        if type(right) in (int,float):
            for i in self.terms:
                return i<=right
                   
                    
        else:
            raise TypeError
    
    def __eq__(self,right):
        
        if type(right)==Poly:
            return right._terms==self._terms
        else:
            raise TypeError        
    
    def __ne__(self,right):
        if type(right)==Poly:
            return right._terms!=self._terms
        else:
            raise TypeError
    
#     def __setattr__(self):
#         pass


if __name__ == '__main__':
#     Simple tests before running driver
#     Put your own test code here to test Poly before doing bsc tests
   
#     print('Start of simple tests')
#     p = Poly((3,2),(-2,1),(4,0))
#     print('  For Polynomial: 3x^2 - 2x + 4')
#     print('  str(p):',p)
#     print('  repr(p):',repr(p))
#     print('  len(p):',len(p))
#     print('  p(2):',p(2))
#     print('  list collecting the iterator results:', [t for t in p])
#     print('  p+p:',p+p)
#     print('  p+2:',p+2)
#     print('  p*p:',p*p)
#     print('  p*2:',p*2)
#     print('End of simple tests\n\n')
       
    import driver
    driver.default_file_name = 'bscp22W18.txt'
#     driv9er.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()     
