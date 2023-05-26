import pandas as pd

def load_data():
    try:
        df = pd.read_csv('characters.csv')
    except FileNotFoundError:
        print("File not found. Please make sure the 'characters.csv' file exists.")
        return pd.DataFrame(columns=['name', 'role', 'abilities'])  # returns an empty DataFrame
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame(columns=['name', 'role', 'abilities'])  # returns an empty DataFrame
    return df

def add_character(df, name, role, abilities):
    # Create a dictionary with the new character's information.
    new_character = pd.DataFrame({'Name': [name], 'Role': [role], 'Abilities': [abilities]})

    # Add the new character to the DataFrame.
    df = pd.concat([df, new_character], ignore_index=True)

    # Return the updated DataFrame.
    return df

def edit_character(df, name, role=None, abilities=None):
    # Check if the character exists in the DataFrame.
    if name in df['Name'].values:
        # If the character is in the DataFrame, update their role and abilities.
        if role:
            df.loc[df['Name'] == name, 'Role'] = role
        if abilities:
            df.loc[df['Name'] == name, 'Abilities'] = abilities
    else:
        # If the character is not in the DataFrame, add them.
        df = add_character(df, name, role, abilities)

    # Return the updated DataFrame.
    return df

def delete_character(df, name):
    if name in df['Name'].values:
        df = df[df['Name'] != name]
        df.to_csv('characters.csv', index=False)
    else:
        print(f"Character '{name}' not found in the database.")
  
def view_all(df):
    print(df)

df = load_data()
view_all(df)
add_character(df, 'New Character', 'Protagonist', 'Super Strength')
edit_character(df, 'New Character', abilities='Super Speed')
delete_character(df, 'New Character')
