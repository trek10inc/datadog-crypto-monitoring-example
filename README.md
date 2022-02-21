## This is a bare bones readme to accompany blog: 

* the repo has three parts
    *  lambda code: this is where the code if you wanted to copy/paste into the lambda console. Besides the copy / paste you will need to set the lambda cron schedule, configure the datadog layer (which includes creating an env var)
    *  datadog dashboard: this is a json file that can be imported via Datadog's dashboard import via json functionality
    *  datadog monitors: this is a collection of json files that can be imported via Datadog's monitor create via json functionality

* to get the lambda up + running + pushing metrics to datadog you will need to do the following steps:
    *  create a lambda function using python 3.8 in the console, named what you want,  x86_64 
    *  paste code from lambda_function.py
    *  in function overview pane hit add layer → arn:aws:lambda:<<your_region>>:464622532012:layer:Datadog-Python38:50
    *  in the configuration tab select `Environment variables` → add env variable in console named DD_API_KEY with an API key found at https://app.datadoghq.com/organization-settings/api-keys 
    *  in function overview pane hit `Add trigger` → choose `EventBridge (Cloud Watch Events) →  schedule expression → use `cron(0,10,20,30,40,50 * ? * * *)` as the expression
    *  hit deploy

  
  
This was written by James Bowyer in helps of helping out fellow LINK/Datadog/AWS enthusiasts - if you have any questions about the setup please reach out via: jbowyer@trek10.com / https://www.linkedin.com/in/james-bowyer-697149a2/ / carrier pigeon ... invest at your own risk, not a finacial advisor, etc 