import boto3
import botocore
import time
import base64

def lambda_habler(event, context):

  event=json.loads(event['body'])
  message=event['message']
  bedrock = boto3.client("bedrock-runtime", region_name=region, config= botocore.config.Config(read_timeout=300, retries={'max_attempts':2}))
  s3=boto3.client('s3')

  body={
    "text_prompts":[{f"text":message}]
    "cf_scale":10,
    "seed":0,
    "steps":50, ##more than 50 is premium image, more tokens included
  }

  reponse = bedrock.invoke_model(body=json.dumps(body), modelId="stability.stable-diffusion-xl-v0",contentType="application/json", accept= "application/json")
  reponse_body=json.loads(response.get("body").read())
  base_64_img_str = reponse_body["artifacts"][0].get("base64")
  image= base64.decodedbytes(base_64_img_str,"utf-8")

  bucket_name = "images-bucket"
  current_time = time.strftime('%Y%M%D-%H%M%S')
  s3_key=f"output-images/{current_time}.png"

  s3.put_object(Bucket= bucket_name, Key= s3_key, Body = image, ContentType='image/png')
  if (image is not null or image <> None ): 
    return{
      'statusCode':200,
      'body': json.dumps('Image saved')
    }
  else:
      return{
      'statusCode':400,
      'body': json.dumps('No Image')
    }
