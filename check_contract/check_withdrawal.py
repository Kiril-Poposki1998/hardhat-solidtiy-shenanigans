from web3 import Web3

# Connect to Hardhat localhost node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

print(f"Is connected: {w3.is_connected()}")

# Contract details
contract_address = "0x5FbDB2315678afecb367f032d93F642f64180aa3"  # Replace with deployed contract address
owner_address = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"  # Replace with the address that deployed the contract
private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"  # Private key for signing transactions

# Load contract ABI
import json
with open("../artifacts/contracts/Lock.sol/Lock.json") as f:  # Replace with your ABI file
    contract_json = json.load(f)
    contract_abi = contract_json['abi']

# Instantiate contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

contract_balance = w3.eth.get_balance(contract_address)
print(f"Contract Balance Before: {w3.from_wei(contract_balance, 'ether')} ETH")