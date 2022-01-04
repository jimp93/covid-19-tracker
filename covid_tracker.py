import pandas as pd
import numpy as np
import pandas as pd
import numpy as np

countries = ['australia', 'canada', 'denmark', 'france', 'germany', 'italy', 'norway', 'spain', 'united-kingdom']

df_q = pd.read_excel('codebook.xlsx')
df_q.head(70)

df_q.drop(df_q.index[:67], inplace=True)

df_q

df_q.dropna(axis=0, subset=['RecordNo'], inplace=True) 

df_q.head(50)

df_q.reset_index(drop=True, inplace=True)

for index, row in df_q.iterrows():
    if pd.isna(row['Unnamed: 2']) == True:
        df_q.iloc[index]['Unnamed: 2'] = df_q.iloc[index+1]['Unnamed: 2']
df_q.head(50)

df_q=df_q[df_q['RecordNo'] != 'Standard Attributes']

df_q=df_q[df_q['RecordNo'] != 'Valid Values']

df_q.drop('Unnamed: 1', axis=1, inplace=True)

df_q.reset_index(drop=True, inplace=True)

df_q.head(50)

df_q.rename(columns = {'RecordNo':'code', 'Unnamed: 2': 'question'}, inplace = True)
df_q

code_dict={}
for index, row in df_q.iterrows():
    code = row['code']
    q = row['question']
    code_dict[code]=q
code_dict

codes = ['qweek', 
 'age', 'weight', 'gender', 'household_size', 'household_children','employment_status',
 'i1_health', 'i2_health', 'i7a_health', 'i3_health', 'i4_health',  
 'i5_health_1', 'i5_health_2', 'i5_health_3', 'i5_health_4', 'i5_health_5', 'i5_health_99',
 'i5a_health', 'i6_health', 'i9_health', 'i10_health', 'i11_health', 'i12_health_1', 'i12_health_2',
 'i12_health_6','i12_health_8','i12_health_9','i12_health_10','i12_health_11', 'i12_health_12',
 'i12_health_13','i12_health_17','i12_health_18', 'i12_health_21',
 'm8_1', 'm8_2', 'm8_3', 'm8_4', 'm8_5', 'm8_6', 'm8_7', 'm8_8', 'm8_96', 'm8_99', 
 'd1_health_1', 'd1_health_2', 'd1_health_3','d1_health_4', 'd1_health_5', 'd1_health_6', 'd1_health_7', 'd1_health_8', 'd1_health_9',
 'd1_health_10', 'd1_health_11', 'd1_health_12', 'd1_health_13', 'd1_health_98', 'd1_health_99',
 'WCRex1', 'WCRex2', 'WCRV_4', 
 'Soc1_1', 'Soc1_2', 'Soc1_3', 
 'm1_1', 'm1_2', 'm1_3', 'm2', 'm3', 'm7_1', 'm7_2', 'm7_3', 'm7_4', 'm7_5', 'm7_6', 'm7_8', 'm7_9', 'm7_10', 'm7_11', 
 'm14_1', 'm14_2', 'm14_3', 'm14_4', 'm14_5', 'm14_6', 'm14_7', 'm14_8', 'm14_9', 'm14_10', 'm14_11', 'm14_96', 'm14_99',
 'v1', 'v2_1', 'v2_2','v2_3','v2_4','v2_5','v2_99', 'v3', 'v3_open', 'vac', 
 'vac_2', 'vac2_1', 'vac2_2', 'vac2_3', 'vac2_4', 'vac2_5', 'vac2_6', 'vac2_7', 'vac4', 'vac5', 'vac7','vac12_12',  
 'vac12_13', 'r1_8',
 'av1_1', 'av1_2', 'av1_3', 'av2',
 'r1_1', 'r1_2', 'r1_3', 'r1_4', 'r1_5', 'r1_6', 'r1_7',
 'ct2', 'ct4', 
 'ox1_1', 'ox1_2', 'ox3_1', 'ox3_2', 'ox3_4', 'ox6', 
 'w1', 'w2', 'w4_1', 'w4_2', 'w4_3', 'w4_6', 'w4_7', 'w4_8', 
 'work1', 'work2', 'work3', 'work4', 'work5',
 'cantril_ladder', 'PHQ4_1', 'PHQ4_2', 'PHQ4_3', 'PHQ4_4', 'w9_1', 'w9_2', 'w9_3', 'w9_4', 'w9_5']

