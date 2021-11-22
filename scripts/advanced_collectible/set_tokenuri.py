from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPEN_SEA_URL, get_breed, get_account

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}

def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collections = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collections} token IDs")
    for token_id in range(number_of_collections):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id} ")
            set_tokenURI(token_id, advanced_collectible, dog_metadata_dic[breed])

def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    nft_contract.set_tokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(f"Awesome! you can now view your nft at{OPEN_SEA_URL.format(nft_contract.address, token_id)} ")
    print("Please wait up to 20 mins and hit the refresh metadata button")
