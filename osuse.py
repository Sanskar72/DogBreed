import os
import pandas as pd
import numpy as np
import shutil

ll = ['beagle', 'chihuahua', 'doberman', 'french_bulldog', 'golden_retriever', 'malamute', 'pug', 'saint_bernard', 'scottish_deerhound', 'tibetan_mastiff']

df = pd.read_csv('labels.csv')
print(df.shape)
df = df[(df['breed'].isin(ll))]

#df.to_csv (r'C:\Users\sanzk\OneDrive\Desktop\PythonFiles\labels1.csv', index = False, header=True)

print(df.shape)

df['id'] = df['id'] + ".jpg"
#print(df)

os.chdir(r'C:\Users\sanzk\OneDrive\Desktop\PythonFiles\DogBreed')
dst_dir = r"C:\Users\sanzk\OneDrive\Desktop\PythonFiles\NewDogBreed"
'''
for f in df['id']:
    shutil.copy(f, dst_dir)

'''