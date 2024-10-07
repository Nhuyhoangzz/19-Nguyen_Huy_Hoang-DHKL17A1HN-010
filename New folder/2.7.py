import json
json_data = '''
{
    "name": "huyhoang",
    "age": 19,
    "city": "HaNoi",
    "skills": ["Python", "Data Analysis"]
}
'''
# Chuyển đổi từ chuỗi JSON thành đối tượng Python
py_obj = json.loads(json_data)
# In đối tượng Python
print(py_obj )
#kq
print("tên:",py_obj ['name'])
print("Tuổi:",py_obj ['age'])
print("Kỹ năng:",py_obj ['skills'])
