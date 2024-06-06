import os
import re
import json
import sys

def validate_filename(directory):
    filename = os.path.basename(directory)
    if not re.match(r'^0x[a-f0-9]{40}$', filename):
        print(f"Invalid filename: {filename}. It should match the regex /^0x[a-f0-9]{40}$/")
        return False
    return True

def validate_json(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Invalid JSON format: {json_file}")
        return False
    
    required_properties = ["tokenAddress", "tokenName", "tokenSymbol", "tokenDecimals", "tokenCategory"]
    missing_properties = [prop for prop in required_properties if prop not in data]
    
    if missing_properties:
        print(f"Missing required properties in: {json_file}, {missing_properties}")
        return False
    
    # Ensure tokenCategory is valid
    valid_categories = ["Stablecoin", "DeFi", "Memecoin", "Game", "Other"]
    if data["tokenCategory"] not in valid_categories:
        print(f"Invalid tokenCategory in: {json_file}")
        return False
    
    return True

def validate_assets_directory(assets_dir):
    all_valid = True

    for dir_name in os.listdir(assets_dir):
        dir_path = os.path.join(assets_dir, dir_name)
        if os.path.isdir(dir_path):
            print(f"Validating files in: {dir_path}")
            if not validate_filename(dir_path):
                all_valid = False
                break

            token_info = os.path.join(dir_path, "token-info.json")
            if os.path.isfile(token_info):
                if not validate_json(token_info):
                    all_valid = False
                    break
            else:
                print(f"Missing token-info.json in: {dir_path}")
                all_valid = False
                break

            token_logo = os.path.join(dir_path, "token-logo.svg")
            if not os.path.isfile(token_logo):
                print(f"Missing token-logo.svg in: {dir_path}")
                all_valid = False
                break

    return all_valid

# Validate files in the assets directory of each chain
CHAINS_PATH = "chains"
all_chains_valid = True

for chain_dir_name in os.listdir(CHAINS_PATH):
    chain_dir_path = os.path.join(CHAINS_PATH, chain_dir_name)
    assets_dir = os.path.join(chain_dir_path, "assets")
    if os.path.isdir(chain_dir_path) and os.path.isdir(assets_dir):
        print(f"Validating assets in: {assets_dir}")
        if not validate_assets_directory(assets_dir):
            all_chains_valid = False
            break
    else:
        print(f"Missing assets directory in: {chain_dir_path}")
        all_chains_valid = False
        break

if all_chains_valid:
    print("All validations passed.")
    sys.exit(0)
else:
    print("Validations failed.")
    sys.exit(1)
