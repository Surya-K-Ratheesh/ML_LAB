def main():
    nums1 = [1,2,3,4,5]
    nums2 = [3,4,5,6,7,8]
    
    print("ORIGINAL LIST")
    print(nums1)
    print(nums2)
    
    result = union_intersection(nums1, nums2)
    
    print("\nUNION OF LISTS: ")
    print(result[0])
    
    print("\nINTERSECTION OF LISTS: ")
    print(result[1])
    
    colours1 = ["Red", "Green", "Blue"]
    colours2 = ["Red", "white", "Pink", "Black"]
    
    print("\nORIGINAL LIST")
    print(colours1)
    print(colours2)
    
    result = union_intersection(colours1, colours2)
    
    print("\nUNION OF LISTS: ")
    print(result[0])
    
    print("\nINTERSECTION OF LISTS: ")
    print(result[1])
    
    
def union_intersection(list1, list2):
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    return union, intersection
    

if __name__ == '__main__':
    main()