import json
import boto3
import base64
import datetime

#Create client with Bedrock and s3 Services - Link
bedrock= boto3.client('bedrock-runtime')
s3=boto3.client('s3')

def lambda_handler(event, context):
    #1. using input variables
    prompt=event['prompt']
    print(prompt)
    #2. Create syntax request
    response= bedrock.invoke_model(contentType='application/json', accept='application/json', modelId='stability.stable-diffusion-xl-v0',
          body=json.dumps({"text_prompts":[{"text":prompt}],"cfg_scale":10, "steps":30,"seed":0}))
    #3.retrive from response, convert streaming body to bytes object 
    reponse_bytes=json.loads(response['body'].read())
    print(reponse_bytes)
    #4.Retrive data with artifact key, Import Base 64, Decode
    response_bytes_64=response_bytes['artifacts'][0]['base64']
    response_image=base64.b64decode(response_bytes_64)
    print(response_image)
    #5. File to s3 include date 
    image_name='image'+datetime.datetime.today().strftime('%Y-%M-%D-%H-%m-%S')

    reponse_s3=s3.putobject('imagePrompt',
      Bucket=''MyBucketTest',
      Body='response_image,
      Key=image_name)
    #6. Generate Pre-signed URL
    download_url=s3.generate_presigned_url('get_object',Params={'Bucket':'MyBucketTest','Key'=image_name}, ExpiresIn=3600)
    print(download_url)
    return{
      'statusCode':200,
      'body':download_url
    }
