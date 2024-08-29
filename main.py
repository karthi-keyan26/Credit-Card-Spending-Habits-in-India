import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('Creditcardtransactions-India.csv')
print("Checking the first 10 elements")
print(data.head(10))

# checking the info of the data
print(data.info())


data = data.replace('F', 'Female')
data = data.replace('M', 'Male')

# Total amount spend by gender
total_amount_spend_by_gender = data.groupby('Gender')['Amount'].sum()
print("Total amount spend by gender")
print(total_amount_spend_by_gender)

# Average transaction amount by card type
avg_trans_amount_card_type = data.groupby('Card Type')['Amount'].mean()
print(avg_trans_amount_card_type)

# Total amount spend by city filtered by top 10
total_amount_spend_by_city = data.groupby('City')['Amount'].sum().sort_values(ascending=False)
print(total_amount_spend_by_city.head(10))

# Total amount spend by expense type
total_amount_spend_by_exptype = data.groupby('Exp Type')['Amount'].sum().sort_values(ascending=False)
print(total_amount_spend_by_exptype)

# Visualizations

# Total amount spend by gender
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.barplot(x=total_amount_spend_by_gender.index, y=total_amount_spend_by_gender.values)
plt.title('Total amount spend by gender')
plt.xlabel('Gender')
plt.ylabel('Total Amount')

# Average transaction amount by card type
plt.subplot(2, 2, 2)
sns.barplot(x=avg_trans_amount_card_type.index, y=avg_trans_amount_card_type.values)
plt.title('Average transaction amount by card type')
plt.xlabel('Card Type')
plt.ylabel('Average Amount')

# Total amount spent by city
plt.subplot(2, 2, 3)
sns.barplot(x=total_amount_spend_by_city.head(10).index, y=total_amount_spend_by_city.head(10).values)
plt.title('Total amount spent by city (Top 10)')
plt.xlabel('City')
plt.ylabel('Total Amount')
plt.xticks(rotation=90)

# Total Expense over the Genders
plt.subplot(2, 2, 4)
g = sns.barplot(x=data['Exp Type'], y=data['Amount'], hue='Gender', data=data)
sns.move_legend(g, "upper left", bbox_to_anchor=(.78, .99), title='Genders')
plt.title('Expense over the types')
plt.xlabel('Expense Type')
plt.ylabel('Total Amount')

plt.tight_layout()
plt.show()
