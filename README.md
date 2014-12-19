aiju_weixin
===========

aws server ip - ec2-54-164-22-233.compute-1.amazonaws.com // 54.164.22.233

git commands:

# retrieve & track remote master to local
git clone https://github.com/NotHere1/aiju_weixin.git

# retrieve & track remote branch to local
git fetch <remote> <rbranch>:<lbranch>  ## fetch remote branch -> local branch 
git checkout <lbranch>                  ## checkout newly created local branch

# check which branch
git branch

# move to branch
git checkout <branch>

# what's a 'remote'?
'remote is git's way of saying url to your repository (repo)'
git remote -v                           ## list all remote

# initialize a local repo
git init

# push to remote
'to push to remote repo you first have to push to your local git repo'
git add .                               ## stage all modified files to be push
git commit -m "<what has changed>"      ## push all modified file to local

'now you push to remote repo'
git push origin <branch>                ## update remote branch

# 
