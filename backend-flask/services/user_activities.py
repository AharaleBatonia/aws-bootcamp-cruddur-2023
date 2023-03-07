from datetime import datetime, timedelta, timezone

# adding XRAY subsegment +++ as a respons to an error 
from aws_xray_sdk.core import xray_recorder

class UserActivities:
  def run(user_handle):
    
    # adding XRAY subsegment 1. copy the line bellow, 2. changing < in_segment('segment_name') > with < in_segment('user_activities') > 
      # 3. indenting back to the same level everything bellow 1 tab to the right. 4. add subsegment 5. change ... in_segment('subsegment_name') to in_segment('mock-data')
      #    
    segment = xray_recorder.begin.segment('user_activities')
    # andrew took this above line out and in the end he added only subsegment in the end of the file. 
    
    model = {
      'errors': None,
      'data': None
    }

    now = datetime.now(timezone.utc).astimezone()    

    if user_handle == None or len(user_handle) < 1:
      model['errors'] = ['blank_user_handle']
    else:
      now = datetime.now()
      results = [{
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Andrew Brown',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=1)).isoformat(),
        'expires_at': (now + timedelta(days=31)).isoformat()
      }]
      model['data'] = results
      

    # adding XRAY subsegment
    subsegment = xray_recorder.begin_subsegment('mock-data')
      # adding XRAY subsegment +++ adding dict 
    dict = {
        "now": now.isoformat(),
        "results-size": len(model['data'])
    }
    # adding XRAY subsegment
    subsegment.put_metadata('key', dict, 'namespace')
    
    return model
