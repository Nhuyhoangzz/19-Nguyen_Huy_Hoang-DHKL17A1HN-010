import json

py_obj = {
    "name": "huyhoang",
    "age": 19,
    "city": "HaNoi",
    "skills": ["Python", "Machine Learning", "Data Analysis"]
}
# Chuyển đổi đối tượng từ điển Python sang chuỗi JSON và sắp xếp
json_data = json.dumps(py_obj, indent=4)
print("Chuỗi JSON sau khi sắp xếp theo khóa:")
print(json_data)
# kết quả
print("Các thành viên của đối tượng Python:")
for key, value in py_obj.items():
    print(key,value)
