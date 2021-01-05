dict_1 = {'id': 1, 'name':'hong', 'email':'hong@mail.com', 'hp_num':'010-2343-9879'}
dict_2 = {'id': 2, 'name':'lee', 'email':'lee@mail.com', 'hp_num':'010-3333-9879'}
dict_3 = {'id': 3, 'name':'jang', 'email':'jang@mail.com', 'hp_num':'010-7777-9879'}
dict_4 = {'id': 4, 'name':'king', 'email':'king@mail.com', 'hp_num':'010-9999-9879'}


list_dict = [dict_1, dict_2, dict_3, dict_4]

for i in list_dict:
    for j in i:
        print(j, i[j])