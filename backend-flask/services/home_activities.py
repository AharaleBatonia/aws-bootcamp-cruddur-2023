from datetime import datetime, timedelta, timezone

# 1 of 2 ... as the home interface is hard coded 
# and it is not going to a real database … 
# in order to see spans with multiple spans / calls 
# we will need to hard code them as well 

from opentelemetry import trace

# adding AWS CloudWatch 
import logging
# andrew took out the above line!

tracer = trace.get_tracer("home_activities")

class HomeActivities:
  def run():
    
    # adding AWS CloudWatch 
    # LOGGER.info("debug 6 - Hello Cloudwatch! from  /api/activities/home")
    LOGGER.info("debug 8 - Hello Cloudwatch! from  /api/activities/home")
    logger.info("debug 4 - HomeActivities")
    # additional line from the week2.md # added also in app.py 
    LOGGER.info("debug 5 - Hello Cloudwatch! from  /api/activities/home")
    logger.info("debug 7 - HomeActivities")

# 2 of 2 as the home interface is hard coded ... see aboove ... 
    with tracer.start_as_current_span("home_activities"):
      span = trace.get_current_span()
      
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      results = [{
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Andrew Brown',
        'message': 'Cloud is fun! L&H',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 1,
        'reposts_count': 0,
        'replies': [{
          'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
          'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
          'handle':  'Worf',
          'message': 'This post has no honor!',
          'likes_count': 0,
          'replies_count': 0,
          'reposts_count': 0,
          'created_at': (now - timedelta(days=2)).isoformat()
        }],
      },
      {
        'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
        'handle':  'Worf',
        'message': 'I am out of prune juice',
        'created_at': (now - timedelta(days=7)).isoformat(),
        'expires_at': (now + timedelta(days=9)).isoformat(),
        'likes': 0,
        'replies': []
      },
      {
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Garek',
        'message': 'My dear doctor, I am just simple tailor',
        'created_at': (now - timedelta(hours=1)).isoformat(),
        'expires_at': (now + timedelta(hours=12)).isoformat(),
        'likes': 0,
        'replies': []
      }
      ]
      span.set_attribute("app.result_length", len(results))
      return results
