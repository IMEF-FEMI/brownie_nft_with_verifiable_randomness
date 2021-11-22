 



from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, get_contract
from brownie import network
import pytest 
import time

def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for Integration testing")
    # Act
    advanced_collectible, creation_transaction = deploy_and_create()
   
    time.sleep(60)
    # assert
    assert advanced_collectible.tokenCounter() == 1



