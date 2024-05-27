import json
import os

CHAINS_PATH = "chains"
TOKEN_LIST_FILENAME = "token-list.json"

def process_chain(chain_dir):
    assets_path = os.path.join(chain_dir, 'assets')
    token_list_path = os.path.join(chain_dir, TOKEN_LIST_FILENAME)
    
    print(f"Processing chain directory: {chain_dir}")
    
    # Initialize token list array
    token_list = []
    
    # Iterate over each subdirectory in the assets directory
    for dir_name in os.listdir(assets_path):
        dir_path = os.path.join(assets_path, dir_name)
        if os.path.isdir(dir_path):
            token_info_path = os.path.join(dir_path, 'token-info.json')
            token_logo_path = os.path.join(dir_path, 'token-logo.svg')
            
            if os.path.isfile(token_info_path) and os.path.isfile(token_logo_path):
                with open(token_info_path, 'r') as f:
                    token_info = json.load(f)
                
                # Append token_info to token_list
                token_list.append(token_info)
            else:
                print(f"token-info.json or token-logo.svg not found in {dir_path}")
    
    # Read existing token list if it exists
    if os.path.isfile(token_list_path):
        with open(token_list_path, 'r') as f:
            existing_token_list = json.load(f)
    else:
        existing_token_list = []

    # Sort token list by tokenAddress
    token_list = sorted(token_list, key=lambda x: x['tokenAddress'])

    # Check if the new token list is different from the existing one
    if token_list != existing_token_list:
        # Write updated token list to token-list.json
        with open(token_list_path, 'w') as f:
            json.dump(token_list, f, indent=2)
        print(f"Written updated token list to {token_list_path}")
    else:
        print(f"No changes detected in {token_list_path}, skipping write.")

# Iterate over each subdirectory in the chains directory
for chain_dir in os.listdir(CHAINS_PATH):
    chain_dir_path = os.path.join(CHAINS_PATH, chain_dir)
    if os.path.isdir(chain_dir_path):
        process_chain(chain_dir_path)
    else:
        print(f"No directories found in {CHAINS_PATH}")

print("All token lists updated.")
