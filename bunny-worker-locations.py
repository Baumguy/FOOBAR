def solution(x,y):
    def solution(x,y):
        #Creating a variable for "the maximum ID number based on distance from (1,1)"
        xyz=0
        #Defining the distance from (1,1)
        xy=x+y
        #Defining the maximum ID number based on distance from (1,1) by adding together the values from smaller distances
        #For example, 6+5+4+3+2+1
        while (xy) > 0:
            xyz=xyz+(xy-1)
            xy=(xy-1)
        #Subtracting the height-1 from the maximum ID possible, because they count from top to bottom and start at (1,1)    
        ID_Number=str(xyz-(y-1))
        return(ID_Number)
    
    
solution(5,10)
    
