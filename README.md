# ML-Project

## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/docs/?dv=win)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


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
2. HEROKU_API_KEY = <>
3. HEROKU_API_NAME = ml-regression-mbisde


BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname> .
'''
> Nore: Image name for the docker should be in lower case 

To list docker images

'''
docker images
'''

RUN docker image 

'''
docker run -p  5000:5000 -e PORT=5000 62649b3cb8cb

'''
To check running containers 
'''
docker ps 
'''

To stop docker container
'''
docker stop <container_id>
'''

'''

python setup.py install 
'''

'''
pip install -r requirements.txt
'''

'''
pip install -e
'''

Install python kernel

```
pip install ipykernel

```

Install YAML 

```
pip install PyYAML
```

Install dill file

```
pip install dill 
```
Install matplotlib file

```
pip install matplotlib
```

Data drift :

When your data set stats gets changes it is called data drift.
Compare the stats of two data sets and if there is no difference there is 0 percent data drift. 
If two data set is not similar it has data drift. 


