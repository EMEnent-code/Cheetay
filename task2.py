def printLargest(my_list):
    result = []
    print('Input:', my_list)
    while len(my_list) != 0:
        mynumber = []
        Max_length = len(str(max(map(int, my_list))))
        if Max_length == 2:
            one = []
            two = []
            for i in range(len(my_list)):
                one.append(my_list[i][:1])
                two.append(my_list[i][1:2])
        elif Max_length == 3:
            one = []
            two = []
            three = []
            for i in range(len(my_list)):
                one.append(my_list[i][:1])
                two.append(my_list[i][1:2])
                three.append(my_list[i][2:3])
        indices = []
        for i in range(len(one)):
            if one[i] == max(one):
                indices.append(i)
        for i in range(len(indices)):
            x = indices[i]
            if Max_length == 2:
                number = one[x] + two[x]
                mynumber.append(number)
            else:
                number = one[x] + two[x] + three[x]
                mynumber.append(number)
        mynumber = sorted(mynumber, reverse=True)
        for i in range(len(mynumber)):
            mynumber[i] = mynumber[i].replace(' ', '')
        for i in mynumber:
            result.append(i)
            my_list.remove(i)
    result = ''.join(result)
    print('Output: ', result)


# my_list = ['54', '546', '548', '60']
my_list = ['3', '30', '34', '5', '9']
printLargest(my_list)
