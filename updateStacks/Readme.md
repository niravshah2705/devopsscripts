Execute Script:

Step 1: Modify the variables in file
Step 2: install dependency
pip3 install -r requirements.txt
Step 3: Execute & respond to y/n questions
python3 updateStack.py

Demo Run:
Looking for template with description: Standard RDS cluster alarms
This will apply / read new templatefile from path:rds-alarms.yml

List of stacks to be worked upon:
SC-123459999999-pp-irqbo2s45ylbq
SC-123459999999-pp-sgfyz4mv7ih6y
SC-123459999999-pp-lqhnfwsvilir2
SC-123459999999-pp-3255bjqwp4bs2
SC-123459999999-pp-r2lgvj6nllelg
SC-123459999999-pp-zwbvb5d5rq4vw
SC-123459999999-pp-iir6wjhonjrok
Change set will be created & wait for approval
Is the information good to go?(Y/N):y

updating template:SC-123459999999-pp-irqbo2s45ylbq
-------------------------------------
Changes for the Changeset:arn:aws:cloudformation:eu-west-1:123459999999:changeSet/MyChangeSet-KQLBI/a689b838-90b3-435a-8538-b47b82fc7a5c
[{'Type': 'Resource', 'ResourceChange': {'Action': 'Modify', 'LogicalResourceId': 'ConnectionsAlarm', 'PhysicalResourceId': 'mydb1-database-alarms-Connections-Alarm', 'ResourceType': 'AWS::CloudWatch::Alarm', 'Replacement': 'False', 'Scope': ['Properties'], 'Details': [{'Target': {'Attribute': 'Properties', 'Name': 'Statistic', 'RequiresRecreation': 'Never'}, 'Evaluation': 'Static', 'ChangeSource': 'DirectModification'}]}}]
Is the changeset good to apply?(Y/N):y
Change Set applied successfully!

updating template:SC-123459999999-pp-sgfyz4mv7ih6y
-------------------------------------
Changes for the Changeset:arn:aws:cloudformation:eu-west-1:123459999999:changeSet/MyChangeSet-2DV6F/7a3a70d6-c77a-44b4-a7f0-47d686c2e8b9
[{'Type': 'Resource', 'ResourceChange': {'Action': 'Modify', 'LogicalResourceId': 'ConnectionsAlarm', 'PhysicalResourceId': 'mydb2-alarms-Connections-Alarm', 'ResourceType': 'AWS::CloudWatch::Alarm', 'Replacement': 'False', 'Scope': ['Properties'], 'Details': [{'Target': {'Attribute': 'Properties', 'Name': 'Statistic', 'RequiresRecreation': 'Never'}, 'Evaluation': 'Static', 'ChangeSource': 'DirectModification'}]}}]
Is the changeset good to apply?(Y/N):y
Change Set applied successfully!

updating template:SC-123459999999-pp-r2lgvj6nllelg
-------------------------------------
An error occurred (ValidationError) when calling the CreateChangeSet operation: Parameters: [RDSInstance] do not exist in the template
Something went wrong

updating template:SC-123459999999-pp-zwbvb5d5rq4vw
-------------------------------------
Changes for the Changeset:arn:aws:cloudformation:eu-west-1:123459999999:changeSet/MyChangeSet-EKAWY/88d331a5-db87-478e-bda4-95dc07011bda
[{'Type': 'Resource', 'ResourceChange': {'Action': 'Modify', 'LogicalResourceId': 'ConnectionsAlarm', 'PhysicalResourceId': 'mydb3-manager-database-alarms-Connections-Alarm', 'ResourceType': 'AWS::CloudWatch::Alarm', 'Replacement': 'False', 'Scope': ['Properties'], 'Details': [{'Target': {'Attribute': 'Properties', 'Name': 'Statistic', 'RequiresRecreation': 'Never'}, 'Evaluation': 'Static', 'ChangeSource': 'DirectModification'}]}}]
Is the changeset good to apply?(Y/N):y
Change Set applied successfully!

updating template:SC-123459999999-pp-iir6wjhonjrok
