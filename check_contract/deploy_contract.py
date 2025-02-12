from web3 import Web3
from os import getenv
import json

hardhat_url = getenv("HARDHAT_URL")
owner_address = getenv("OWNER_ADDR")
private_key = getenv("PRIV_KEY")

# Connect to Hardhat localhost node
w3 = Web3(Web3.HTTPProvider(hardhat_url))
print(f"Connected: {w3.is_connected()}")

with open("../artifacts/contracts/Lock.sol/Lock.json") as f:
    contract_json = json.load(f)

contract_abi = contract_json["abi"]
contract_bytecode = contract_json["bytecode"]

unlock_time = 1739370083

contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
transaction = contract.constructor(unlock_time).build_transaction({
    "from": owner_address,
    "gas": 2000000,
    "gasPrice": w3.to_wei("10", "gwei"),
    "nonce": w3.eth.get_transaction_count(owner_address),
    "value": w3.to_wei(1, "ether")
})

tx_hash = w3.eth.send_transaction(transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Contract deployed at: {tx_receipt.contractAddress}")