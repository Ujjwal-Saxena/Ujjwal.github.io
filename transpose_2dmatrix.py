def transpose(l1, l2): 
  
    for i in range(len(l1[0])):
        row =[] 
        for item in l1:  
            row.append(item[i]) 
        l2.append(row) 
    return l2 
if __name__=='__main__':
	l1 = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]] 
	l2 = [] 
	print(transpose(l1, l2))