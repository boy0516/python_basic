'''
스택과 큐를 리스트로 작성한다
'''


stack_list = [1,2,3]
stack_list.append(5)
stack_list.extend([10,20])
print(stack_list)
#LIFO
stack_list.pop()
print(stack_list)
stack_list.pop()
print(stack_list)
#FIFO
queue_list =[10, 20, 30]
queue_list.pop(0)
print(queue_list)

#tuple
my_tuple = tuple([10, 20, 30])
my_tuple2 = (20, 30, 40)
print(type(my_tuple), type(my_tuple2))
print(my_tuple[2],my_tuple[0:2],my_tuple*2)
#하지만 값 변경은 할 수 없다

my_set = set([1,2,3,1,2,3])
print(type(my_set),my_set)
my_set.add(1)
print(my_set)
my_set.remove(1)
print(my_set)
my_set.update([1,4,5,6,7])
print(my_set)
my_set.discard(3)
print(my_set)
my_set.clear()
print(my_set)

s1=set([1,2,3,4,5])
s2 =set([3,4,5,6,7])

print('합집합', s1.union(s2), s1|s2)
print('교집합', s1,intersection(s2))