import requests
import json
from firebase import *

tt = main()
ss = str(tt[0]).split("'")
req_gtin = ss[1]
print(req_gtin)

resp = requests.get('https://productinformation.lab.atrify.com/items/_search?q='+req_gtin, headers={'apikey':'fd9653ad-6cf1-4ade-8524-d90a1c709432'})
f = open("test.json", mode='w', encoding='utf-8')
if resp.status_code != 200:
    # This means something went wrong.
    print(resp.status_code)
#for todo_item in
js = json.loads(resp.text)

#print(json.dumps(js, indent=4))
#f.write(json.dumps(js, indent=4))

#print(js[3]['tradeItem']['gtin']['_text'])
for i in range(len(js)):
    if(js[i]['tradeItem']['gtin']['_text'] == req_gtin ):
        print(js[i]['tradeItem']['informationProviderOfTradeItem']['partyName']['_text'])
f.close()
#    print('{} {}'.format(todo_item['id'], todo_item['summary']))
