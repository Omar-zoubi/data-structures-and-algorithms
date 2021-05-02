li =[1,2,3,4,5,6]
res =[]

def reverseArray(list):
    var = len(list)
    var=var-1
    for i in list :
      res.insert(i,list[var]) 
      
      var =var-1
    print(res)
reverseArray(li)