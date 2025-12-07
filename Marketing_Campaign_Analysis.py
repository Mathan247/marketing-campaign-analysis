#MARKETING CAMPAIGN ANALYSIS

#1.Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2.Load Dataset

df=pd.read_csv('Marketing_Campaign_Analysis_Dataset.csv')
print(df.head())

#3.Basic Info about Data

print(df.info())
print(df.describe())

#4.Check Missing Values

print(df.isna().sum())

#5.Data Cleaning

df=df.drop_duplicates() #Remove duplicates
df=df.fillna(0)

#6.Campaign wise performance analysis

df['campaign_id']=df['campaign_id'].apply(lambda x:'C'+''.join(filter(str.isdigit,str(x))))
plt.suptitle('Marketing Campaign Performance Analysis',fontsize=18,fontweight='bold')

#6.1 Total Clicks by Campaign (bar)

plt.subplot(2,1,1)
campaign_clicks=df.groupby('campaign_id')['clicks'].sum().sort_values()
sns.barplot(x=campaign_clicks.index,y=campaign_clicks.values,palette='Blues')
plt.title('Total Clicks by Campaign')
plt.xlabel('Campaign')
plt.ylabel('Clicks')

#6.2 Click Through Rate by Age (line)

plt.subplot(2,3,4)
ctr_by_age=df.groupby('age')['click_through_rate'].mean().reset_index()
sns.lineplot(data=ctr_by_age,x='age',y='click_through_rate',marker='o')
plt.title('Click Through Rate by Age')
plt.xlabel('Age')
plt.ylabel('Click Through Rate')

#6.3 Spend Distribution (pie)

plt.subplot(2,3,5)
spend_by_campaign=df.groupby('campaign_id')['amount_spent_in_inr'].sum()
plt.pie(spend_by_campaign,labels=spend_by_campaign.index,colors=sns.color_palette('Blues',len(spend_by_campaign)))
plt.title('Spend Distribution by Campaign (₹)')

#6.4 Cost per Click vs Clicks (scatter)

plt.subplot(2,3,6)
sns.scatterplot(data=df,x='clicks',y='cost_per_click',palette='Blues',s=100)
plt.title('Cost per Click vs Clicks')
plt.xlabel('Clicks')
plt.ylabel('Cost per Click (₹)')

plt.show()