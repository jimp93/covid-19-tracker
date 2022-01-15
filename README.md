## Project Overview

Following warnings from the WHO and the UN that the pandemic has inreased risk factors for suicide [1, 2], the UK government approached our consultancy firm in order to identify the groups most at risk of mental health problems. These will be the targets of an upcoming awareness campaign. <br>

To do this, we analysed data from the Imperial College London/YouGov Covid-19 Behaviour Tracker Data Hub.

The dataset is designed to provide behavioural analysis on how different populations are responding to the pandemic by, every two weeks, anonymously surveying around a 1,000 people in each of around 12 countries around the world (the number can vary). 

The questions in the survey cover data on general behaviours, attitudes towards vaccination, country, age, number of people in the household, pre-existing health conditions, working status and mental health. <br>

Various techniques were then used in order to model whether a respondent would say they had felt derpressed during the previous week, given their reposnses to the other questions. <br>

The best performing models were around 70% accurate, and caught around 75% of cases in which respondents said they had felt depressed. <br>

We then analysed the internal workings of the model to understand which factors were the strongest predictors of mental health problems, and which groups the government should target during its campaign. <br>

Creating a strong predictive model can also help tailor surveys for those interacting with country's National Health Service (NHS), which could help identify indiviudals at risk without having to ask outright. This is an advantage as sometimes those who are suffering from issues are reluctant to say so. <br>

The UK's Covid taskforce shares its insights with other governments, so any findings of international discrepancies are also of interest to us. <br>

<img src="images/logo.png" style="width: 700px;"/>

<br>
<br>

### Business Problem

To identify the groups most at risk from mental health problems in the pandemic for an upcoming UK government awareness campaign. <br>

This involves creating a string predicitve model, and also inferring from the workings of the model which factors most increase the odds of someone suffering mental health issues. <br>

Our insights can also be used by the NHS to flag up any high-risk cases, without having to directly quiz them about this highly-sensitive issue.<br>

Any findings in international interest can be shared with the relevant governments.<br>

<img src="images/seattle.jpg" style="width: 700px;"/>
<br>
<br>

### The Data

Data drawn from the Imperial College London/YouGov Covid-19 Behaviour Tracker Data Hub.

https://github.com/YouGov-Data/covid-19-tracker

The dataset comprises surveys of around 400 questions carried out by hundreds of thousands of respondents from 29 countries around the world.

There was variation in which questions were posed by different countries, and which countries provided regular data.

Infrequently answered questions, and repetitious ones, were removed from the dataset, leaving around 35 questions that covered the main issues surrounding personal attitudes towards the pandemic.

We focussed on the 11 countries that provided the most comprehensive responses. These were: Australia, Canada, Denmark, France, Germany, Italy, Norway, Spain, the UK and the US.

<br>
<br>

### Methods

The final dataset of over 130,000 reposnses sales was analyzed to find the strength of relationships between reponses to each question and the response to the question 'at any point during the last week, have you been feeling down, depressed, or hopeless?'. <br>

The end goal was to create an accurate model, and to find out which factors were given the heaviest weighting by the most accurate models. <br>

To do this, we created a series of models using logitstic regression, decision trees, random forests and gradient boosting.

Each model was then put to the test with previously unseen data, and its perfomance calculated in terms of how accurately it could predict whether a respondent would answer 'yes' or 'no' to the question of whether they had recently suffered from depression or hopelessnes. <br>

We were also interested in how many of those answering 'yes' that the model caught. <br>

If used by the NHS to flag up potential high-risk cases, we could sacrifice some accuracy in order to increase this number and make it less likely we miss those who are suffering from problems. 

Triggering a follow-up response with someone who is not suffering from problems is less of an issue than potentially missing someone who needs help. If we tolerate misidentifying around half of those who do not have symptoms, we can catch around 85% of those who do. Knowing the factors that matter the most, we can design a custom questionnaire that should improve these metrics. <br>

Each model was tuned to maximise its performance, and the results of the best two models were analysed to find the most important factors across both.

<img src="images/seattle_heat.png" style="width: 700px;"/>
<br>
<br>

### Headline Results
<br>

**Age and gender are key factors with younger people and females most at risk of depression. Being female increased the odds or reporting symptoms by percent. <br>
<br>
<br>
<img src="images/feature_price_bar.png" style="width: 700px;"/>

**Students and unemployed people were also strong predictors of mental health issues.** <br>
<br>
<br>


<img src="images/location_price_bar.png" style="width: 700px;"/>
<br>
<br>

**People who did not leave the house often or see many other people from outside their households were more likley to suffer form depression.**
<br>

**Being Italian increased the odds of reporting depression by around 70 percent.**
<br>

**Those whose lives had been most affected by the pandemic were more likely to report mental health issues, suggesting they were triggered by the virus and the response to it.**
<br>

<img src="images/shutterstock_620724863.jpg" style="width: 700px;"/>
<br>
<br>



### Conclusion

This analysis leads to three recommendations for the government over which groups to target in its upcoming mental health awareness campaign.

**Students and unemployed people are highly vulnerable** 

* The government should work with student services at major universities to raise awareness of symptoms to look out for, and who to contact for help
* A similar campaign should be coordinated with job centres across the country.


**Young women are also at risk**

* The governemnt should run television, Facebook and Instagram campaigns targetting young men, but mmore particularly young women. 

**Inform the Italian government of the findings**

* Being Italian was the single strongest predictor of mental health problems found in the dataset. This finding should be shared with the Italian authorities handling the response to the pandemic.


### Next steps

*  Tailor a new questionnaire focussed on the key factors identified in the models. Each factor needs to be explored in more detail to produce a more granular model.<br>
* Once we are confident that we have a high-performing model, we can then produce a concise survey for the NHS to offer those who use its services. This can be ised to flag up individuals at high risk of suffering mental health problems.<br>

* Although we found that there was a strong link between those whose lives had been affected most by the virus and mental health problems, we need to analyse pre-pandemic data to identify underlying factors and more accurately model whether the mental health of certain groups has been disproportionately affected by the pandemic.<br>

* There was sparse response to questions about working from home, which made them unusable. We should conduct our own survey on this issue, as it is a potentially important factor that has only arisen during the last two years. <br>

* The reposnses on vaccine uptake and hesitancy were also a little inconsistent as different countries were at different stages in their vaccination programs during the duration of the survey. Now countries are on more of an even footing, we could conduct a survey focussed on issues surrounding access and attitudes to vaccines. 
 

<br>
<br>


https://news.un.org/en/story/2021/09/1099572

https://www.who.int/news-room/feature-stories/detail/facing-mental-health-fallout-from-the-coronavirus-pandemic