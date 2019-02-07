# Recommender Class

import pandas as pd

class beers():
    ''' "DW_SVD" : Descriptive words with Single Value Decomposition
    "DW" : Descriptive words with Count Vectorization
    "AW_SVD" : All words with Single Value Decomposition
    "AW" : All words withCount Vectorization'''
    def __init__(self, cosign_matrix = 'DW_SVD'):
        self.cms = pd.read_pickle(f"./Data/modeldata/dataframe_{cosign_matrix}")
        self.beer_info = pd.read_pickle('Data/modeldata/beer_info')

    def search(self, beer_name,):
        '''Search a beers name, its not that complicated... '''
        return self.beer_info[self.beer_info.index.str.contains(beer_name,case = False, regex = True)]

    def recommend(self, beer_name, n_recommendations = 5):
        '''Use beer name from the results of searching'''
        top = self.cms.loc[beer_name].sort_values(ascending = False)[1:n_recommendations+1].index
        return self.beer_info.loc[top].set_index('Beer_Name')
