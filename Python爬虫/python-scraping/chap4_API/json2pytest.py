import json

jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],' \
             '"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'

jsObj = json.loads(jsonString)   #转化成了 python 字典形式
# 与 jsObj = eval(jsonString)  效果相同

print(type(jsObj))
print(jsonString)
print(jsObj.get("arrayOfNums"))
print(jsObj["arrayOfNums"])