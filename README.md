# Job-applications-manager

# Local Development Setup:

Open the terminal at the destination folder:

```bash
# cloning the repository
git clone https://github.com/Aritra8438/Job-applications-manager.git

# creating virtual environment
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

This project's database is hosted at [Render's PostgreSQL service](https://render.com/docs/databases). You should use django's default database SQLite3 by overwriting database settings at the settings file.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}
```

Once you successfully completed these steps, our backend is ready to serve. Open the terminal at the current directory:
 ```bash
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

- Go to the forked repository and **Clone your fork of your repo to the destination folder**.
```
$ git clone https://github.com/YOUR_USERNAME/YOUR_FORK.git

```
- Navigate to the Project repository
```
$ cd Job-applications-manager
```
- Add Upstream to your clone

```
$ git remote -v
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
```
```
$ git remote add upstream https://github.com/Aritra8438/Job-applications-manager.git
```

```
$ git remote -v
> origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
> upstream  https://github.com/Aritra8438/Job-applications-manager.git (fetch)
> upstream  https://github.com/Aritra8438/Job-applications-manager.git (push)
```
- Before making any changes, sync your origin with upstream 

```
$ git pull upstream main --rebase
``` 


- Make some changes to the project. After that, open a new branch and commit the changes.

```
$ git checkout -b <new_branch>
$ git add .
$ git commit -m "Commit message"
$ git push origin <new branch>
``` 

- There will be a visible change in your repo, click on that and create a new pull request.

Thank you for your contribution.



