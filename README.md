# bedrock
bedrockLambdas

This repository contains some general examples of how to generate code with bedrock or images in AWS

Depending of lambda is required to include latest boto3 version in lambdas.
#create a dir for a layer 
mkdir boto3_layer
cd boto3_layer
#create python dir
mkdir python
#create environment 
python3 -m venv venv

#active environment 
source venv/bin/activate

#Install the lastest boto3 into the python directory 
pip install boto3 -t ./python

#Deactivate the virtual environment 
deactivate

#Zip the package
zip -r layer.zip ./python 

#Optionally, remove the virtual environment after packaging 
rm -r venv


API Gateway is used to be the trigger of these lambdas. 

To have at API Gateway: 
  POST/ 
  Integration by lambda_function

Example call for code_gen : 
{
"key":"python",
"message":"",
"extension":"py"
}


---For Model Evaluation examples--- 

1. Go to Bedrock in AWS
2. Go to Assessment & deployment
3. Go to Model Evaluation
4. Create model evaluation
5. set a name and description
6. select a model in model(s) selector choose the one that you want for my case Anthropic
7. choose text type on: general text generation, text summarization, question and answer, text classification. for lambda example text generation on anthropic one
8. Metrics and databases 
9. Use your own prompt dataset and select s3, format involved is important . Real Toxicity data set or BOLD(additional pay)
10. select metric
11. select TREX
12. use or not robustnest be sure what you are using as model.
13. create bucket
14. and then create a folder results in evaluation sets.
15. IAM selection, be carefully on permisisons. 
