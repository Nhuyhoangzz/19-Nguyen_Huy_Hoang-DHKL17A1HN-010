import json

py_obj = {
    "name": "huyhoang",
    "age": 19,
    "city": "HaNoi",
    "skills": ["Python", "Machine Learning", "Data Analysis"]
}
# Chuyển đổi đối tượng Python sang chuỗi JSON
json_data = json.dumps(py_obj)

# In chuỗi JSON
print("Chuỗi JSON:")
print(json_data)

# Truy cập và in từng giá trị từ đối tượng Python
print("Các giá trị từ đối tượng Python:")
for key, value in py_obj.items():
    print(key,value)
