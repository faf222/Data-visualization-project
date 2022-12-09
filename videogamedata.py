import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

file_name = 'Video_Games_Sales_as_at_22_dec_2016.csv'
console_file = 'console.csv'

def main():
   
    #yearly_game_sales(dict_to_data(shrink_dict_sum(to_horizontal_dict("Year_of_Release","Global_Sales",load_csv(file_name))),'Years','Sold'))
    #Average_Sales_PerGame(load_csv(file_name))
    #genre_sales(dict_to_data(shrink_dict_sum(to_horizontal_dict('Genre','Global_Sales',load_csv(file_name))),'Genre','Sales'))
    #games_made_year(dict_to_data(shrink_dict_num(to_horizontal_dict('Year_of_Release','Name',load_csv(file_name))),'Years','Number of Games'))
    #onsole_release(dict_to_data(shrink_dict_num(to_horizontal_dict('Release_Year','Console_Name',load_csv(console_file))),'Years','Console'))
    sales_to_rating(dict_to_data(shrink_dict_sum(to_horizontal_dict('Critic_Score','Global_Sales',load_csv(file_name))),'Score','Sales'))
    plt.show()

def load_csv(file):
    return pd.read_csv(file)

def shrink_dict_num(dict):
    temp = {}
    for i in dict.keys():
        temp[i] = len(dict[i])
    return temp

def to_horizontal_dict(key_column, value_column, data):
    storage_dict = {}
    temp = data[[key_column,value_column]]
    temp = temp.dropna()
    keys = temp[[key_column]].to_numpy()
    values = temp[[value_column]].to_numpy()
    for index , key in enumerate(keys):
#        try:
#            if math.isnan(key[0]) == False:
                if key[0] not in storage_dict.keys():
                    storage_dict[key[0]] = [values[index][0]]
                else:
                    storage_dict[key[0]].append(values[index][0])
#        except:
#            if key[0] not in storage_dict.keys():
#                storage_dict[key[0]] = [values[index][0]]
#            else:
#                storage_dict[key[0]].append(values[index][0])
    return storage_dict


def shrink_dict_sum(dict):
    temp = {}
    for i in dict.keys():
        temp[i] = int(sum(dict[i]))
    return temp

def dict_to_data(dict,key_column,value_column):
    df = pd.DataFrame.from_dict({key_column:dict.keys(),value_column:dict.values()})
    return df

def console_release(df):
    sns.scatterplot(x='Years',y='Console', data=df)

def games_made_year(df):
    sns.scatterplot(x = 'Years',y='Number of Games',data=df)
        
def yearly_game_sales(df):
    sns.lineplot(x='Years', y='Sold',data=df)

def genre_sales(df):
    sns.barplot(x = 'Genre',y = 'Sales', data = df)

def Average_Sales_PerGame(data):
    sns.lineplot(x='Year_of_Release', y='Global_Sales',data=data)#average number of sales per video game

def sales_to_rating(df):
    sns.barplot(x = 'Score',y = 'Sales', data = df)

if __name__ == "__main__":
    main()