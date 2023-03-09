
def twoSum(lst, target):
    storei=0
    storej=0

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                storei = i
                storej = j
                print('[',storei, ',', storej, ']')
                break
    
    return 
ll = []
templl = list(input('input list value').split())
ll.append(templl)
tg = list(input('input target'))
twoSum(ll, tg)

    