emp_dict={
'employment_status_1': 'Full time employment',
'employment_status_2': 'Part time employment',
'employment_status_3': 'Full time student',
'employment_status_4': 'Retired',
'employment_status_5': 'Unemployed',
'employment_status_6': 'Not working',
'employment_status_7': 'Other'
}

def emp_helper(df):
    for index, row in df.iterrows():
        for k in emp_dict:
            if row[k] == 'Yes':
                df.loc[index, 'employment_status'] = emp_dict[k]
    drop_list=list(emp_dict.keys())
    df.drop(drop_list, axis=1, inplace=True)
    return df

dataframe_country_dict = {}
for country in countries:
    file_name=f'data/{country}.csv'
    print(country)
    df = pd.read_csv(file_name, low_memory=False)
    if country == 'denmark' or country == 'norway':
        df["employment_status"] = ""
        df = emp_helper(df)
    df=df[codes]
    df['Country'] = country
    df.rename(columns = code_dict, inplace = True)
    dataframe_country_dict[country] = df


df_a = dataframe_country_dict['denmark'] 
#df_a = df_a[df_a.qweek=='week 33']
df_a

dataframe_country_dict['denmark']['qweek'] = dataframe_country_dict['denmark']['qweek'].apply(lambda x: x[5:])
dataframe_country_dict['denmark']

dataframe_country_dict['denmark']['Weight'].dtype

dataframe_country_dict['denmark']['Gender'] = dataframe_country_dict['denmark']['Gender'].map( {'Male':0, 'Female':1})
dataframe_country_dict['denmark']['Gender'].dtype

households =['Number of people in household', 'Number of children under 18 in household']

dataframe_country_dict['denmark'][households] = dataframe_country_dict['denmark'][households].apply(lambda x: x[:1])

dataframe_country_dict['denmark']['Number of people in household']=dataframe_country_dict['denmark']['Number of people in household'].astype(int)

dataframe_country_dict['denmark']['Number of children under 18 in household']

dataframe_country_dict['denmark']

