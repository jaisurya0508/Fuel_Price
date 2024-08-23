import requests

url = 'http://localhost:5000/predict_api' 
r = requests.post(url,json={'drivenKM':300,'model':0})

print(r.json())

import numpy as np
import pandas as pd

def age_most_recent_account(response):
    """
    A function to calculate the Age in months of the most recently opened account (for all accounts).
    Includes debug information.
    """
    age_most_recent_account = np.inf
    try:
        # Ensure 'Accounts' exists and is a list
        accounts = response.get('Accounts', [])
        if not isinstance(accounts, list):
            print(f"Expected list in 'Accounts', got: {type(accounts)}")
            return np.nan
        
        # Debugging: Check each account's AgeOfAccount
        for acct in accounts:
            age = acct.get('AgeOfAccount', None)
            if age is not None:
                print(f"Found AgeOfAccount: {age}")
                age_most_recent_account = min(age_most_recent_account, age)
            else:
                print("AgeOfAccount is None or missing")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Handle case where no valid age was found
    if age_most_recent_account == np.inf:
        return np.nan

    return age_most_recent_account

# Apply the function to your DataFrame
df_efx["AgeMostRecentAccount"] = df_efx["BureauData_f2"].map(lambda x: age_most_recent_account(x))
