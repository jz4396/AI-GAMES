# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('training_data.npy')

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

Jumps = []
notJumps = []


shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0]:
        Jumps.append([img,choice])
    elif choice == [0,1]:
        notJumps.append([img,choice])
    else:
        print('no matches')


Jumps = Jumps[:len(notJumps)]
notJumps = notJumps[:len(Jumps)]

final_data = Jumps + notJumps
shuffle(final_data)

np.save('training_data_balanced.npy', final_data)




