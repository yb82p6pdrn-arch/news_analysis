import sys
print("当前解释器路径：", sys.executable)

try:
    from rdkit import Chem
    print("rdkit 导入成功！")
except ImportError:
    print("rdkit 导入失败，环境没选对！")