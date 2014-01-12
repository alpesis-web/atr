Jan 12 2014 | Git | Kelly Chan
# Git CodeSchool

## Level 1 New Init
to get help
```
git help
git help config
```
to create a user for all repos
```
git config --global user.name "XX"
git config --global user.email xxx@xx.com
git config --global color.ui true
```
to creat a new repo
```
mkdir store
cd store
git init
```
to check the status
```
git status
```
to add and commit files
```
git add index.html
git commit -m "new file index.html created"

git add readme.md LICENSE
git add --all
git commit -m "Add LICENSE and finish README."

git add *.txt
git add "*.css"
git add css/*.css
git add css/
```
to read the log file
```
git log
```

## Level 2 Staging and Remotes
to compare

```
git diff
git diff --staged
```
to unstage
```
git checkout (filename)
git checkout -- cats.html index.html
git reset ostrich.html
```
to stage and commit, modify and commit
```
git commit -a -m "file updated"
git commit --amend -m "xxxx"
```
undo the commit
```
git reset --soft HEAD^
git reset --hard HEAD^
git reset --hard HEAD^^
git reset HEAD LISENCE
```
to add a remote
```
git remote add origin https://github.com/XXX/xx.git
git remote -v
git push -u origin master
git pull
```
## Level 3 Cloning and Branching
to create and edit a branch
```
git branch cat
git checkout cat
git add cat.txt
git commit -m "xxxx"

git checkout master
ls

git merge cat

git checkout -b admin
git pull
git add readme.txt
git commit -m "xxxx"
git push
```

## Level 4


## Level 5
## Level 6
## Level 7


