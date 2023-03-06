from datetime import datetime, timedelta, timezone

# adding XRAY subsegment +++ as a respons to an error 
from aws_xray_sdk.core import xray_recorder

class UserActivities:
  def run(user_handle):
    
    # adding XRAY subsegment 1. copy the line bellow, 2. changing < in_segment('segment_name') > with < in_segment('home.activities') > 
      # 3. indenting everything bellow 1 tab to the right. 
      # 
    with xray_recorder.in_segment('home.activities') as segment:
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()
      
      # adding XRAY subsegment +++ adding dict 
      dict = {
          "now": now.isoformat()
      }
      # adding XRAY subsegment
      segment.put_metadata('key', dict, 'namespace')

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
      return model
