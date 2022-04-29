from brownie import accounts, config, SimpleStorage, network
#import  os

def deploy_simple_contract():
    #account = accounts[0]
    #print(account)
    account = get_account()
    print('Deploying the contract...')
    my_simple_storage = SimpleStorage.deploy({'from':account})
    print('Deployed!!')

    print('Retrieveing Value...')
    stored_value = my_simple_storage.retrieve()
    print('Retrieved!!')
    print(stored_value)

    print('Updating the Value by making a state change...')
    transaction = my_simple_storage.store(25)
    transaction.wait(1)

    print('Successful State Change!!, Value now updated!!')
    new_stored_valuue = my_simple_storage.retrieve()
    print(new_stored_valuue)

    
    #account = accounts.load('ugwumsi')
    #account = accounts.add(os.getenv)
    #print(account)

def get_account():
    if (network.show_active() == 'deployment'):
        return accounts[0]
    else: 
        return accounts.add(config['wallets']['from_key'])

def main():
    deploy_simple_contract()