import json


def json_write(req_dict, name, facetokens):
    for i in req_dict:#在json中遍历查找token
        if i == "faceset_token":
            with open("D:/face/conf/fac_con", 'r') as load_f:
                load_dict = json.load(load_f)
                print(load_dict)
            with open("D:/face/conf/fac_con", "w") as f:
                real_dict = load_dict[name]
                real_dict.append(facetokens)
                load_dict[name] = real_dict
                json.dump(load_dict, f)