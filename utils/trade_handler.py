from typing import Any, Dict
from flask import jsonify
from dexterity_sdk import SDKContext, OrderFillEvent
from utils.dexterity_context.py import get_dexterity_context
import json
import requests
from config import TRADING_API_URL

ctx = get_dexterity_context()

def handle_transaction(tr: Dict[str, Any]):
    events = ctx.parse_events_from_logs(tr.get("meta", {}).get("logMessages", []))
    fill_events = [event for event in events if isinstance(event, OrderFillEvent)]

    if fill_events:
        parsed_trades = [event_to_trade_data(tr, event) for event in fill_events]
        try:
            for trade in parsed_trades:
                process_trade(trade)
            print(f"Sent {len(parsed_trades)} trade events.")
        except Exception as e:
            print(f"Failed to send fill events due to error: {e}")
    else:
        print("No fill events found in transaction.")

def event_to_trade_data(tr: Dict[str, Any], event: OrderFillEvent):
    return {
        "product": event.product,
        "taker_side": event.taker_side,
        "quote_size": event.quote_size,
        "base_size": event.base_size,
        "maker": event.maker,
        "taker": event.taker,
        "price": event.price
    }

def process_trade(trade):
    url = f"{TRADING_API_URL}/process-trade"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(trade)
    try:
        response = requests.post(url, headers=headers, data=data)
        print("Status Code:", response.status_code)
        print("Response:", response.json())
    except Exception as e:
        print(f"An error occurred: {e}")
