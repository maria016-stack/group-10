lst=[345,564,100,5673]
print(lst[0])#before call it gave the first number of original list
def change_list (lst):
    lst[0]=999
    print(lst[0])
change_list(lst)#after the call it gave the first number in the list as 999
