# Week 1 — App Containerization

## week 1 - required homework assignments 


## Containerize Backend

### Run Python

I followed the instructions and after adding the /api/activities/home to the url i got the json code as expected.

![Run Python - Backend & getting back json](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Run%20Python%20-%20Backend.png)

------------------

additional details in the process - i did get some errors on the way that i manged to solve. so, if it is boring "you can jump to add dockerfile section" bellow.

#### - error 1 = Followed the instructions and I still get the 404 error msg 
![Followed the instructions and I still get the 404 error msg](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/Followed%20the%20instructions%20and%20I%20still%20get%20the%20404%20error%20msg.png)
i was assuming that after adding the commands "export BACKEND_URL="*" it will work.
#### error 2 - Port 4567 is in use by another program 
and than when trying to run the cmd again ... i got a new error msg that we didn't see in none of the videos - Port 4567 is in use by another program 
![new error - Port 4567 is in use by another program](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/new%20error%20-%20Port%204567%20is%20in%20use%20by%20another%20program.png) 

#### resolving with the help of ChatGPT by asking how to kill a running port. as i still didn't know that shoting down the container will kill the port. ;).
i was trying to resolve it by following theses steps:
1. running cmd - lsof -i :4567 in order to identify the PID that holds the port 
![identify the PID](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/identify%20the%20PID.png)
2. running the cmd kill <PID> in this case it was 1353 which worked. 
![kill 1353](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/kill%201353.png) 

and than after running the cmd again and added the /api/activities/home to the url ... i did get to the page with the json code. 

---------------------

### Add Dockerfile

i suuccesfully created the dockerfile `backend-flask/Dockerfile`

### Build Container

![running "docker images" after running the build command](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/running%20-%20docker%20images%20-%20after%20running%20the%20build%20command.png)

### Run Container

after running the docker run --rm -p 4567:4567 -it backend-flask command i got the expected … 404 error, because we are still missing the enviorment variables of:backend and forntend (the same way we got when we were running it in our local enviorment.)

![expected … 404 error after docker run cmd](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week1-containers/expected%20%E2%80%A6%20404%20error%20after%20docker%20run%20cmd.png)
