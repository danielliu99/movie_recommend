import pandas as pd 

class movie_index(): 
    def __init__(self, data_path) -> None:
        self.dataframe = pd.read_csv(data_path)
        self.index_to_item = self.dataframe[['id', 'original_title']].to_dict('index')
        self.id_to_index = {v['id']:k for k, v in self.index_to_item.items()}

    def getItem(self, index): 
        return self.index_to_item[index]

    def getId(self, index): 
        return self.index_to_item[index]['id']
    
    def getTitle(self, index): 
        return self.index_to_item[index]['original_title']
    
    def getIndex(self, id): 
        return self.id_to_index[id]