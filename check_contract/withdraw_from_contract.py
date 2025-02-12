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
contract_address = w3.to_checksum_address("0x5FbDB2315678afecb367f032d93F642f64180aa3")
contract = w3.eth.contract(address=contract_address,abi=contract_abi)

txn = contract.functions.withdraw().build_transaction({
    'nonce': w3.eth.get_transaction_count(owner_address),
    'gas': 200000,
    'gasPrice': w3.to_wei("10","gwei"),
    'from': owner_address,
})

sign_txn = w3.eth.account.sign_transaction(txn, private_key)

tx_hash = w3.eth.send_raw_transaction(sign_txn.raw_transaction)
reciept = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction is successful {reciept.transactionHash.hex()}")

print(f"Balance of contract is {w3.eth.get_balance(contract_address)}")

