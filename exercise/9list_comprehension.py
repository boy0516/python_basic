books = list()
print(type(books))

books.append({'제목':'개발자의 코드', '출판연도':'2013.02.28', '출판사':'A출판', '쪽수':200, '추천유무': False})
books.append({'제목':'클린 코드', '출판연도':'2013.03.04', '출판사':'B출판', '쪽수':584, '추천유무': True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014.07.02', '출판사':'A출판 ', '쪽수':296, '추천유무': True})
books.append({'제목':'구글드', '출판연도':'2010.02.10', '출판사':'B출판 ', '쪽수':526, '추천유무': False})
books.append({'제목':'강의력', '출판연도':'2013.12.12', '출판사':'C출판 ', '쪽수':248, '추천유무': True})


list_1 = [book for book in books if book['쪽수'] > 250]
list_2 = [book for book in books if book['추천유무'] == True]
all_book_page = sum(book['쪽수'] for book in books)
set_3 = set([book['출판사'].strip() for book in books])



print(list_1)
print(list_2)
print(set_3)