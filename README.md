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

