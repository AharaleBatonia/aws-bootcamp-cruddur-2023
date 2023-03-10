# Week 2 — Distributed Tracing

## sumuarry
I am attaching my summary of this week as context for the homework for this week. if it is boaring you can jump to Honeycomb bellow. 

    Summary week 2 

    Gitpod credits - 
    as I was low on credits I decided to do all file editing using the GitHub interface and only run gitpod when everything was ready to run compose up. 
    I think it worked well, but as you will see in my journal I did get some errors. 

    personal remark - 
    This week was a struggle for me. I suffered from debilitating neck pain and as a result, I am behind. Although I managed to learn new things and am more knowledgeable than last week, I still feel a bit like an impostor.

    + I managed to understand the concepts.
    + I managed to implement 95% successfully.
    + I have learned a lot about our APP & debugging errors. [but it took me a lot more time than desired]

    - I failed to see the outcome subsegments in xray 
    - I failed to see the outcome of implementing Rollbar 


    I will do whatever it takes to go ahead and close the gap and join the rest of the class. 

## Honeycomb 

Followed successfully the instructions:
1. exporting the env vars 
2. Check with env | grep HONEYCOMB that it got registered correctly. 
3. add opentelemetry to docker-compose
4. add instrumentation to app.py 
5. finding traces in the backend logs for spans 

![BE logs after implementing Honeycomb](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/BE%20logs%20after%20implementing%20Honeycomb.png)

6. getting spans & traces in Honeycomb

![getting spans & traces in Honeycomb](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/getting%20teaces%20in%20honeycomb%20%2B%20second%20span%20with%20mock%20data.png)

![traces honecomb](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/traces%20honeycomb.png)

7. running query [MAX, app.result_length exists, trace.trace_id]

![query honeycomb](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/query%20honeycomb.png)

![output for query honeycomb](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/output%20for%20query%20honeycomb.png)

![latency query honeycomb](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/latency%20query%20honeycomb.png)

8. saving queries for future use.

![saving queries for future use](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/saving%20queries%20for%20future%20use.png)

## Instrument AWS X-Ray

Followed successfully the instructions:
1. add X-RAY to requierments.txt 
2. add middleware recorder to app.py
3. add the xray.json file to the aws folder 
4. create a new group via cli 
5. add xray to docker-compose 
6. compose up and look for traces in cloudwatch / xray traces 

![X-RAY service map](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/X-RAY%20service%20map.png)

![X-RAY traces](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/X-RAY%20traces.png)

![X-RAY traces 2](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/X-RAY%20traces%202.png)

### adding subsegment to xray 
1. adding a segment to user_activities.py 
2. adding dict definition above 
3. add xray recorder to user_activities
4. adding capture functionality
5. hiding the xray implementation 

- I failed to see the outcome subsegments in xray, but I do have some buckets created in cloudtrail that I believe include the xray logs. but I am not sure and therefore I think I failed to see the outcome. 

![cloudtrail logs](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/cloudtrail%20logs.png)

##  implementing cloudwatch

Followed successfully the instructions:
1. add watchtower to requierments.txt and then run pip i.
2. add to app.py 
    a. I have got a few errors related to [logger/ Logger / LOGGRE] not being defined 
    
    ![looger is not defined](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/Logger_%20is%20not%20defined.png)
    
    ![LOGGER is not defined](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/LOGGER%20is%20not%20defined.png)
    
    ![looger is not defined but looks ok in the code](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/looger%20is%20not%20defined%20but%20looks%20ok%20in%20the%20code.png)    
    
    so I changed the logger to LOGGER but the error persisted.
    and then I followed some suggestions I saw on discord but none solved the logger error. 
        + I learned while debugging new cmd to find all occurrences of a string in my repo or folder = grep -r -i "logger". I had the idea to unify all occurrences of the logger to either low or high case but it didn't solve the error. 
        
     ![grep -r -i](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/grep%20-r%20-i.png)

    b. while I got the error "logger is not defined" I still could see logs in cloudwatch.
    
    ![logs in cloudwatch 1](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/logs%20in%20cloudwatch%201.png)
    
    ![logs in cloudwatch 2](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/logs%20in%20cloudwatch%202.png)

3. add to home_activities.py 
4. add to docker-compose 


##  Implementing Rollbar 

Followed the instructions:
1. add Rollbar to requierments.txt 
2. run pip I
3. run export and gp env with Rollbar token 
4. verify env vars with env | grep = works 
5. add Rollbar to app.py 
6. I get correctly to the rollbar/test web page 

![rollbar_test web page](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/rollbar_test%20web%20page.png)

7. when I did run compose up I got an error "pyrollbar: No access_token provided. Please configure by calling rollbar.init() with your access token." 
I followed a suggestion in discord and hard-coded my token in the rollbar.init(), and the error was solved.
8. but still I was not able to see any errors in rollbar. 
I tried different suggestions from discord but all in vain. 
    a. compose down and restart the container 
    b. start a new codespace 
9. I followed the instructions on forcing an error by deleting the return from the file with the hope that now I will see something, but no :(. 

I am sorry to share that I spend many hours over 3 days trying to be smart and solve it myself. 

The problems I think I have and things I tried while debugging:
1. when I did the setup ... after choosing the flask SDK I am getting stuck on the page with instructions on how to implement the SDK into FirstProject.
    a. I tried to create a new project. 
    b. I tried creating a new account. 
but nothing worked so I could jump this step like Andrew did in the class. 
2. when wanting to choose Environment, I don't see the production environment although it is set in the project settings. 

![no production environment](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/no%20production%20environment.png)

![enironment production is set in the project settings](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/enironment%20production%20is%20set%20in%20the%20project%20settings.png)

3. I managed to get to include all levels from the dashboard but it still didn't connect. 

![include all levels](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Distributed%20Tracing/include%20all%20levels.png)


### please suggest to me a next step for my failed implementation in X-RAY subsegments and Rollbar, especially if you believe it is essential. 

