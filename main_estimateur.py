from operation import Operation
from estimateur import Estimateur
from moyenne import Moyenne
from variance import Variance
from sd import Sd
import matplotlib.pyplot as plt 
from boxplot import Boxplot


var1 = [2,2,2,5,5,15]
sd1 = Sd(var1)
data=[["id",1,2,3,4],["pop",10,50,64,87],["prenom","jul","hug","bap","ren"],["note",5,74,8,63]]
data2=[[1,2,3,4],[10,50,64,87],[5,74,8,63]]
data3=[["id",1,2,3,4],["pop",10,50,64,87],["note",5,74,8,63]]
moyenne1 = Moyenne(var1)
variance1 = Variance(var1)
sd1 = Sd(var1)


print(moyenne1.execute())
print(variance1.execute())
print(sd1.execute())

boxplot1 = Boxplot(data)
print(boxplot1)



