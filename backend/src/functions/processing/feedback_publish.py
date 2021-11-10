import json
import time
import boto3
import os
from botocore.exceptions import ClientError
import uuid
import urllib


def lambda_handler(event, context):
    print("FEEDBACK PUBLISH")
    print(json.dumps(event))
    #if "file" in event:
    #    s3 = boto3.client('s3')
    #    uuidv4 = str(uuid.uuid4())
    #    try:
    #        response = s3.generate_presigned_post(os.environ["FEEDBACK_BUCKET"], uuidv4 + "_" + event["file"],
    #                                              ExpiresIn=120)
    #    except ClientError as e:
    ##        print(str(e))
    #        return json.dumps({"status": "err", "msg": "could not get signed url"})
    #
    #    return json.dumps(response)

    #elif "Records" in event:
    #    filename = urllib.unquote_plus(event["Records"][0]["s3"]["object"]["key"])
    #    print(filename)
    #    os.system("touch /tmp/{} /tmp/{}.txt".format(filename, filename))

    #elif "body" in event:
    #    return {
    #        "statusCode": 200,
    #        "headers": {
    #            "Access-Control-Allow-Origin" : "*"
    #        },
    #        "body": json.dumps({"status": "ok", "message": "Thank you."})
    #    }
    #else:
    s3 = boto3.client('s3')
    uuidv4 = str(uuid.uuid4())
    #s3.put_object(Body=more_binary_data, Bucket=os.environ["FEEDBACK_BUCKET"], Key=uuidv4)
    return {"status": "ok", "message": "Thank you."}