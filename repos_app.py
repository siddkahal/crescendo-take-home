from flask import Flask, session, render_template, request, flash, redirect, url_for, make_response
import requests
import json
import sys
import os

app = Flask(__name__)

@app.get('/')
def index():
    CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
    auth_url = 'https://github.com/login/oauth/authorize?client_id={}'.format(CLIENT_ID)

    return render_template("home.html", url=auth_url)


@app.post('/activation-code')
def activation_code():
    OCTACAT = os.getenv('OCTACAT')
    entered_code = request.form.get('activation_code')
    repos_string = os.getenv('USER_REPOS')
    repos = json.loads(repos_string)

    if (OCTACAT == entered_code):
        return render_template("repos.html", repositories=repos)

    else:
        flash('CODES DO NOT MATCH!', 'error')
        return redirect(url_for('index'))



@app.get('/login/github/authorized')
def user_auth_callback():
    session_code = request.args.get('code')

    CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
    CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')

    result = requests.post('https://github.com/login/oauth/access_token', data={'client_id':CLIENT_ID, 'client_secret':CLIENT_SECRET, 'code':session_code}, headers={'Accept':'application/json'})

    result_json = result.json()

    # # extract the token and granted scopes
    access_token = result_json['access_token']

    user_result = requests.get('https://api.github.com/user', headers={'Authorization':'token {}'.format(access_token),'Accept':'application/json'})
    
    user_data = json.loads(user_result.text)
    

    user_repos_result = requests.get('https://api.github.com/user/repos', headers={'Authorization':'token {}'.format(access_token),'Accept':'application/json'})

    # Convert data to dict
    user_repo_data = json.loads(user_repos_result.text)
    repos = []
    
    for repo_data in user_repo_data:

        pull_count_result = requests.get('https://api.github.com/repos/{owner}/{repo}/pulls'.format(owner=user_data['login'], repo=repo_data['name']), headers={'Authorization':'token {}'.format(access_token),'Accept':'application/json'})
        pull_count_list = json.loads(pull_count_result.text)
        
        if (len(pull_count_list)):
            pull_count = pull_count_list[0]['number']
        else:
            pull_count = 0

        repo_data_object = {'data':repo_data, 'pull_count':pull_count}
        repos.append(repo_data_object)

    user_login = user_data['login']

    os.environ['USER_LOGIN'] = user_login
    session_flag = os.getenv('SESSION_FLAG')

    if (session_flag == 'true'):
        os.environ['SESSION_FLAG'] = 'false'
        return render_template("repos.html", repositories=repos)
    else:
        os.environ['SESSION_FLAG'] = 'true'
        os.environ['USER_REPOS'] = json.dumps(repos)
        return render_template('auth.html')

def main():
    os.environ['GITHUB_CLIENT_ID'] = sys.argv[1]
    os.environ['GITHUB_CLIENT_SECRET'] = sys.argv[2]
    os.environ['OCTACAT'] = sys.argv[3]
    os.environ['SESSION_FLAG'] = 'false'
    app.config['SECRET_KEY'] = 'shonysiddsecretkey'
    app.run(debug=True)


if __name__ == '__main__':
    main()