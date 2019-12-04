import json
import os
def GlobalWrite(key,information):
    data_file = os.path.abspath('..')  # 项目路径
    file = os.path.join(data_file, 'conf', 'global_nam')  # faces路径，face要放在项目的同一级
    with open(file, 'r') as load_f:
        load_dict = json.load(load_f)
    with open(file, "w") as f:
        load_dict[key] = information
        json.dump(load_dict, f)