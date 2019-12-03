import json
import os

def GlobalRead():
    data_file = os.path.abspath('..')  # 项目路径
    file = os.path.join(data_file, 'conf', 'global_nam')  # faces路径，face要放在项目的同一级
    with open(file, 'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict