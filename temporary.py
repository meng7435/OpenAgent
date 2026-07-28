import os
# 配置镜像加速
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
from modelscope import snapshot_download

# 下载模型，保存到本地目录
model_dir = snapshot_download("BAAI/bge-small-zh-v1.5")
print("模型下载路径：", model_dir)