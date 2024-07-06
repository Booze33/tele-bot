import os

# Environment variables
API_KEY = os.getenv('API_KEY', 'Wla_oJ_aREztb0-f')
TRADING_API_URL = os.getenv('TRADING_API_URL', 'http://localhost:3000')

# Solana Devnet RPC URL
SOLANA_RPC_URL = f"https://devnet-rpc.shyft.to?api_key={API_KEY}"

# Market Product Group Key (Replace with actual key)
MARKET_PRODUCT_GROUP_KEY = "BRWNCEzQTm8kvEXHsVVY9jpb1VLbpv9B8mkF43nMLCtu"