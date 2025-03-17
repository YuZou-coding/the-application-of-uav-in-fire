import pandas as pd

def filter_hk_collisions(csv_path):
    # 读取 CSV 文件，设置 low_memory=False 以避免 DtypeWarning
    df = pd.read_csv(csv_path, low_memory=False)
    
    # 筛选符合条件的行
    filtered_df = df[
        (df['longitude'] >= 114.130) & 
        (df['longitude'] <= 114.230) & 
        (df['latitude'] >= 22.295) & 
        (df['latitude'] <= 22.345)
    ]
    
    # 只保留前十条记录
    filtered_df = filtered_df.head(10)
    
    # 输出保留的数据行数
    print(f"Number of rows after filtering: {len(filtered_df)}")
    
    # 保存筛选后的数据到 CSV 文件
    filtered_df.to_csv(csv_path, index=False)
    print(f"Filtered data saved to {csv_path}")

# 使用函数筛选数据
csv_path = 'hk_collisions.csv'
filter_hk_collisions(csv_path)



