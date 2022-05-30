def lambda_handler(event, context):
   print(f"event:{event}")
   print(f"context:{context}")
   message = 'Hello {} !'.format(event['key1'])

   return {
       'message' : message
   }
