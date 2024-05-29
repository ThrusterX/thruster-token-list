#!/bin/bash

CHAINS_PATH="chains"
TOKEN_LIST_FILENAME="token-list.json"

process_chain() {
  local chain_dir=$1
  local assets_path="$chain_dir/assets"
  local token_list_path="$chain_dir/$TOKEN_LIST_FILENAME"
  
  echo "Processing chain directory: $chain_dir"
  
  # Initialize token list array
  local token_list="[]"
  
  # Iterate over each subdirectory in the assets directory
  for dir_name in "$assets_path"/*; do
    if [ -d "$dir_name" ]; then
      local token_info_path="$dir_name/token-info.json"
      local token_logo_path="$dir_name/token-logo.svg"
      
      if [ -f "$token_info_path" ] && [ -f "$token_logo_path" ]; then
        local token_info=$(cat "$token_info_path")
        token_list=$(echo "$token_list" | jq --argjson token_info "$token_info" '. + [$token_info]')
      else
        echo "token-info.json or token-logo.svg not found in $dir_name"
      fi
    fi
  done

  # Read existing token list if it exists
  if [ -f "$token_list_path" ]; then
    local existing_token_list=$(cat "$token_list_path")
  else
    local existing_token_list="[]"
  fi

  # Sort token list by tokenAddress
  token_list=$(echo "$token_list" | jq 'sort_by(.tokenAddress)')

  # Check if the new token list is different from the existing one
  if [ "$token_list" != "$existing_token_list" ]; then
    # Write updated token list to token-list.json
    echo "$token_list" | jq '.' > "$token_list_path"
    echo "Written updated token list to $token_list_path"
  else
    echo "No changes detected in $token_list_path, skipping write."
  fi
}

# Iterate over each subdirectory in the chains directory
for chain_dir in "$CHAINS_PATH"/*; do
  if [ -d "$chain_dir" ]; then
    process_chain "$chain_dir"
  else
    echo "No directories found in $CHAINS_PATH"
  fi
done

echo "All token lists updated."
