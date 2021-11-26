import boto3
import os
import json
import string 
import secrets
import time
from sys import exit

# Configuration Area

# For all the stacks created with below description
description = 'Standard RDS cluster alarms'

# If template defination modifies locally 
# Note: currently argument passed with TemplateBody , in future TemplateURL should be better for big files
updatetemplate = True
newtemplatepath ='../rds-alarms.yml' # Localpath

# If we have to add or modify existing parameter, need to supply only changed or new parameter
updateparameter = False 
newparameter ={"IOThreshold":"1000"}

# If we want to safe with checking change set & proceed enable below
# In production always keep True
safepath = True
waittime = 5
###

def updatestack(stackname,templatebody,parameters,capabilites):
    client = boto3.client('cloudformation')
    try:
        response = client.update_stack(
                    StackName=stackname,
                    TemplateBody=templatebody,
                    Parameters=parameters,
                    Capabilities=capabilites,
                    UsePreviousTemplate=not updatetemplate
            )

        print("Susscessfully Completed for StackId:"+response['StackId'])
    except Exception as e:
        print("Error: "+str(e))

def createchangeset(stackname,templatebody,parameters,capabilites):
    client = boto3.client('cloudformation')
    try:
        response = client.create_change_set(
                StackName=stackname,
                TemplateBody=templatebody,
                Parameters=parameters,
                Capabilities=capabilites,
                UsePreviousTemplate=not updatetemplate,
                ChangeSetName='PeakChangeSet-'+''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(5))
        )
        Changesetname=response['Id']
        
        while True:
            response=client.describe_change_set(ChangeSetName=Changesetname)
            
            if response['Status'] == 'CREATE_COMPLETE':
                success=True
                break
            elif response['Status'] == 'FAILED':
                success=False
                break
            time.sleep(waittime)
            
        if success == True:
            print('Changes for the Changeset:'+Changesetname)
            print(response['Changes'])
            return Changesetname
        if success == False:
            print('Error on Changeset:'+Changesetname)
            print(response['StatusReason'])
            return None

    except Exception as e:
        print(str(e))
        return None

def executechangeset(Changesetname):
    client = boto3.client('cloudformation')
    try:
        response = client.execute_change_set(
                ChangeSetName=Changesetname
        )
        print('Change Set applied successfully!')
    except Exception as e:
        print("Error while applying changeset: "+str(e))

def gettemplate(stackname):
    client = boto3.client('cloudformation')
    try:
        response = client.get_template(
                StackName=stackname
        )
        return response['TemplateBody']
    except Exception as e:
        print("Error while applying changeset: "+str(e))
def handler():
    
    cfn = boto3.resource('cloudformation')
    print("Looking for template with description: "+description)
    stacks = [stack for stack in cfn.stacks.all() if stack.description == description]
    cf_template = 'Dummy template'

    # Only update Template    
    if updatetemplate==True:
        cf_template = open(newtemplatepath).read()
        print('This will apply / read new templatefile from path:'+newtemplatepath)
        
    if updateparameter==True:
        print('This will apply / read new parameters:'+str(newparameter))

    print('List of stacks to be worked upon:')
    for stack in stacks:
        print(stack.name)

    print('Change set will be created & wait for approval') if safepath else print('Directly update stacks ')
    
    answer = input('Is the information good to go?(Y/N):')
    if answer.lower() !='y':
        print('bye bye!!')
        exit() 

    for stack in stacks:
        finalparameter = stack.parameters

        # Only update Parameter
        if updateparameter ==True:
            for k,v in newparameter.items():
                found=0
                for item in finalparameter:
                    if item['ParameterKey']== k:
                        item['ParameterValue'] = v
                        found=1
                if found==0:
                    finalparameter.append({'ParameterKey':k,'ParameterValue':v})
        print('')
        print("updating template:"+stack.name)
        print("-------------------------------------")
        
        if updatetemplate==False:
            cf_template = gettemplate(stack.name)
        else:
            cf_template = open(newtemplatepath).read()
             
        if safepath == False:
            updatestack(stack.name,cf_template,finalparameter,['CAPABILITY_IAM'])
        else:
            response=createchangeset(stack.name,cf_template,finalparameter,['CAPABILITY_IAM'])
            if response:
                answer = input('Is the changeset good to apply?(Y/N):')
                if answer.lower() =='y':
                    executechangeset(response)
                else:
                    print('Skipping for the stack:'+stack.name)
            else:
                print('Something went wrong')
        
if __name__ == "__main__":
    handler()
