
# coding: utf-8

import pandas as pd

def create_averages_dataframe(df, target):
    
    '''
    This function takes in the 2012 PISA data as a pandas
    dataframe ad computes the average score of the target
    variable for each country based on whether or not the
    student had their own room, had a computer, or had
    access to the internet
    
    Input variables:
    df: pandas dataframe object of 2012 PISA data
    target: numerical variable to extract averages of such as
            'PV1MATH' or 'PV5SCIE'
    
    Output:
    averages: pandas dataframe object where each row contains
              country name and average target score for each
              of 4 scenarios: (no room and no computer and no internet),
                               has own room, has computer, has internet
    '''
    
    #create dataframes for 4 scenarios
    no_tools = pisa[(pisa.ST26Q02 == 'No') & (pisa.ST26Q04 == 'No') & (pisa.ST26Q06 == 'No')]
    room = pisa[(pisa.ST26Q02 == 'Yes')]
    computer = pisa[(pisa.ST26Q04 == 'Yes')]
    both = pisa[(pisa.ST26Q02 == 'Yes') & (pisa.ST26Q04 == 'Yes')]
    
    #convert dataframes to averages using df.groupby()
    no_tools = no_tools.groupby('CNT', as_index = False).mean()
    room = room.groupby('CNT', as_index = False).mean()
    computer = computer.groupby('CNT', as_index = False).mean()
    both = both.groupby('CNT', as_index = False).mean()
    
    #also create dataframe of averages per country (for dimple.js sorting)
    average_all = pisa.groupby('CNT', as_index = False).mean()
    
    #initialize output dataframe
    averages = pd.DataFrame()
    averages['country'] = no_tools['CNT']
    averages['no_tools'] = no_tools[target]
    averages['room'] = room[target]
    averages['computer'] = computer[target]
    averages['both'] = both[target]
    averages['average_all'] = average_all[target]
    
    #sort averages by internet column and add sequential numbers for dimple.js sorting

    averages = averages.sort_values('average_all', ascending=False).reset_index()
    averages['sort'] = pd.Series(range(1,len(averages)+1))
    
    return averages



pisa = pd.read_csv('truncatedPisa.csv')

math_averages = create_averages_dataframe(pisa, 'PV1MATH')

math_averages = pd.melt(math_averages,id_vars=["country", "sort"],
                value_vars=["no_tools", "room", "computer", "both", "average_all"],
                var_name = "tools", value_name = "math_average")

math_averages.to_csv("math_averages.csv")
