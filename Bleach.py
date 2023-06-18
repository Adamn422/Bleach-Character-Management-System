import pandas as pd

def load_data():
    try:
        df = pd.read_csv('characters.csv')
    except FileNotFoundError:
        print("File not found. Please make sure the 'characters.csv' file exists.")
        return pd.DataFrame(columns=['Name', 'Race', 'Ability'])  # returns an empty DataFrame
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame(columns=['Name', 'Race', 'Ability'])  # returns an empty DataFrame
    return df

def add_character(df, name, race, ability):
    new_character = pd.DataFrame({'Name': [name], 'Race': [race], 'Ability': [ability]})
    df = pd.concat([df, new_character], ignore_index=True)
    df.to_csv('characters.csv', index=False)  # Save the updated DataFrame to the CSV file
    return df

def edit_character(df, name, race=None, ability=None):
    if name in df['Name'].values:
        if race:
            df.loc[df['Name'] == name, 'Race'] = race
        if ability:
            df.loc[df['Name'] == name, 'Ability'] = ability
    else:
        df = add_character(df, name, race, ability)
    df.to_csv('characters.csv', index=False)  # Save the updated DataFrame to the CSV file
    return df

def delete_character(df, name):
    if name in df['Name'].values:
        df = df[df['Name'] != name]
        df.to_csv('characters.csv', index=False)
        print(f"Character '{name}' deleted successfully.")
        return df
    else:
        print(f"Character '{name}' not found in the database.")
        return df

def view_all(df):
    print(df)

df = load_data()
print("Initial data:")
view_all(df)

print("\nAdding new character:")
df = add_character(df, 'New Character', 'New Race', 'New Ability')
view_all(df)

print("\nEditing new character:")
df = edit_character(df, 'New Character', ability='Edited Ability')
view_all(df)

print("\nDeleting new character:")
df = delete_character(df, 'New Character')
view_all(df)


