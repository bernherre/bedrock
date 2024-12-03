import boto3
import botocore.config
import json
import time

def generate_code_using_bedrock(message:str, languge:str, extention:str) ->str:
  prompt_text = f'''Human: Write{language} for the following instructions: {message}.
  Assistant:
  '''
  body = {
      "prompt": prompt_text,
      "max_tokens_to_sample": 2048,
      "temperature": 0.1,
      "top_k":250,
      "top_p":0.2,
      "stop_sequence":["\n\nHuman:"]
  }
  try:
    bedrock=boto3.client("bedrock-runtime",region_name="region", config= botocore.config.Config(read_timeout=300, retries={'max_attempts':2}))
    response= bedrock.invoke_model(body=json.dumps(body), modelId="anthropic.claude-v2")
    response_content = response.get('body').read().decode('utf-8')
    response_data=json.loads(response_content)
    code= response_data["completion"].strip()
    return code
  except Exception as e:
    print("Error generating the code: {e}")
    return ""
def save_code_file(code_s3_bucket, code_s3_path,extention):
  s3=boto3.client('s3')
  try: 
    s3.put_object(Bucket = s3_bucket, Key= s3_ky, Body=code) 
    print("file saved")
   except Exception as e:
     print("Error saving the code: {e}")
def lambda_handler(event,context): 
  event = json.loads(event['body'])
  message = event['message']
  language= event['key']
  print(message, language)
  generated_code = generate_code_using_bedrock(message, language)
  if generated_code : 
    current_time = time.strftime('%Y%M%D-%H%M%S')
    s3_key= f'code-output/{current_time}.{extention}'
    s3_bucket="my_code_bucket"

    save_code_file(generated_code, s3_bucket, s3_key)
  else: 
    print("there was not code generated")
  return{
    'statusCode':200,
    'body':json.dumps('code generation completed')
  }
  }
  generate_code_using_bedrock
