#Bài 01
# Viết hàm day_diff() nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code. 
# Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). 
# Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05

# from datetime import date
# from datetime import time
# from datetime import datetime

# release_date = "23/08/2021"
# code_complete_day = "2021-15-09"
# def day_diff(release_date, code_complete_day):
#      convert_release_time = datetime.strptime(release_date, "%d/%m/%Y")
#      print("Ngày release:",convert_release_time)
#      convert_code_complete_day = datetime.strptime(code_complete_day, "%Y-%d-%m")
#      print ("Ngày complete:",convert_code_complete_day)
#      number_time = convert_code_complete_day - convert_release_time
#      print ("Số ngày có thể test được sản phẩm là:",number_time)
#      return number_time.days
# day_diff(release_date, code_complete_day)



# def day_diff(date_release, date_complete):
#     d1=datetime.datetime.strptime(date_release,"%d/%m/%Y")
#     print("Ngày release:",d1)
#     d2 = datetime.datetime.strptime(date_complete,"%Y-%d-%m")
#     print ("Ngày complete:",d2)
#     print ("Số ngày có thể test được sản phẩm là:",d1-d2)

# day_diff(date_release, date_complete)



# Bài 2:
# Viết hàm alpha_num() tìm tất cả những từ trong một câu 
# có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
# Vd:
# str1 = "Emma25 is Data scientist50 and AI Expert"
# alpha_num(str1) == ["Emma25", "scientist50"]


str= "Emma25 is Data scientist50 and AI Expert"
print("chuỗi là: ",str)
def alpha_num(sentence):
    list_words = []
    words = sentence.strip().split()
    for i in words:
        is_text = False
        is_number = False
        for j in i:
            if j.isalpha():
                is_text = True
            elif j.isnumeric():
                is_number= True
            if is_text and is_number:
                list_words.append(i)
                break
    return list_words
alpha_num(str)  