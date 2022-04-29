from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    my_simple_storage = file.read()
    #print(my_simple_storage)

#compile my solidity. The code below compiles my solidity code down to machine language (Low-Level Language)

my_compiler = compile_standard(
    {
        'language': 'Solidity',
        'sources': {'SimpleStorage.sol': {'content': my_simple_storage}},
        'settings': {
            'outputSelection': {
                '*': {'*': ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']}
            }
        },
    },
    solc_version = '0.6.0'
)
install_solc('0.6.0')
#print(my_compiler)

with open ('compiled_code.json','w') as file:
    json.dump(my_compiler,file)

#get Byte code just for fun
my_byte_code = my_compiler['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

#get abi just for fun
my_abi = my_compiler['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']

#Things needed for connecting to Goerli
#The Blockchain address.
w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/20ae38d62f2745bf8a43d99c4ab3f531'))
# Will need the Chain ID
network_ID = 5
#Will need my wallet Address
wallet_address = '0xE995b6994e5D9FEE2afF0548e51e646f983489D2'
#Private Key to sign the transaction
private_key = os.getenv('PRIVATE_KEY')

#print(private_key)

#We can create the contract from the contract metadata; the 'abi' & 'bytecode'
#More accurately, this is our compiled contract.
new_Simple_Contract = w3.eth.contract(abi=my_abi, bytecode=my_byte_code)

#Get the Latest Transaction Nonce
nonce = w3.eth.getTransactionCount(wallet_address)
#print(nonce)


#Build a Transaction
#Sign a Transaction
#Send a Transaction
print('Deploying Contract...')
transaction = new_Simple_Contract.constructor().buildTransaction({"gasPrice": w3.eth.gas_price,'chainId':network_ID,'from':wallet_address,'nonce':nonce})

signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

#Now, let's send this signed transaction 
txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
print('Deployed!')
#Working with Contracts

#We need the contract Address
newr_simple_storage = w3.eth.contract(address=txn_receipt.contractAddress, abi=my_abi)

print(newr_simple_storage.functions.retrieve().call())

print('Updating Contract...')
store_function = newr_simple_storage.functions.store(25).buildTransaction(
    {'gasPrice': w3.eth.gas_price,'chainId':network_ID,'from':wallet_address,'nonce':nonce +1}
)

#signing the Store transaction we just created.
signed_store_transaction = w3.eth.account.signTransaction(store_function,private_key)

#Sending the transaction we just created
send_signed_txn = w3.eth.send_raw_transaction(signed_store_transaction.rawTransaction)

the_receipt = w3.eth.wait_for_transaction_receipt(send_signed_txn)
print('Updated!')
#print the retrieve function again and se eif the vaue was updated.
print(newr_simple_storage.functions.retrieve().call())
#And the Contract ABI