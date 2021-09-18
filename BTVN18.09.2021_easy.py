#Bài 01
# Viết hàm day_diff() nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code. 
# Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). 
# Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05

from datetime import date
from datetime import time
from datetime import datetime
import datetime
date_release = "23/08/2021"
date_complete = "2021/15/09"
def day_diff(date_release, date_complete):
    d1=datetime.datetime.strptime(date_release,"%d/%m/%Y")
    print("Ngay release:",d1)
    d2 = datetime.datetime.strptime(date_complete,"%Y-%d-%m")
    print ("Ngày complete:",d2)
    print ("So ngay co the test duoc sp la:",d1-d2)

day_diff(date_release, date_complete)

# Bài 2:
# Viết hàm alpha_num() tìm tất cả những từ trong một câu 
# có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
# Vd:
# str1 = "Emma25 is Data scientist50 and AI Expert"
# alpha_num(str1) == ["Emma25", "scientist50"]


str= "Emma25 is Data scientist50 and AI Expert"
print("chuoi la: ",str)
def chu_so(s):
    s_list_chu_so = []
    s_list = str.split()
    print(s_list)
    for tu in s_list:
        if tu.isalpha()!=True and tu.isdecimal()!=True:
            s_list_chu_so.append(tu)
        else:
            continue  
    print("tu can tim trong chuoi tren la:",s_list_chu_so)
chu_so(str)