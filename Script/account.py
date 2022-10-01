import json
import base64
from tkinter.messagebox import YES
from algosdk import account, mnemonic
from algosdk.v2client import algod
import time

def create_account(fund=True):
    # Change algod_token and algod_address to connect to  client
    algod_token = "2f3203f21e738a1de6110eba6984f9d03e5a95d7a577b34616854064cf2c0e7b"
    algod_address = "https://academy-algod.dev.aws.algodev.network/"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    # Generate new account 
    secret_key, my_address = account.generate_account()
    mmnemon = mnemonic.from_private_key(secret_key)
    print("My address: {}".format(my_address))

    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get("amount")) + "\n")

    if fund:
    
        print(
            "Created account: \n https://dispenser.testnet.aws.algodev.network/?account={}".format(
                my_address
            )
        )

        completed = ""
        while completed.lower() != "yes":
            completed = input("Type 'yes' once you funded the account: ")

        print("Fund transfer in process...")
        
        time.sleep(5)

        print("Fund transferred!")
        # Check your balance.
        account_info = algod_client.account_info(my_address)
        print(
            "Account balance: {} microAlgos".format(account_info.get("amount")) + "\n"
        )

    return mmnemon