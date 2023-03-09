import pandas as pd
from faker import Faker

# Initialize Faker
faker = Faker()

# # read in existing file
# existing_file = pd.read_csv('/home/sakabuana31/training/create_data/source/sales_data.csv')


# Create an empty dataframe
df = pd.DataFrame(columns=['customer_name', 'income', 'spending'])

# Fill the dataframe with 10 random records
for i in range(200):
    data = {'customer_name': faker.name(),
            'income': faker.random_number(digits=7),
            'spending': faker.random_number(digits=7)}

    df = pd.concat([df, pd.DataFrame(data, index=[0])], ignore_index=True)

# specify the directory and file name to save the CSV file
file_path = '/home/sakabuana31/DigitalSkola/Learning/HW_W11_K_MEANS_CLUSTER/input_data/sales_data.csv'

# Save the dataframe to a CSV file
df.to_csv(file_path, index=False)

# read in new file
new_file = pd.read_csv('/home/sakabuana31/training/create_data/source/sales_data.csv')

# # # merge the two dataframes
# # merged_data = pd.concat([existing_file, new_file])

# # save to new csv file in specific directory
# merged_data.to_csv('/home/sakabuana31/training/create_data/source/sales_data.csv', index=False)