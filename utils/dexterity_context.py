from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.publickey import PublicKey
from dexterity_sdk import SDKContext
from config import SOLANA_RPC_URL, MARKET_PRODUCT_GROUP_KEY

def get_dexterity_context():
    client = Client(SOLANA_RPC_URL)
    payer = Keypair()
    market_product_group_key = PublicKey(MARKET_PRODUCT_GROUP_KEY)

    ctx = SDKContext.connect(
        client=client,
        market_product_group_key=market_product_group_key,
        payer=payer,
        raise_on_error=True
    )
    return ctx
