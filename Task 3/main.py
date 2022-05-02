file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'

def write_func():
    with open(file_name_1, encoding = 'utf8') as f_1:
        text_1 = f_1.read().split('\n')
        text_1.insert(0, str(len(text_1)))
        text_1.insert(0, file_name_1)



    with open(file_name_2, encoding = 'utf8') as f_2:
        text_2 = f_2.read().split('\n')
        text_2.insert(0, str(len(text_2)))
        text_2.insert(0, file_name_2)


    with open(file_name_3, encoding = 'utf8') as f_3:
        text_3 = f_3.read().split('\n')
        text_3.insert(0, str(len(text_3)))
        text_3.insert(0, file_name_3)



    list_1 = [text_1,text_2,text_3]

    list_1.sort(key=len)


    with open('4.txt','a', encoding = 'utf8') as f_4:
        for i in list_1:
            for k in i:
                f_4.write(f'{k}\n')
write_func()




