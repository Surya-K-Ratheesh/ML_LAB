def main():
    nums1 = [1,2,3,4,5]
    nums2 = [3,4,5,6,7,8]
    
    print("ORIGINAL LIST")
    print(nums1)
    print(nums2)
    
    result = union_intersection(nums1, nums2)
    
    print("\nUNION OF TWO LISTS: ")
    print(result[0])
    
    print("\nINTERSECTION OF TWO LISTS: ")
    print(result[1])
    
    colours1 = ["Red", "Green", "Blue"]
    colours2 = ["Red", "White", "Pink", "Black"]
    
    print("ORIGINAL LIST")
    print(colours1)
    print(colours2)
    
    result = union_intersection(colours1, colours2)
    
    print("\nUNION OF TWO LISTS: ")
    print(result[0])
    
    print("\nINTERSECTION OF TWO LISTS: ")
    print(result[1])
    

def union_intersection(lst1, lst2):
    union = list(set(lst1) | set(lst2))
    intersection = list(set(lst1) & set(lst2))
    return union, intersection


if __name__ == '__main__':
    main()