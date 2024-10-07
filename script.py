#You’re the lead data analyst for a chain of gardening stores called Petal Power. Help them analyze their inventory!

import pandas as pd

#Data for all of the locations of Petal Power is in the file inventory.csv. Load the data into a DataFrame called inventory.
inventory = pd.read_csv('inventory.csv')

#Answer Customer Emails

#The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.
staten_island = inventory.head(10)

#A customer just emailed you asking what products are sold at your Staten Island location.
product_request = staten_island.product_description

#Another customer emails to ask what types of seeds are sold at the Brooklyn location.
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')] 

#Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.
inventory['in_stock'] = inventory.quantity.apply(lambda units: True if units > 0 else False)

#Petal Power wants to know how valuable their current inventory is.
inventory['total_value'] = inventory.apply(lambda row: row.price * row.quantity, axis=1) 

#The Marketing department wants a complete description of each product for their catalog.
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)     

#Export DataFrame as an HTML table
html_table = inventory.head(10).to_html(index=False, classes='table table-striped')

# Save the HTML table in a file
with open("table.html", "w") as file:
    file.write(html_table)

print("HTML table generated and saved to table.html")

#Read index.html
with open('index.html', 'r') as file:
    html_content = file.read()

#Inject the inventory table where the placeholder comment is located
html_content = html_content.replace('<!--TABLE_PLACEHOLDER-->', html_table)

# Write the updated content back to index.html
with open('index.html', 'w') as file:
    file.write(html_content)

print("HTML table injected into index.html")
print(inventory.head(10))
print(seed_request)

# Run this in terminal
# python -m http.server 8000 - creates a local host
# Open http://localhost:8000/index.html
