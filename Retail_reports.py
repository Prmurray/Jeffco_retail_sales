import pandas as pd
import matplotlib.pyplot as plt

report = pd.read_csv('Retail_Reports_by_County_in_Colorado.csv')

jeffco = (report[report['county'] == 'Jefferson'].dropna(axis='columns'))

sales_2015_full = jeffco.loc[((jeffco['year'] == 2015)), ['retail_sales']]

jeffco_2015 = jeffco.loc[((jeffco['year'] == 2015) & (jeffco['month'] < 9)), ['retail_sales']]
jeffco_2016 = jeffco.loc[((jeffco['year'] == 2016) & (jeffco['month'] < 9)), ['retail_sales']]
jeffco_2017 = jeffco.loc[((jeffco['year'] == 2017) & (jeffco['month'] < 9)), ['retail_sales']]
jeffco_2018 = jeffco.loc[((jeffco['year'] == 2018) & (jeffco['month'] < 9)), ['retail_sales']]
jeffco_2019 = jeffco.loc[((jeffco['year'] == 2019) & (jeffco['month'] < 9)), ['retail_sales']]
jeffco_2020 = jeffco.loc[((jeffco['year'] == 2020) & (jeffco['month'] < 9)), ['retail_sales']]
jeffco_2021 = jeffco.loc[((jeffco['year'] == 2021) & (jeffco['month'] < 9)), ['retail_sales']]

#2015's retail sales needed to be multiplied by 1000 to make them the same format as the other years.
sales_2015_full = jeffco.loc[((jeffco['year'] == 2015)), ['retail_sales']]
sales_list = sales_2015_full['retail_sales']
new_2015_sales = []
for item in sales_list:
    new_2015_sales.append(item*1000)

jeffco.loc[jeffco['year'] == 2015, 'retail_sales'] = new_2015_sales

by_year = jeffco.groupby('year').sum()
annual_retail_sales = by_year['retail_sales']

jan_thru_aug = [round(jeffco_2015['retail_sales'].sum()*1000, -3), jeffco_2016['retail_sales'].sum(), jeffco_2017['retail_sales'].sum(),
                jeffco_2018['retail_sales'].sum(), jeffco_2019['retail_sales'].sum(), jeffco_2020['retail_sales'].sum(),
                round(jeffco_2021['retail_sales'].sum(), -3)]

years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']

#two bar graphs, one showing the full year retail sales (2015-2020) and Januar - August sales (2015 - 2021)
annual_retail_sales.plot.bar()
plt.bar(years, jan_thru_aug)


#Here's my attempt at a FiveThirtyEight style stacked bar graph 
fig, ax=plt.subplots(figsize=(4, 6))

fig.text(0, 0.9, "The pandemic hasn't slowed Jeffco's economy", weight='bold')
fig.text(0, 0.87, "2021 Retail sales are poised to reach another record high", size=9)
fig.text(0.5, 0.2, "January - August", alpha=0.5, rotation=90, weight='bold')
fig.text(0.5, .53, "Sept - Dec", alpha=0.5, rotation=90, weight='bold')


ax.bar(years, annual_retail_sales, color="#6d904f", width=0.75)
ax.bar(years, jan_thru_aug, color="#e5ae38", width=0.75)
ax.set_yticklabels([])
ax.set_xticklabels(['2015','','2017','','2019','','2021'])
for side in ['top', 'bottom', 'left', 'right']:
    ax.spines[side].set_visible(False)
ax.tick_params(left=0, bottom=0)

ax.text(-1.8, 9600000000, "$10", size=15, c='grey', alpha=0.6)
ax.text(-1.8, 19600000000, "$20", size=15, c='grey', alpha=0.6)
ax.text(-.6, 20300000000, "Retail Sales (Billion)", size=10, c='grey', alpha=0.6)
ax.axhline(y=10000000000, c='grey', alpha=0.5)
ax.axhline(y=20000000000, c='grey', alpha=0.5)
ax.text(3, -450000000, "Source: Colorado Department of Revenue", size=5, c='grey', alpha=0.8)


plt.show()