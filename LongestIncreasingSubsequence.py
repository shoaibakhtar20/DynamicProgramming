def Lis(input_list):
    final_list = []
    ele= input_list[0]
    final_list.append(ele)

    for i in range(1, len(input_list)):
        if input_list[i] > ele:
            final_list.append(input_list[i])
            ele = input_list[i]

    print(final_list)
    return len(final_list)

print(Lis([10,22,9,33,21,50,41,60,80]))