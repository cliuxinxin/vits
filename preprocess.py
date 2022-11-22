import text
import pandas as pd

out_extension = "cleaned"
file = 'DUMMY3/metadata.csv'
text_cleaners = "basic_cleaners"

df = pd.read_csv(file, sep='|', header=None, names=['path', 'text'])
df['text'] = df['text'].apply(lambda x: text._clean_text(x, [text_cleaners]))

lenth = len(df)

train_len = 100

# 随机打乱数据
df = df.sample(frac=1).reset_index(drop=True)

train_df = df[:train_len]
val_df = df[train_len:]

train_df.to_csv('filelists/train.cleaned', sep='|', index=False, header=False)
val_df.to_csv('filelists/val.cleaned', sep='|', index=False, header=False)



