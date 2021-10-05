# Crescendo Take Home Solution #

## Instructions: ##
1. When you are registering for the OAuth appliction on GitHub, ensure that the Homepage URL is 'http://127.0.0.1:5000'. And the Authorization callback URL is 'http://127.0.0.1:5000/login/github/authorized'
2. Navigate to the 'crescendo-take-home' directory
3. In the command line run the application through the following: 'python3 repos_app.py {clientID_value} {clientSecret_value} {ocatacat_value}'. The first 2 arguments are the clientID (GITHUB_CLIENT_ID) and clientSecret (GITHUB_CLIENT_SECRET), which were set up through GitHub. The ocatacat_value (OCTACAT) is the authentication code the user will need to enter when email is not activated. This value provided here will be used for comparison. 
4. Now you can go to the URL 'http://127.0.0.1:5000' in the browser and interact with the application.
5. To run the test file, navigate to the 'tests' directory and run 'python3 test_repos_app.py'
6. I only have standard Python libraries imported, so there should be no dependency issues. If required, pip install any that are missing.  

## TODO List: ##
1. Currently displaying the repository Owner, NOT the Organization. I had a hard time finding the API endpoint with the Organization.
2. Improve/refactor the session behavior and user information storage. There is the built in 'session' library for Flask. I tried to use that but did not get the desired behavior.
3. Add more unit tests around the callback functions and UI.
4. Look into 'flask_dance' and specifically 'make_github_blueprint'. This library makes it easier to work with the data returned form the GitHub endpoints.

## Screenshots: ##

<img width="1265" alt="HomePage" src="https://user-images.githubusercontent.com/19416227/135974812-cc53d906-348e-422c-a511-2af70437e319.png">

<img width="720" alt="AuthPage" src="https://user-images.githubusercontent.com/19416227/135974868-2ae14fa0-8098-4e7f-bd41-fe9141ea51f4.png">

<img width="1262" alt="ReposPage" src="https://user-images.githubusercontent.com/19416227/135974901-acdf24c9-408f-4188-b677-411ce6a2e47c.png">
