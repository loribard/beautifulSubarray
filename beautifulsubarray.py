def  beautifulSubarrays(a, m):
    array = []
    array_list = []
    odds = []
    for item in a:
        if item % 2 != 0:
            odds.append("odd")
        else:
            odds.append("even")
    print "ODDS", odds
    if odds.count("odd") < m:
        return 0
    if odds.count("odd") == m and len(odds) == m:
        return m

    for i in range(len(odds)):
        for j in range(i+m, len(odds) + 1):
            print i, j, odds[i:j]
            if odds[i:j].count("odd") == m:
                array_list.append(a[i:j])
                print array_list

                
                

                   
                    


print beautifulSubarrays([2,5,4,9], 3)
print beautifulSubarrays([5,9], 2)
print beautifulSubarrays([5,9,7], 2)
print beautifulSubarrays([2,5,4,9], 2)
print beautifulSubarrays([2,5,4,9], 1)
print beautifulSubarrays([0,2,5,4,9], 1)


