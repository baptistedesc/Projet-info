from re import A


M=[['hugues','baptiste'],['12','2']]

print(type(M[0][0]))
print(type(M[1][1]))


# float(M[0][0])
# float(M[1][1])

# print(type(M[0][0]))
# print(type(M[1][1]))

if '1' or '2' or '3' or '4'or'5'or'6'or'7'or'8'or'9'or'0' in M[1][0]:
    M[1][0]=10
    
print(M)