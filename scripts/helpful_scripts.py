from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3


DECIMALS = 8
STARTING_PRICE = 200000000
LOCAL_BLOCKCHAIN_DEVELOPMENT = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_DEVELOPMENT
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        return accounts[0]
    else:
        return accounts.load("insert name here")


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mock")
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from": get_account()}
        )
        print("Mock deployed")
