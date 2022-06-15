# ML-Project
Start Machine Learning project.
Software and account Requirement.
[Github Account] (https://github.com)
[Heroku Account] (https://id.heroku.com/login)
[VS Code IDE] (https://code.visualstudio.com/docs/?dv=win)
[GIT cli] (https://git-scm.com/downloads)
[GIT Documentation] (https://git-scm.com/docs/gittutorial)


Creating conda environment.
'''
conda create -p venv python==3.7 -y
'''

Activating conda environment
'''
conda activate venv/

'''
Install flask

'''
pip install -r  requirements.txt
python -m pip install flask
'''

To add files to the git

STEP 1

'''
git add .

'''
OR 

'''
git add <file_name>

'''

Note: To ignore file or folder from git we can write name of file/folder  in .gitmore file


To check git status

'''

git status

'''

To check all version maintained by git 

'''
git log

'''

STEP 2

To create version/commit all changes by git

'''
git commit -m "message"    

'''
STEP 3

To send version/changes to git hub
'''
git push origin main

'''
To check remote url

'''
git remote -v
'''

To set up CI/CD pipeline we need 3 information.

1. HEROKU_EMAIL = adviteeya.shrav21@st.niituniversity.in
2. HEROKU_API_KEY = 7167f954-b519-4489-82a4-30fd719cf0e5
3. HEROKU_API_NAME = ml-regression-mbisde


BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname> .
'''
> Nore: Image name for the docker should be in lower case 
