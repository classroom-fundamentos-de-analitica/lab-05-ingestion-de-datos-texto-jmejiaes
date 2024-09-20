import os
import pandas as pd
import numpy as np

# obtain a list of every file in data/test/neutral


# define an empty dataframe with two cols, phrase and target
df = pd.DataFrame(columns=['phrase', 'target'])


# for status in ['neutral', 'positive', 'negative']:

#     list = os.listdir(f'data/test/{status}')
#     text = []


#     for i in range(len(list)):

all_status = ['neutral', 'positive', 'negative']
all_directories = ['test', 'train']

for directory in all_directories:

    external_df = pd.DataFrame(columns=['phrase', 'sentiment'])

    for status in all_status:

        text = []
        list_of_files = os.listdir(f'data/{directory}/{status}')

        for i in range(len(list_of_files)):

            with open(f'data/{directory}/{status}/' + list_of_files[i], 'r', encoding="utf-8") as file:


                if list_of_files[i] == '.DS_Store':
                    continue

                
                # print( list[i])
                text.append(file.read())

        # crear dataframe
        internal_df = pd.DataFrame({'phrase': text, 'sentiment': status})

        ## TODO verificar el index ignoring
        external_df = pd.concat([external_df, internal_df], ignore_index=True)

    external_df.to_csv(f'{directory}_dataset.csv', index=False)
    

print('done')