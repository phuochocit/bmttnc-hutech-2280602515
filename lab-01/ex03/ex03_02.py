def dao_nguoc_list (lst):
    return lst[::-1]
input_list = input("Nhap danh sach cac so,cach nhau dau phay: ")
number_list = list(map(int, input_list.split(",")))
list_dao_nguoc = dao_nguoc_list(number_list)
print ("List sau khi dao nguoc la:", list_dao_nguoc)