"""
From the below JSON Object print value for the key “name” (highlighted in blue).
highlighted in blue:"name":"Checklist_Ericsson_PKC_INM_CGNAT.txt"
"""
import json
def read_json_obj(j_obj):
    
    j_obj = json.loads(j_obj)
    my_vals=j_obj.values()
    return(j_obj['content'][0]['attachment']['name'])

json_obj='{"content":[{"attachment":{"href":"cid:63f5e4909ca9205450a40030","len":4,"name":"Checklist_Ericsson_PKC_INM_CGNAT.txt","type":"text/plain","xmime:contentType":"text/plain"}},{"attachment":{"href":"cid:642d4b2aceab0054508de410","len":10338,"name":"dump.csv","type":"application/octet-stream","xmime:contentType":"application/octet-stream"}}]}'
read_json_obj(json_obj)
