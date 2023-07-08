
def draw(n):  

    base = n-1
    oks = 1


    print('o' * n + 'x')
    for len in range(n):
        
# adding o's
        if n - base > 0:
            print('o' * base + 'x' + 'o' * oks)
        
# checking if there's space for one more line

        if base - 1 > 0:
            base = base - 1        
            oks = oks + 1

# finishing off with the last line starting with x
        else:
            print('x' + 'o' * (oks+1))
            break
        



