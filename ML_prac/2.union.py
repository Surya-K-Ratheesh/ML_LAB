def main():
    list1 = []
    list2 = []
    
    a = int(input("ENTER SIZE OF LIST 1: "))
    b = int(input("ENTER SIZE OF LIST 2: "))
    
    for i in range(0, a):
        j = int(input("ENTER VALUES FOR LIST 1: "))
        list1.append(j)
        
    print("")
        
    for i in range(0, b):
        j = int(input("ENTER THE VALUES OF LIST 2: "))
        list2.append(j)
        
    result = union_intersection(list1, list2)
    
    print(f"UNION = {result[0]}")
    print(f"INTERSECTION = {result[1]}")
    
    
def union_intersection(list1, list2):
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    return union, intersection



if __name__ == '__main__':
    main()