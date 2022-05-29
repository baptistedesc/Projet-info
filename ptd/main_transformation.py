from operation import Operation
from transformations.transformation import Transformation
from transformations.selection import Selection
from transformations.centrage import Centrage

from ptd.transformations.reduction import Reduction

data=[["id",1,2,3,4],["pop",10,50,64,87],["prenom","jul","hug","bap","ren"],["note",5,74,8,63]]
selection1 = Selection(data)


# print(selection1.execute("pop"))
# centrage1 = Centrage(data)
# print(centrage1.execute("pop"))
# reduction1 = Reduction(data)
# print(reduction1.execute("pop"))