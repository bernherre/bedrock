# bedrock
bedrockLambdas

This repository contains some general examples of how to generate code with bedrock or images in AWS

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

