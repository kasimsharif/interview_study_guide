def makeAnagram(a, b):
    map_a = {}
    cnt = 0
    for each_char_a in a:
        map_a[each_char_a] = map_a.get(each_char_a, 0) + 1
    for each_char_b in b:
        if each_char_b in map_a.keys():
            map_a[each_char_b] = map_a[each_char_b] -1
            if map_a[each_char_b] == 0:
                map_a.pop(each_char_b)
        else:
            cnt+=1
    for each_value in map_a.values():
        cnt += each_value
    return cnt