[

'household_children', - int (7 don’t know, 8 prefer not to say)

'employment_status',

        1- Full time employment

        2- Part time employment

        3- Full time student

        4- Retired

        5- Unemployed

        6- Not working

        7- Other

            

 


'i1_health', - int

'i2_health', - int

'i7a_health', - int

'i3_health',

        1- Yes, and I tested positive

        2- Yes, and I tested negative

        3- Yes, and I have not received my results from the test yet

        4- No, I have not

 

 

'i4_health', 

        1- Yes, and they tested positive

        2- Yes, and they tested negative

        3- Yes, and they have not received their results from the test yet

        4- No, they have not

        5- Not sure

 


'i9_health',

        1- Yes

        2- No

        3- Not sure

 

'i10_health', -- can be int

        1- Very easy

        2- Somewhat easy

        3- Neither easy nor difficult

        4- Somewhat difficult

        5- Very difficult

        99- Not sure

       

'i11_health' -- can be int
        1- Very willing

        2- Somewhat willing

        3- Neither willing nor unwilling

        4- Somewhat unwilling

        5- Very unwilling

        99- Not sure

 
'i12_health_1', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

       

'i12_health_2', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

 

'i12_health_6', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

'i12_health_8', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

'i12_health_9', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

'i12_health_10' -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

'i12_health_11', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

'i12_health_12', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

'i12_health_13', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

'i12_health_17', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

'i12_health_18', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

'i12_health_21', -- can be int

        1- Always

        2- Frequently

        3- Soemtimes

        4- Rarely

        5- Not at all

 

 

 

ALL INT YES NO…

'd1_health_1',

'd1_health_2',

'd1_health_3',

'd1_health_4',

'd1_health_5',

'd1_health_6',

'd1_health_7',

'd1_health_8',

'd1_health_9',

'd1_health_10',

'd1_health_11',

'd1_health_12',

'd1_health_13',

'd1_health_98', prefer not to say

'd1_health_99', none of these - GET RID

 

 

'WCRex1', - int

        1- Very well

        2- Somewhat well

        3- Somewhat badly

        4- Very badly

        5- Don't know

 

'WCRex2', - int

        1- A lot of confidence

        2- A fair amount of confidence

        3- Not very much confidence

        4- No confidence at all

        5- Don't know

 

'WCRV_4', - int

        1- I am very scared that I will contract the Coronavirus (COVID-19)

        2- I am fairly scared that I will contract the Coronavirus (COVID-19)

        3- I am not very scared that I will contract the Coronavirus (COVID-19)

        4- I am not at all scared that I will contract the Coronavirus (COVID-19)

        977- Don't know

        988- Not applicable -I have already contracted Coronavirus (COVID-19)

 

'Soc1_1', - ALL int Yes, No

'Soc1_2',

'Soc1_3',

 

 

'm1_1', -- can be int
        1- Very willing

        2- Somewhat willing

        3- Neither willing nor unwilling

        4- Somewhat unwilling

        5- Very unwilling

        99- Not sure

 

'm1_2', -- can be int
        1- Very willing

        2- Somewhat willing

        3- Neither willing nor unwilling

        4- Somewhat unwilling

        5- Very unwilling

        99- Not sure

 

'm1_3', -- can be int
        1- Very willing

        2- Somewhat willing

        3- Neither willing nor unwilling

        4- Somewhat unwilling

        5- Very unwilling

        99- Not sure

 

'm2', int

'm3', int

'm7_1', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm7_2', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm7_3', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm7_4', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm7_5', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm7_6', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm7_8', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm7_9', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm7_10', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm7_11', - int

        1- Very much

        2- Somewhat

        3- Not at all

        99- Not sure

 

'm14_1', - int

        0- No

        1- Yes

'm14_2'- int

        0- No

        1- Yes

,

'm14_3'- int

        0- No

        1- Yes

,

'm14_4'- int

        0- No

        1- Yes

,

'm14_5'- int

        0- No

        1- Yes

,

'm14_6'- int

        0- No

        1- Yes

,

'm14_7'- int

        0- No

        1- Yes

,

'm14_8'- int

        0- No

        1- Yes

,

'm14_9'- int

        0- No

        1- Yes

,

'm14_10'- int

        0- No

        1- Yes

,

'm14_11'- int

        0- No

        1- Yes

,

'm14_96'- int

        0- No

        1- Yes

,

'm14_99'- int

        0- No

        1- Yes

,

 

 

 

'v1', int-

        1- Yes

        2- No

        3- Not sure

 

'v2_1', int-

        0- No

        1- Yes

'v2_2', int-

        0- No

        1- Yes

 

'v2_3', int-

        0- No

        1- Yes

 

'v2_4', int-

        0- No

        1- Yes

 

'v2_5', int-

        0- No

        1- Yes

 

'v2_99', int-

        0- No

        1- Yes


'v3', - dummies

      1- The government said that people can leave home only for essential services

      2- A healthcare provider recommended delaying or missing vaccines

      3- The vaccination clinic is closed or not giving vaccines due to COVID-19

      4- It's hard to get an appointment even though the vaccination clinic is open

      5- Couldn't afford it

      6- Wanted to save health services for the people who really need them now

      7- People don't need vaccines now because no one is going out

      8- Worry about getting COVID-19 by leaving leave the house

      9- Worry about getting COVID-19 when on public transit to get to the vaccination clinic

      10- Worry about getting COVID-19 at the vaccination clinic

      11- Worry about giving COVID-19 to other people at the vaccination clinic

                99- Something else

 

'vac', - int

        1- No, neither

        2- Yes, one dose

        3- Yes, two doses


'vac4', -int

        1- Not at all important

        2- A little important

        3- Moderately important

        4- Very important

'vac6', -int

        0- No

        1- Yes

        99- Not sure

'vac7', -int

        1- Not at all

        2- A little

        3- Moderately

        4- Very much

'vac12_12',  ALL in No, Yes

'vac12_13',

 


'av1_1', ALL int No, Yes

'av1_2',

'av1_3',

'av2', -int

        1- Yes, I think more research needs to be done before I will consider receiving the vaccine

        2- No, I don't think more research needs to be done before I will consider receiving the vaccine

        99- Not sure

 

'r1_1' - int, 1-7, Disagre, Agree

'r1_2'- int,

'r1_3'- int,

'r1_4'- int,

'r1_5'- int,

'r1_6'- int,

'r1_7'- int,

'r1_8'- int

'r1_9'- int

 

 

'ct2', - int

        0- No

        1- Yes

        99- Not sure

 

'ct4', - int

        0- No

        1- Yes

        99- Not sure

 

 


'ox1_1', - int

        1- Much lower

        2-

        3- The same

        4-

        5- Much higher

 

'ox1_2', - int

        1- Much lower

        2-

        3- The same

        4-

        5- Much higher

 

'ox3_1', - int

        1- Strongly agree

        5- Strongly disagree

'ox3_2', - int

        1- Strongly agree

        5- Strongly disagree

 

'ox3_4', - int

        1- Strongly agree

        5- Strongly disagree

 

'ox6', - int

        1- Not efficient at all

        2- Extremely efficient

 

'w1', - int

        1- More united

        2- No change

        3- More divided

 

'w2', - int

        1- Very stong

        2- Somewhat strong

        3- Somewhat weak

        4- Very weak

 

'w4_1', -- ALL int No, Yes

'w4_2',

'w4_3',

'w4_6',

'w4_7',

'w4_8',

 

'WAH4' - int, YB, NS

 

'work1', - int

        1- Yes, fully

        2- Yes, partly

        3- No, not at all

'work2', -int

        1- No

        2- Yes, within past 2 weeks

        3- Yes, between 2 weeks and 2 months ago

        4- Yes, more than two months ago but since 1st February 2020


'work3', -int

        1- No

        2- Yes, that started within past 2 weeks

        3- Yes, between 2 weeks and 2 months ago

        4- Yes, more than two months ago but since 1st February 2020

 

'work4', -int

        1- Very likely

        2- Quite likely

        3- Neother likely nor unlikely

        4- Quite unlikely

        5- Very unlikely

        98- Don't know

 

'work5', - int

        1- Yes, fully

        2- Yes, partly

        3- No, not at all

 

 

'cantril_ladder', -- INT, 0-10

'PHQ4_1', - int

        1- Not at all

        2- Several days

        3- More than half the days

        4- Nearly every day

        99- Prefer not to say

 

'PHQ4_2', - int

        1- Not at all

        2- Several days

        3- More than half the days

        4- Nearly every day

        99- Prefer not to say

 

'PHQ4_3', - int

        1- Not at all

        2- Several days

        3- More than half the days

        4- Nearly every day

        99- Prefer not to say

 

'PHQ4_4', - int

        1- Not at all

        2- Several days

        3- More than half the days

        4- Nearly every day

        99- Prefer not to say

 

'w9_1', - int

        1- At no time

        2- Some of the time

        3- Less than half of the time

        4- More than half of the time

        5- Most of the time

        6- All the time

'w9_2', - int

        1- At no time

        2- Some of the time

        3- Less than half of the time

        4- More than half of the time

        5- Most of the time

        6- All the time

 

'w9_3', - int

        1- At no time

        2- Some of the time

        3- Less than half of the time

        4- More than half of the time

        5- Most of the time

        6- All the time

 

'w9_4', - int

        1- At no time

        2- Some of the time

        3- Less than half of the time

        4- More than half of the time

        5- Most of the time

        6- All the time

 

'w9_5'- int

        1- At no time

        2- Some of the time

        3- Less than half of the time

        4- More than half of the time

        5- Most of the time

        6- All the time

]