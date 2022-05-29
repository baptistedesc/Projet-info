def createList(name):
            result = {}
            for i in range(len(name)):
               nameList = name[i]
               result[nameList] = []
            return result



print(createList(['lala','eheh']))