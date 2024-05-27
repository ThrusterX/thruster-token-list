# Thruster Token Listing
This repo serves as an easy way to submit tokens for whitelisting on Thruster's token list. Pull requests (PRs) will be processed every 5-10 days, for more urgent requests please reach out to the team on Discord -- spam will be rejected.

## Prerequisites
In order for any submitted request to be considered, Thruster requires the following:
- Verified token contract address on Blastscan
- Over $100,000 of ETH/USDB liquidity in your primary liquidity pool
- Twitter presence, or if no established representation and history on Twitter then locked/burnt LP

## Getting Started
To submit a request to whitelist a token on the Thruster frontend, you must do the following in a pull request:
- In the corresponding chain directory in `/chains` (e.g. Blast is 81457), create a directory in `/assets` using the token contract address **in lowercase**.
    - **Note:** Do not modify the `token-list.json` file at the root of the chain directories, this file is auto-generated.
- For your token directory, you must create 2 files:
    - `token-info.json`
        - You must add the following:
            - `tokenAddress`: lower case contract address which should match your folder name
            - `tokenName`: the token name on the blockchain
            - `tokenSymbol`: the token symbol on the blockchain
            - `tokenDecimals`: the decimals of the token on the blockchain
            - `tokenCategory`: desired category for the token (i.e. `DeFi`, `Stablecoin`, `Memecoin`, or by default `Other`)
    - `token-logo.svg`
        - A svg file image of your token logo as a circle, which **MUST** be under 150 KB. Rectangles and other shapes of images will not be accepted.
- Additionally, in the submitted PR, please add a brief description of the type of token if the token contract is non-standard (e.g. non-ERC20, BT404, tax).

When you create a PR, a checklist of the above requirements should automatically be populated to help you make sure to submit the necessary information. **Your PR will not be accepted unless all information is complete.**

If you have any additional information or requests (e.g. changing default token name, otherwise will be pulled from contract), please add any info under the *Additional Information* section in the pull request.

## Disclaimer
Thruster allows anyone to submit new assets to this repository. However, this does not mean that Thruster endorses any of these projects. It is important that individuals performs their own due diligence and risk assessment.

Thruster will reject projects that are deemed as scams or fraudulent after careful review. Thruster reserves the right to change the terms of asset submissions at any time due to changing market conditions, risk of fraud, or any other factors Thruster deems relevant.
