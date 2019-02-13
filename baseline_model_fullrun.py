import pandas as pd
import numpy as np
import random
from sklearn.metrics import f1_score
import seaborn as sns

################################################################################
#####                         IMPORT DATA FILES                            #####
################################################################################

ette_cont = pd.read_csv("bachelorette-contestants.csv")
elim_data = pd.read_csv('bachelorette_538.csv')

################################################################################
#####                       FORMAT DATA AS NEEDED                          #####
################################################################################

# remove first line, which is just the header info repeated
elim_data = elim_data.drop([0])

# need to change from wide form data to long form data
# want it to be:
# SHOW, SEASON, CONTESTANT, 'TYPE', 'VALUE'
# with 'TYPE' as the current column names
elim1 = pd.melt(elim_data, id_vars=['SHOW', 'SEASON', 'CONTESTANT'])

# rename variable and value
elim1.columns = ['SHOW', 'SEASON', 'CONTESTANT', 'TYPE', 'VALUE']

# split TYPE variable
elim1[['ELIM_DATE', 'NUMBER']] = elim1['TYPE'].str.split('-',expand=True)

#convert NUMBER to numeric
pd.to_numeric(elim1['NUMBER'])

################################################################################
#####                       CHOOSE SEASON AND SHOW                         #####
################################################################################

ette13 = elim1[(elim1.SEASON == '13') & (elim1.SHOW == 'Bachelorette')]

################################################################################
#####                           DEFINE FUNCTIONS                           #####
################################################################################

#function returns name of random person from input contestant list
def randbaseline(cont_list):
    num_cont = len(cont_list) # set length of list
    ran_cont_list = random.sample(cont_list, len(cont_list)) #shuffles input list
    win_num = random.randint(0,num_cont-1) # chooses a random number
    return ran_cont_list[win_num] # returns the name associated with the random number chosen

#function returns the updated contestant list after elimination occurs
def getcont(week,cont_list,data):
    numelim = 'ELIMINATION-' + week #sets the week we're looking at
    # selects the data set that corresponds with the week and elimination data
    elim = data[(data.TYPE == numelim) & ((data.VALUE == 'E')|(data.VALUE == 'EU')|(data.VALUE == 'ED')|(data.VALUE == 'EF'))].CONTESTANT.values
    new_cont_list = cont_list.copy() # creates copy of contestant list
    new_cont_list = [elem for elem in new_cont_list if elem not in elim ] # creates new contestant list based on those contestants available
    return new_cont_list

#*****add in option bach/ette option
#input season, data
def baselinemodel(season_num, show, data): #data == elim1
    if show == "Bachelor":
        subset = data[(data.SEASON == str(season_num)) & (data.SHOW == 'Bachelor')]
        if season_num == '11':
            return (0,0,0)
    elif show == "Bachelorette":
        subset = data[(data.SEASON == str(season_num)) & (data.SHOW == 'Bachelorette')]
    else:
        return ("Not a Show Option")
    elimrounds = subset.NUMBER.max()

    w1_cont = pd.unique(subset.CONTESTANT) #select list of starting contestants
    w1_cont = [name for name in w1_cont if str(name) != 'nan'] #remove nan
    w1_cont_ID = {} #dictionary that contains numerical ID for contestants
    ID = 0
    for name in w1_cont:
        w1_cont_ID[name] = ID
        ID += 1

    winner = subset[subset.VALUE == 'W'].CONTESTANT.values
    winner_lst =[]
    for win in winner:
        break
    winner_lst = [w1_cont_ID[win]] * (int(elimrounds)+1)

    elimdict = {}
    contlist = w1_cont
    elimdict[1] = contlist
    #loops through each elimination week and creates a dict of the updated contestant lists
    for week in range(1,int(elimrounds)+1):
        elimdict[week+1] = getcont(str(week),contlist,subset)
        contlist = elimdict[week+1]

    pred_winner_dict = {}
    for key in elimdict.keys():
        pred_winner_dict[key] = randbaseline(elimdict[key])

    pred_winner = []
    for key in pred_winner_dict.keys():
        pred_winner.append(w1_cont_ID[pred_winner_dict[key]])

    F1score = f1_score(winner_lst, pred_winner, average='micro')

    return (pred_winner_dict, winner, F1score) #return predicted winner for each week, winner, f1score

################################################################################
#####                      BACHELORETTE RUN CODE                           #####
################################################################################

scoredict_ette = {}
seasonlist_ette = ['01', '02','03','04','05','06','07','08','09','10','11','12','13']
i=1
for season in seasonlist_ette:
    scoredict_ette[i] = baselinemodel(season,'Bachelorette',elim1)
    i+=1
#len(scoredict_ette)

# for key in scoredict_ette.keys():
#     print(key,scoredict_ette[key][2])
ettescore = pd.DataFrame.from_dict(scoredict_ette, orient = "index")
ettescore.columns = ['predictions','seasonwinner','F1Score']
#ettescore.head()

sns.barplot(x=ettescore.index, y=ettescore.F1Score)

################################################################################
#####                         BACHELOR RUN CODE                            #####
################################################################################

scoredict_bach = {}
seasonlist_bach = ['01', '02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21']
i=1
for season in seasonlist_bach:
    scoredict_bach[i] = baselinemodel(season,'Bachelor',elim1)
    i+=1
len(scoredict_bach)

# for key in scoredict_bach.keys():
#     print(key,scoredict_bach[key][2])
bachscore = pd.DataFrame.from_dict(scoredict_bach, orient = "index")
bachscore.columns = ['predictions','seasonwinner','F1Score']
#bachscore.head()

sns.barplot(x=bachscore.index, y=bachscore.F1Score)
