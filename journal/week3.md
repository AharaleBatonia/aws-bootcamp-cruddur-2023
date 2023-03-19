# Week 3 — Decentralized Authentication
----------------------------
### Personal remarks: 
1. I am bearly managing to follow along and understand all the material and i am actually having doubts if i am doing well or maybe i am out off my league? 
2. I am struggeling with an error [error = no crudds in the home feed - on port 3000] that started to show up after the implementation of AWS Amplify. in the end of this document i will give more details and screenshots of the things i tried to do firstly to pin point the origin and secondly to resolve i, but unfourtentally without a success. 
3. I am a bit bhind but doing my best according to my real life circemstances. 
4. Thanks for having me :). 
----------------------------


## Setup Cognito User Pool

### create user pool 
1. creating user-pool in AWS Cognito\

![1. creating user-pool in AWS Cognito](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/1.%20creating%20user-pool%20in%20AWS%20Cognito.png)

### Install AWS Amplify
2. Install AWS Amplify

![2. Install AWS Amplify](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/2.%20Install%20AWS%20Amplify.png)

### Replace auth by cookies with Amplify, in files:
1. app.js 
2. docker-compose.yml
3. homeFeedPage.js
4. profileInfo.js
5. desktopSidebar.js

I group the following elements as 1 process, up to UI improvment & CSS global VAR implementation.

## Implement Custom Signin Page
## Implement Custom Signup Page
## Implement Custom Confirmation Page
## Implement Custom Recovery Page
## Verify JWT token server side
## Watch about different approaches to verifying JWTs

3. cognito user state force to change password
![3. cognito user state force to change password](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/3.%20cognito%20user%20state%20force%20to%20change%20password.png)
4. cognito user confirmed and enabled
![4. cognito user confirmed and enabled](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/4.%20cognito%20user%20confirmed%20and%20enabled.png)
5. User attributes
![5. User attributes](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/5.%20User%20attributes.png)
6. Signed in to cruddur with my user
![6. Signed in to cruddur with my user](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/6.%20Signed%20in%20to%20cruddur%20with%20my%20user.png)
7. Sign out from cruddur
![7. Sign out from cruddur](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/7.%20Sign%20out%20from%20cruddur.png)
9. your password has beed succesfully reset
![9. your password has beed succesfully reset](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/9.%20your%20password%20has%20beed%20succesfully%20reset.png)
8. Getting verification code by email
![8. Getting verification code by email](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/8.%20Getting%20verification%20code%20by%20email.png)


## Implementing UI Improvments 

10. my implementation - global var CSS
![10. my implementation - global var CSS](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/10.%20my%20implementation%20-%20global%20var%20CSS.png)
11. the result of UI improvments
![11. the result of UI improvments](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/11.%20the%20result%20of%20UI%20improvments.png)


## Error = I am struggeling with an error [error = no crudds in the home feed - on port 3000] 
The started to show up after the implementation of AWS Amplify on the server side. 

### the broblem
While i can see some post / crudds in some pages, my home page shows no crudds. 
this condition is true when signed in and when sined out. 


1. In the begining i tried to identify the origin of the error by comparing all the files i edited since the last time that my home feed showed correctly. this approch didn't yield solution. 
2. I tracked the date of the last time i saw the home feed correctlly in my notes and i dentified the problematic GitHub commit. 

When i run the Gitpod codespace with the commit bbe6769995 the home feed shows correclly. but when running the commit f75e3649f7 the home feed shows broken with no crudds. 
16. GitHub commit - Source of error Home Feed.png…
![16. GitHub commit - Source of error Home Feed.png…](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/16.%20GitHub%20commit%20-%20Source%20of%20error%20Home%20Feed.png)
the changes amde in this commit are shown in the screen shot bellow. I compared the content of my HomeFeedPage.js file to the relevant file of Andrew and it is matching. 
17. adding Headers to HomeFeedPage
![17. adding Headers to HomeFeedPage](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/17.%20adding%20Headers%20to%20HomeFeedPage.png)

14. home feed signed in
![14. home feed signed in.png…](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/14.%20home%20feed%20signed%20in.png)
15. Home feed signed out
![15. Home feed signed out.png…](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/15.%20Home%20feed%20signed%20out.png)
12. other pages with crudds nr.1
![12. other pages with crudds nr.1.png…](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/12.%20other%20pages%20with%20crudds%20nr.1.png)
13. other pages with crudds nr.2
![13. other pages with crudds nr.2.png…](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/13.%20other%20pages%20with%20crudds%20nr.2.png)

here bellow i am attaching the relevant logs:
1. backend logs 
2. backend env 
3. frontend logs [in the end of the log i get 3 errors which are the same error repeated 3 times on 2 files which are confirmationpage and recoverpage = 'setCognitoErrors' is not defined  no-undef. i looked int he repo of ansrew and those lines are correct.]
4. frontend env 
5. inspect element/console of home feed before and after refresh 

file with the relevant logs
[file with the relevant logs](https://github.com/AharaleBatonia/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Week%203%20%E2%80%94%20Decentralized%20Authentication/relevant%20logs%20for%20home%20feed%20error.pdf)

Next step - I took the time [many hours] to learn by trying to solve it myself but i am stuck. Please help me by suggeting me a valid next step with the purpose to unstuck me. 

Many thanks! 

