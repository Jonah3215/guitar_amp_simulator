# guitar_amp_simulator

commands to run main (powershell)
cd C:\guitar_amp_simulator\guitar_amp_simulator 
venv\Scripts\activate
python -m amp_simulator.main


commands to push to branch (git bash)
git status
git add .
git commit -m "message"
git push -u origin branch-name

afterwards:
submit a pull request and merge changes to main


commands to fetch changes from main into (git bash)
git checkout main
git pull origin main


Assuming you're currently on your own branch and changes are merged into main, do this

Commit your work
      ↓
Update local main (git pull)
      ↓
Merge main into your branch
      ↓
Resolve conflicts if any
      ↓
Push your branch
      ↓
Merge via Pull Request

git status
git add .
git commit -m "Describe your changes"

git checkout main
git pull origin main

git checkout your-branch-name
git merge main
git push origin your-branch-name


this ensures both your branch and main is up to date with all changes
