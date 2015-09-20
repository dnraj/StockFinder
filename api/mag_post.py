import web
import sys
import os, cgi
import requests 
import json
from pprint import pprint
urls = (
    '/', 'index'
)

class index: 
  def GET(self):
	#for arg in sys.argv:
	print "Content-Type: text/html\n"
	query =	 os.environ.get('QUERY_STRING')
	arguments = cgi.parse_qs(query) if query else {}
	item_id='41299768'
	json_data_input=arguments
#	json_data_input='stock'
	q_url='https://prod-mmx-01.magnet.com:5221/mmxmgmt/api/v1/topics/buyer2/publish' 
        headers = { 'X-mmx-app-id': '23giesorc33' ,'X-mmx-api-key': '855c5a64-ecf5-4a46-a7e4-1a5638c120c8' ,'Content-Type': 'application/json'}
        payload= {'content':'Currently Available for itemid 41299768','messageType':'normal','contentType':'text'}
	response=requests.post(q_url,data=json.dumps(payload),headers=headers) 
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
