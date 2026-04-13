import qlib
from qlib.config import REG_CN
from qlib.contrib.data.handler import Alpha158

def main():
    provider_uri = "D:/finance/qlib_data/cn_data"
    qlib.init(provider_uri=provider_uri, region=REG_CN)
    
    # ✅ 必须先实例化（不传时间/股票池，避免加载数据）
    handler = Alpha158(
        instruments='csi300',
        start_time='2022-01-01',
        end_time='2022-01-31',      # ✅ 只用一个月，内存安全
        infer_processors=[],         # ✅ 关闭处理器，进一步减少内存
        learn_processors=[],
    )
    
    # ✅ 用实例调用
    fields, names = handler.get_feature_config()
    
    print(f"特征总数: {len(names)}")
    print("\n前20个特征：")
    for f, n in zip(fields, names):
        print(f"  {n:30s}  {f}")

if __name__ == '__main__':
    main()