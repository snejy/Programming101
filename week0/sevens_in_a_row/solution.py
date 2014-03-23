def sevens_in_a_row(arr,n):
    sevens=[]
    k=0
    if len(arr) == 0:
        return n == 0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==7:
                k=k+1
            if arr[j]!=7:
                sevens.append(k)
                k=0
    if n in sevens:
        return True
    else:
        return False
    k = (list(map(lambda x: x==7, arr)))


def main():
    print(sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
    print(sevens_in_a_row([1,7,1,7,7], 4))
    print(sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
    print(sevens_in_a_row([7,2,1,6,2], 1))

if __name__ == '__main__':
    main()