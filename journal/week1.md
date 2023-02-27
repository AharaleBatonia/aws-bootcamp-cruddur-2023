# Week 1 — App Containerization

## week 1 - required homework assignments 

### Personal comment! 
#### Winning the Mentality Game!

I am feeling proud that I worked through the challenges of this assignment instead of listening to the voice that says "it is difficult" or "it is not for you, just quit!" I listened to and believed Andrew when he said that many have already quit. His encouragement to stay and work hard towards the finish line helped me succeed. It was challenging but very rewarding! Thanks again for this opportunity.

### Here are my assignments for week 1:

## Containerize Backend

### Run Python

I followed the instructions and after adding the /api/activities/home to the URL I got the json code as expected.

![Run Python - Backend & getting back json](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Run%20Python%20-%20Backend.png)

------------------

### additional details in the process - 
I did get some errors on the way that I managed to solve. so, if it is boring "you can jump to add dockerfile section" bellow.

#### - error 1 = 
Followed the instructions and I still get the 404 error msg 
![Followed the instructions and I still get the 404 error msg](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Followed%20the%20instructions%20and%20I%20still%20get%20the%20404%20error%20msg.png)
I was assuming that after adding the commands "export BACKEND_URL="*" it will work.

#### error 2 - 
Port 4567 is in use by another program 
and then when trying to run the cmd again ... I got a new error msg that we didn't see in none of the videos - Port 4567 is in use by another program 
![new error - Port 4567 is in use by another program](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/new%20error%20-%20Port%204567%20is%20in%20use%20by%20another%20program.png) 

#### resolving ... 
with the help of ChatGPT by asking how to kill a running port. as I still didn't know that shooting down the container will kill the port. ;).
I was trying to resolve it by following these steps:
1. running cmd - lsof -i :4567 in order to identify the PID that holds the port 
![identify the PID](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/identify%20the%20PID.png)
2. running the cmd kill <PID> in this case it was 1353 which worked. 
![kill 1353](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/kill%201353.png) 

and then after running the cmd again and added the /api/activities/home to the URL ... I did get to the page with the json code. 

---------------------

### Add Dockerfile

I successfully created the dockerfile `backend-flask/Dockerfile`

### Build Container

![running "docker images" after running the build command](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/running%20-%20docker%20images%20-%20after%20running%20the%20build%20command.png)

### Run Container

after running the docker run --rm -p 4567:4567 -it backend-flask command I got the expected … 404 error, because we are still missing the environment variables of: backend and frontend (the same way we got when we were running it in our local environment.)

![expected … 404 error after docker run cmd](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/expected%20%E2%80%A6%20404%20error%20after%20docker%20run%20cmd.png)

### adding the env vars for FE & BE 

this cmd didn't work - docker run --rm -p 4567:4567 -it -e FRONTEND_URL -e BACKEND_URL backend-flask 
![type error after adding env vars](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/type%20error%20after%20adging%20env%20vars%202.png)

while this cmd did work as expected 
![adding env vars cmd that did work as expected](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/adding%20env%20vars%20cmd%20that%20did%20work%20as%20expected.png)

### Run in background

Comment for the for the following commands - it is true that we did some of the following commands in the class but not in this order. so, I did run each of them to see what is the output but I am not sure what other steps I could take and to what purpose. 

I have got an error when running this cmd - docker container run --rm -p 4567:4567 -d backend-flask 
![failed- port is already allocated 2](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/failed-%20port%20is%20already%20allocated%202.png)

### Return the container id into an Env Var

I got an error when running this cmd - CONTAINER_ID=$(docker run --rm -p 4567:4567 -d backend-flask)
![failed- port is already allocated](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/failed-%20port%20is%20already%20allocated.png)


### Get Container Images or Running Container Ids
![Get Container Images or Running Container Ids](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Get%20Container%20Images%20or%20Running%20Container%20Ids.png)


### Send Curl to Test Server

shows the same content like it is showed in the home web page 
![Send Curl to Test Server](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Send%20Curl%20to%20Test%20Server.png)


### Check Container Logs
I have got the following errors 
![Check Container Logs](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Check%20Container%20Logs.png)

### Debugging adjacent containers with other containers
I have got the following error
![Debugging adjacent containers with other containers](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Debugging%20adjacent%20containers%20with%20other%20containers.png)

### busybosy cmd 
![busybosy cmd](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/busybosy%20cmd.png)


### Gain Access to a Container
it is the same as right clicking and choosing "attach shell" 
![Gain Access to a Container](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Gain%20Access%20to%20a%20Container.png)

### Delete an Image
I didn't feel safe to run this cmd

### Overriding Ports

we didn’t do overriding ports but we learned how to pass environment variables. I didn't feel safe to run this cmd
  

## Containerize Frontend
  
### Run NPM Install
  
![NPM install](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/NPM%20install.png)

### Run Container

![Run Container - frontend](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Run%20Container%20-%20frontend.png)


## Multiple Containers

![Multiple Containers](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Multiple%20Containers.png)

## Create a docker-compose file

I followed the instruction successfully. 
![result after docker compose [no errors]](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/result%20after%20docker%20compose%20%5Bno%20errors%5D.png)

## Frontend adding notifications activities 1. 

![works after Adding api_activities_notifications to the url](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/works%20after%20Adding%20api_activities_notifications%20to%20the%20url.png)

comment - at this stage I have got a name error (while you got assertion error) and after debugging I found that instead of copying the home element in order to create the notification element, I replaced it by mistake. after fixing all worked correctly. as you can see above. 
![name error frontend](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/NameError%20-%20Notifications%20backend.png)

## Frontend adding notifications activities 2. 

I have followed the instructions and got the wanted result. 

![Frontend adding notifications_activities](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Frontend%20adding%20notifications_activities.png)

comment - I don't have the intention of bragging but mere acknowledging. 
this time I changed all "home" occurrences to notifications before Andrew did the correction in the video which gives me the good feeling that I am progressing and starting to get it. 


## Adding DynamoDB Local and Postgres

in the process of adding DynamoDB & Postgres to the compose file, I have got an error that was different than the error Andrew got in the video and looked for the help of ChatGPT. the problem was indentation. 
putting `volumes` and `services` in the same level solved the issue. 

![error compose up after implementing DynamoDB & postgres](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/error%20compose%20up%20after%20implementing%20dynamodb%20%26%20postgres.png)

![Solved - compose up including postgres and dynamodb](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Solved%20-%20compose%20up%20including%20postgres%20and%20dynamodb.png)

![running postgres commands](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/running%20postgres%20commands.png)

comment & Question - in the video Andrew was avoiding to commit the file shared-local-instance.db that was created in the process of trying to solve the postgres issue. my question is why? (I also got the same file). 
Although we gained a new learning on how to create a file called .gitignore and to add files we want to ignore when committing. thanks for that :).
  
  
  





