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
	json_data_input='salePrice'

	q_url='http://api.walmartlabs.com/v1/items/'+item_id+'?format=json&apiKey=<CHANGETOAPIKEY>' 
	response=requests.get(q_url) 
	json_data = json.loads(response.text)
	return (json_data["salePrice"])
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
