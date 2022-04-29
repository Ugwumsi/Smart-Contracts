from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['hardhat','development','ganache','mainnet-fork','goerli']

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts.load('ugwumsi')
    if id:
        return accounts.load(id)
    return accounts.add(config['wallets']['from_key'])