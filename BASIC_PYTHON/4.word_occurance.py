def main():
    print(word_count(input("ENTER A STRING: ")))
    
def word_count(str):
    counts = dict()
    words = str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        
        else:
            counts[word] = 1
    
    return counts


if __name__ == '__main__':
    main()  