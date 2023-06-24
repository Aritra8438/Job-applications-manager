# Job-applications-manager
# Our website is live. Access it here:


# Telegram Bot Documentation:
Due to the [serverless function size](https://vercel.com/docs/concepts/limits/overview#serverless-function-size) limit, we couldn't add all the functionalities to the API.
To compensate for that, We have created a [Telegram Bot](http://t.me/Resume_to_jobs_bot) that offers the following functionality:
- Send your resume/resume-URL to the bot, and the bot will respond with some available jobs based on your skill.

Neither the bot, nor we store your resumes by any means. Telegram generally keeps files (sent to the bot) available for one hour to the bot owners. After that, none can access your resume. 
To run this bot, we use [this](https://github.com/Aritra8438/Job-applications-manager/blob/main/Telegram%20bot/main.py) exact script. So, your resumes are instantly deleted once they are parsed. 

If you want to run/contribute to the Telegram bot, please get an API token from [BotFather](https://t.me/BotFather) and replace YOUR_API_KEY with your token.

If you are interested in Telegram bots, please refer to the [documentation](https://core.telegram.org/bots/api).

Also, don't forget to create a separate virtual environment to run the bot. The `requirements.txt` for the same will be available in `Telegram bot` folder.


# Local Development Setup:

Open the terminal at the destination folder:

```console
# Cloning the repository
git clone https://github.com/Aritra8438/Job-applications-manager.git

# Creating a virtual environment
pip install virtualenv

# linux users
virtualenv venv
source venv/bin/activate

# Windows users
python -m virtualenv venv
./venv\Scripts\activate

# Download packages
pip install -r requirements.txt 
```

If you face any problem installing psycopg2, go to this [link](https://stackoverflow.com/a/64179301/13665014).
Else, your virtual environment should be ready.

This project's database is hosted at [Render's PostgreSQL service](https://render.com/docs/databases). You should use Django's default database SQLite3 by overwriting database settings in the settings file.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}
```

Once you completed these steps, our backend is ready to serve. Open the terminal in the current directory:
 ```console
cd Job-applications-manager

python manage.py makemigrations

python manage.py migrate auth

python manage.py migrate --run-syncdb

python manage.py runserver
 ```
 Holla, you have run it on localhost:8000.
 
## Contribution Workflow:

Hello contributors, here is the contribution guideline you should follow:

- **First, create a fork of this repo. (Available at the top right corner of the repo)** 

- Go to the forked repository and **Clone the fork of your repo to the destination folder**.
```console
$ git clone https://github.com/YOUR_USERNAME/YOUR_FORK.git

```
- Navigate to the Project repository
```console
$ cd Job-applications-manager
```
- Add Upstream to your clone

```console
$ git remote -v
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
```
```console
$ git remote add upstream https://github.com/Aritra8438/Job-applications-manager.git
```

```console
$ git remote -v
> origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
> upstream  https://github.com/Aritra8438/Job-applications-manager.git (fetch)
> upstream  https://github.com/Aritra8438/Job-applications-manager.git (push)
```
- Before making any changes, sync your origin with upstream 

```console
$ git pull upstream main --rebase
``` 


- Make some changes to the project. After that, open a new branch and commit the changes.

```console
$ git checkout -b <new_branch>
$ git add .
$ git commit -m "Commit message"
$ git push origin <new branch>
``` 

- There will be a visible change in your repo, click on that and create a new pull request.

Thank you for your contribution.

## API Documentation:

Most of the APIs are available in [this](https://documenter.getpostman.com/view/27795030/2s93z5A5J6) postman documentation.

Alternatively, the Postman collection can be imported using `Vercel.postman_collection.json`.

Here is a screenshot of the same.

<img width="946" alt="image" src="https://github.com/Aritra8438/Job-applications-manager/assets/64671908/76afcd82-e597-46b4-be57-ddc1e7189efd">

## Unit Testing:
Currently, the essential APIs are unit-tested using ```pytest```.
If you are contributing to this repo, it's recommended that you run pytest before your pull request.

Open the project folder and run:
```console
pytest
```

Currently, most of the tests are linked in cascade by ```@pytest.fixture```. If you are adding a lot of testing to this project, we recommend creating a ```conftest.py``` and declaring all fixtures there.
