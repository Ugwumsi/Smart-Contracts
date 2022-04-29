from brownie import SimpleCollectible
from scripts.helpful_scripts import get_account
import os

print(os.getenv("WEB3_INFURA_PROJECT_ID"))

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URI = "https://testnets.opensea.io/assets/{}/{}"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    txn = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    txn.wait(1)
    print(
        f"You can go and view your NFT at: {OPENSEA_URI.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    print("Please wait 20 minutes and hit the Refresh Metadata button")

