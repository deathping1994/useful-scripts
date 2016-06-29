import os
import subprocess
git_repo = raw_input("Enter git repo path relative to "+os.getcwd())
if git_repo[0] == '/':
	git_repo = git_repo[1:]
print git_repo
git_repo = os.path.join(os.getcwd(),git_repo)
print git_repo
branch_ref = raw_input("Enter branch ref (Default is origin/master):")
if branch_ref == '':
	branch_ref = 'origin/master'
command = " ".join(['cd',git_repo,'&&','git','diff','--stat',branch_ref])
output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
print output