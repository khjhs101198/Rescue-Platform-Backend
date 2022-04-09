def lightpoles_phaseToarray(phases):
    arr = [-1]
    for i in phases :
        
        if( '0' <= i and i <= '9'):
            arr.append(int(i))
    return arr

# for i in lightpoles_phaseToarray("1,2,1,6,5") :
#     print(i)