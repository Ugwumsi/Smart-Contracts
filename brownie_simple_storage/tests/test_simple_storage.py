from brownie import SimpleStorage, accounts, network

def test_deploy():
    account = get_account()

    #Deploy SimpleStorage contract to the Blockchain
    deployed_contract = SimpleStorage.deploy({'from':account})

    starting_value = deployed_contract.retrieve()
    expected_value = 5

    #Make an assertion.
    assert starting_value == expected_value

def get_account():
    if (network.show_active()) == 'development':
        return accounts[0]
    else:
        return accounts.add(['wallets']['from_key'])


def updating_stor_value():
    account = accounts.load('ugwumsi')

    #Deploy the contract again
    deployed_contract = SimpleStorage.deploy({'from':account})

    #Update the value to 300, Mutherfucker
    
    expected_value = 300
    deployed_contract.store(expected_value, {'from':account})

    #Make an assertion.
    assert expected_value == deployed_contract.retrieve()

    