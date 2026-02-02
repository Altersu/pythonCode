import my_utils.str_utils
from my_utils  import file_utils

print(my_utils.str_utils.str_reverse("yousejinshu"))
print(my_utils.str_utils.substr("yousejinshu",1,3))

# print(file_utils.print_file_info("C:/Users/sumen/Desktop/test.txt"))
print(file_utils.append_file("C:/Users/sumen/Desktop/test.txt","别再跌了"))
print(file_utils.print_file_info("C:/Users/sumen/Desktop/test.txt"))