import random
a = input("Кол-во записей:")
logs = open('log.txt', 'a', encoding='UTF8')
list2 = []
count = 0
count_lines = 0
while count < int(a):
    flag2 = 0
    correct = ''
    correct2 = ''
    with open('comands.txt', encoding='UTF8') as f:
        text = f.readlines()
        list = []
        ind = random.randint(0, 8)
        if ind == 0:
            f2 = open('books.txt', encoding='UTF8')
        if ind == 1:
            f2 = open('comp.txt', encoding='UTF8')
        if ind == 2:
            f2 = open('films.txt', encoding='UTF8')
        if ind == 3:
            f2 = open('song.txt', encoding='UTF8')
        if ind == 4:
            f2 = open('song2.txt', encoding='UTF8')
        if ind == 5:
            f2 = open('singers.txt', encoding='UTF8')
        if ind == 6:
            f2 = open('singers2.txt', encoding='UTF8')
        if ind == 7:
            f2 = open('singers3.txt', encoding='UTF8')
        if ind == 8:
            f2 = open('singers4.txt', encoding='UTF8')
        ind2 = random.randint(0, len(text) - 1)
        text2 = f2.readlines()
        ind3 = random.randint(0, len(text2) - 1)
        print(text2[ind3])
        if ind != 0:
            ind4 = random.randint(0, 5)
            if ind4 == 4:
                flag2 = 2
                f4 = open('comands_dob.txt', encoding='UTF8')
                if ind == 1 or ind == 2 or ind == 5 or ind == 6 or ind == 7 or ind == 8:
                    ind5 = random.randint(0, 1)
                    if ind5 == 0:
                        f3 = open('song.txt', encoding='UTF8')
                    if ind5 == 1:
                        f3 = open('song2.txt', encoding='UTF8')
                if ind == 3 or ind == 4:
                    ind5 = random.randint(0, 5)
                    if ind5 == 0:
                        f3 = open('comp.txt', encoding='UTF8')
                    if ind5 == 1:
                        f3 = open('films.txt', encoding='UTF8')
                    if ind5 == 2:
                        f3 = open('singers.txt', encoding='UTF8')
                    if ind5 == 3:
                        f3 = open('singers2.txt', encoding='UTF8')
                    if ind5 == 4:
                        f3 = open('singers3.txt', encoding='UTF8')
                    if ind5 == 5:
                        f3 = open('singers4.txt', encoding='UTF8')
        if text2[ind3].startswith('/'):
            count -= 1
        else:
            ind9 = random.randint(0, 10)
            string = text[ind2] + ' '
            if ind9 == 1:
                f6 = open('ne.txt', encoding='UTF8')
                text6 = f6.readlines()
                ind10 = random.randint(0, len(text6) - 1)
                string += text6[ind10]
                f6.close()
            else:
                if flag2 != 2:
                    ind7 = random.randint(0, 10)
                    if ind7 == 9:
                        f5 = open('dop_clova.txt', encoding='UTF8')
                        text5 = f5.readlines()
                        f5.close()
                        if ind == 0:
                            ind8 = random.randint(0, 2)
                            if ind8 == 0:
                                string += text5[2]
                                string += ' '
                            if ind8 == 1:
                                string += text5[6]
                                string += ' '
                            if ind8 == 2:
                                string += text5[7]
                                string += ' '
                        if ind == 1:
                            string += text5[4]
                            string += ' '
                        if ind == 2:
                            ind8 = random.randint(0, 1)
                            if ind8 == 0:
                                string += text5[8]
                                string += ' '
                            if ind8 == 1:
                                string += text5[9]
                                string += ' '
                        if ind == 3 or ind == 4:
                            ind8 = random.randint(0, 2)
                            if ind8 == 0:
                                string += text5[0]
                                string += ' '
                            if ind8 == 1:
                                string += text5[2]
                                string += ' '
                            if ind8 == 2:
                                string += text5[3]
                                string += ' '
                        if ind > 4:
                            ind8 = random.randint(0, 1)
                            if ind8 == 0:
                                string += text5[1]
                                string += ' '
                            if ind8 == 1:
                                string += text5[5]
                                string += ' '
                if flag2 == 2:
                    text4 = f3.readlines()
                    ind6 = random.randint(0, len(text4) - 1)
                    if text4[ind6].startswith('/'):
                        flag2 = 0
                    else:
                        text3 = f4.readlines()
                        for g, li in enumerate(text3):
                            if ind > 4 or ((ind == 3 or ind == 4) and ind5 >1):
                                if g == 0:
                                    stroka = li
                            if ind == 1 or ((ind == 3 or ind == 4) and ind5 == 0):
                                if g == 1:
                                    stroka = li
                            if ind == 2 or ((ind == 3 or ind == 4) and ind5 == 1):
                                if g == 2:
                                    stroka = li
                        lvsp = []
                        lvsp = stroka.split()
                        if ind == 3 or ind == 4:
                            string += lvsp[0]
                            string += ' '
                            stroka = lvsp[1]
                        else:
                            string += lvsp[1]
                            string += ' '
                            stroka = lvsp[0]
                text7 = text2[ind3]
                l = text2[ind3].split(':')
                text2[ind3] = l[0]
                if len(l) > 1:
                    correct = l[1]
                l = []
                if flag2 == 2:
                    m = text4[ind6].split(':')
                    text4[ind6] = m[0]
                    if len(m) > 1:
                        correct2 = m[1]
                    m = []
                    txt2 = text4[ind6]
                    flag3 =0
                    count_var_2 = 0
                    l_i = []
                    for p2, symbol2 in enumerate(text4[ind6]):
                        if symbol2 == '(':
                            flag3 += 1
                        if symbol2 == ')':
                            flag3 -= 1
                        if symbol2 == '|' and flag3 == 1:
                            count_var_2 += 1
                            l_i.append(p2)
                    if count_var_2 != 0:
                        chose_2 = random.randint(0, count_var_2)
                        if chose_2 == 0:
                            text4[ind6] = text4[ind6][:l_i[0]]
                        elif chose_2 == count_var_2:
                            text4[ind6] = text4[ind6][l_i[chose_2 - 1]:]
                        else:
                            text4[ind6] = text4[ind6][l_i[chose_2 - 1]:l_i[chose_2]]
                    for ko, sy2 in enumerate(text4[ind6]):
                        if sy2.isalpha():
                            clo = ko
                            break
                    text4[ind6] = text4[ind6][clo:]
                    cikl2 = 0
                    while '|' in text4[ind6]:
                        l_i = []
                        flag3 = 0
                        count_var_2 = 0
                        for n2, s3 in enumerate(text4[ind6]):
                            if s3 == '(':
                                flag3 += 1
                            if s3 == ')':
                                flag3 -= 1
                            if s3 == '|' and flag3 < 2:
                                count_var_2 += 1
                                l_i.append(n2)
                        if count_var_2 != 0:
                            chose_3 = random.randint(0, count_var_2)
                            if chose_3 == 0:
                                text4[ind6] = text4[ind6][:l_i[0]]
                                t2 = text4[ind6]
                            elif chose_3 == count_var_2:
                                text4[ind6] = text4[ind6][l_i[chose_3 - 1]:]
                                t2 = text4[ind6]
                            else:
                                text4[ind6] = text4[ind6][l_i[chose_3 - 1]:l_i[chose_3]]
                                t2 = text4[ind6]
                        for k4, s6 in enumerate(text4[ind6]):
                            if s6.isalpha():
                                cl5 = k4
                                break
                        text4[ind6] = text4[ind6][cl5:]
                    print(text4[ind6])
                txt = text2[ind3]
                flag = 0
                count_var = 0
                list_index = []
                for i, symbol in enumerate(text2[ind3]):
                    if symbol == '(':
                        flag += 1
                    if symbol == ')':
                        flag -= 1
                    if symbol == '|' and flag == 1:
                        count_var += 1
                        list_index.append(i)
                if count_var != 0:
                    chose = random.randint(0, count_var)
                    if chose == 0:
                        text2[ind3] = text2[ind3][:list_index[0]]
                    elif chose == count_var:
                        text2[ind3] = text2[ind3][list_index[chose - 1]:]
                    else:
                        text2[ind3] = text2[ind3][list_index[chose-1]:list_index[chose]]
                for k, s in enumerate(text2[ind3]):
                    if s.isalpha():
                        cl = k
                        break
                text2[ind3] = text2[ind3][k:]
                print(text2[ind3])
                cikl = 0
                while '|' in text2[ind3]:
                    list_index = []
                    flag = 0
                    count_var = 0
                    for n, s2 in enumerate(text2[ind3]):
                        if s2 == '(':
                            flag += 1
                        if s2 == ')':
                            flag -= 1
                        if s2 == '|' and flag < 2:
                            count_var += 1
                            list_index.append(n)
                    if count_var != 0:
                        chose = random.randint(0, count_var)
                        if chose == 0:
                            text2[ind3] = text2[ind3][:list_index[0]]
                            t = text2[ind3]
                        elif chose == count_var:
                            text2[ind3] = text2[ind3][list_index[chose - 1]:]
                            t = text2[ind3]
                        else:
                            text2[ind3] = text2[ind3][list_index[chose - 1]:list_index[chose]]
                            t = text2[ind3]
                    for k, s in enumerate(text2[ind3]):
                        if s.isalpha():
                            cl = k
                            break
                    text2[ind3] = text2[ind3][k:]
                string += text2[ind3]
                if flag2 == 2:
                    flag2 = 0
                    string += ' '
                    string += stroka
                    string += ' '
                    string += text4[ind6]
                    string += ' '
                    string += ':'
                    string += correct
                    string += ' '
                    string += ';'
                    string += ' '
                    string += correct2
                    f3.close()
                    f4.close()
                else:
                    string += ' '
                    string += ':'
                    string += correct
            newstring = ''
            for s3 in string:
                if s3.isalpha() or s3 == ":" or s3 == ",":
                    newstring += s3
                else:
                    newstring += ' '
            f2.close()
            f.close()
            ns = ' '.join(newstring.split())
            logs.write(ns + '\n')
            print(ns)
        count += 1
logs.close()