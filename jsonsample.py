import json

jsonString = '{"eventId": "7cb42296-2e24-491c-8aa8-bda6bb1b5c17",' \
             '"eventDate": "2019-05-07T17:07:45.316328",' \
             '"submissionId": "70fbb6b5-7fdf-4181-b09f-46270ea3aa74",' \
             '"submissionStatus": "CLEANED_UP_LANDING"}'

event = json.loads(jsonString)
print "eventId:", event["eventId"]
print "eventDate:", event["eventDate"]
print "submissionId:", event["submissionId"]
print "submissionStatus:", event["submissionStatus"]
