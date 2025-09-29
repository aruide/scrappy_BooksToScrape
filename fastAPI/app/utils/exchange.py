import os
from dotenv import load_dotenv
from pathlib import Path
import requests
import json
      
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class Exchange():
    
    exchange_url = os.getenv("EXCHANGE_URL")

    def __init__(self):
        try:
            response = requests.get(f"{self.exchange_url}/gbp.json")
            self.data = response.json()
        except:
            self.data = {
                "gbp": {
                    "eur": 1
                }
            }

    def exchange_livre_to_euro(self, amount: float):
        
        rate = self.data["gbp"]["eur"]
    
        return amount * rate

exchange = Exchange()