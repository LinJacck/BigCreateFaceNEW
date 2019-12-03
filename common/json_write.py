import json
import os


def json_write(req_dict, name, facetokens):
    data_file = os.path.abspath('..')  # 项目路径
    file = os.path.join(data_file, 'conf', 'fac_con')  # faces路径，face要放在项目的同一级
    for i in req_dict:#在json中遍历查找token
        if i == "faceset_token":
            with open(file, 'r') as load_f:
                load_dict = json.load(load_f)
                print(load_dict)
            with open(file, "w") as f:
                real_dict = load_dict[name]
                real_dict.append(facetokens)
                load_dict[name] = real_dict
                json.dump(load_dict, f)