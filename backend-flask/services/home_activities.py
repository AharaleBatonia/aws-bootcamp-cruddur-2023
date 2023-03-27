from datetime import datetime, timedelta, timezone

# adding postgres connection 
from lib.db import db

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
  def run(cognito_user_id=None):

    # adding postgres connection 
    sql = db.template('activities','home')
    results = db.query_array_json(sql)
    
    # adding AWS CloudWatch 
    # LOGGER.info("debug 6 - Hello Cloudwatch! from  /api/activities/home")
    # LOGGER.info("debug 8 - Hello Cloudwatch! from  /api/activities/home")
    # Logger.info("debug 4 - HomeActivities")
    # additional line from the week2.md # added also in app.py 
    # LOGGER.info("debug 5 - Hello Cloudwatch! from  /api/activities/home")
    # logger.info("debug 7 - HomeActivities")

# 2 of 2 as the home interface is hard coded ... see aboove ... 
    with tracer.start_as_current_span("home_activities"):
      span = trace.get_current_span()
      
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      
      # adding postgres endpoint api call
      sql = """
      SELECT * FROM activities
      """
      
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
      return json[0]
    
      # forcing error for Rollbar activation test by hididng the line of return results and leaving just results and than undo this change back to return results
      return results
