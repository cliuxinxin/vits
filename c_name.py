import re
import pandas as pd

df = pd.read_csv('DUMMY3/metadata2.csv', sep='|', header=None, names=['path', 'text'])
# 只保留数字和字母
df['new_path'] = df['path'].apply(lambda x: re.sub(r'[^a-zA-Z0-9//.-]', '', x))

# 修改文件名
for i in range(len(df)):
    old_name = df['path'][i]
    new_name = df['new_path'][i]
    os.rename(old_name, new_name)