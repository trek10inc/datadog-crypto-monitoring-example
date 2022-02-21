import json
import urllib3
http = urllib3.PoolManager()
from datadog_lambda.metric import lambda_metric
from datadog_lambda.wrapper import datadog_lambda_wrapper
 
 
@datadog_lambda_wrapper
def lambda_handler(event, context):
   r = http.request("GET", "https://api.kraken.com/0/public/Ticker?pair=LINKUSD")
   data=r.data.decode('UTF-8')
   data=json.loads(data)
   current_price=float(data["result"]["LINKUSD"]["c"][0])
   last_24_volume=float(data["result"]["LINKUSD"]["v"][1])
   lambda_metric(
       "chainlink.current_price",              # Metric name
       current_price,                          # Metric value
       tags=['ticker:LINK']                    # Associated tags
   )
   lambda_metric(
       "chainlink.last_24_volume",              # Metric name
       last_24_volume,                          # Metric value
       tags=['ticker:LINK']                    # Associated tags
   )
  
   r = http.request("GET", "https://api.kraken.com/0/public/Ticker?pair=BTCUSD")
   data=r.data.decode('UTF-8')
   data=json.loads(data)
   current_price=float(data["result"]["XXBTZUSD"]["c"][0])
   last_24_volume=float(data["result"]["XXBTZUSD"]["v"][1])
   lambda_metric(
       "bitcoin.current_price",              # Metric name
       current_price,                          # Metric value
       tags=['ticker:BTC']                    # Associated tags
   )
   lambda_metric(
       "bitcoin.last_24_volume",              # Metric name
       last_24_volume,                          # Metric value
       tags=['ticker:BTC']                    # Associated tags
   )
  
   return {
       'statusCode': 200,
       'body': json.dumps('Hello from Lambda!')
   }
