import text
import pandas as pd

out_extension = "cleaned"
text_cleaners = "basic_cleaners"

def read_metadata(file,is_cleaned=False,id=0):
    df = pd.read_csv(file, sep='|', header=None, names=['path', 'text'])
    df['id'] = id
    if is_cleaned:
        return df
    df['text'] = df['text'].apply(lambda x: text._clean_text(x, [text_cleaners]))
    return df

df_1 = read_metadata('DUMMY3/metadata.csv',is_cleaned=False,id=1)
df_2 = read_metadata('DUMMY3/metadata2.csv',is_cleaned=False,id=2)
df_3 = read_metadata('DUMMY3/metadata3_clean.csv',is_cleaned=True,id=3)

df_train = []
df_dev = []
pati = 0.1

for df in [df_1,df_2,df_3]:
    df = df.sample(frac=1)
    df_train.append(df[:int(len(df)*(1-pati))])
    df_dev.append(df[int(len(df)*(1-pati)):])

df_train = pd.concat(df_train)
df_dev = pd.concat(df_dev)

df_train[['path','id','text']].to_csv('filelists/train.cleaned', index=False, sep='|', header=False)
df_dev[['path','id','text']].to_csv('filelists/val.cleaned', index=False, sep='|', header=False)

df_train[['path','text']].to_csv('filelists/train.cleaned', index=False, sep='|', header=False)
df_dev[['path','text']].to_csv('filelists/val.cleaned', index=False, sep='|', header=False)

