# my_dict1={"alter":100,"youse":8,"zijin":40}
# my_dict2={}
# my_dict3=dict()
# print(my_dict1)
# print(my_dict2)
# print(my_dict3)
# score = my_dict1["alter"]
# print( score)

# stu_score_dict ={
#     "wanglihong":{
#         "chinese":100,
#         "english":90,
#         "math":80
#     },"linjunjie":{
#         "chinese":100,
#         "english":90,
#         "math":80
#     },"taozhe":{
#         "chinese":100,
#         "english":90,
#         "math":80
#     }
# }
# print(stu_score_dict)
# score = stu_score_dict["wanglihong"]["chinese"]
# print(score)

# my_dict ={"zhoujielun":99,"linjunjie":88,"taohe":100}
# my_dict["wanglijong"]=99
# print(my_dict)
# my_dict["linjunjie"]=77
# print(my_dict)
# score = my_dict.pop("zhoujielun")
# print(my_dict,score)
# my_dict.clear()
# print(my_dict)

# my_dict ={"zhoujielun":99,"linjunjie":88,"taoze":100}
# keys = my_dict.keys()
# print(keys)
#
# for key in keys:
#     print(key,my_dict[key])
#
# for key in my_dict:
#     print(key,my_dict[key])
#
# num = len(my_dict)
# print(num)

dept_dict ={
    "wanglijong":{
        "bumen":"kejibu",
        "gongzi":3000,
        "jibie":1
    },"linjunjie":{
        "bumen":"shichangbu",
        "gongzi":5000,
        "jibie":2
    },"taozhe":{
        "bumen":"shichangbu",
        "gongzi":7000,
        "jibie":3
    },"zhoujielun":{
        "bumen":"kejibu",
        "gongzi":4000,
        "jibie":1
    },"zhangxueyou":{
        "bumen":"shichangbu",
        "gongzi":6000,
        "jibie":2
    }
}
print(dept_dict)
for key in dept_dict:
    if dept_dict[key]["jibie"] == 1:
         em_dept_dict = dept_dict[key]
         em_dept_dict["jibie"] =2
         em_dept_dict["gongzi"]+=1000
         dept_dict[key] = em_dept_dict
    #     dept_dict[key]["jibie"] = 2
    #     dept_dict[key]["gongzi"]=dept_dict[key]["gongzi"]+1000
    #
    # print(key,dept_dict[key])
print(dept_dict)