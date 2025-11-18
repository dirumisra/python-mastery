# Environment Setup for GEN_AI_Project

This document explains how to set up and manage the Python environment for this project using Conda, and how to handle Git version control.

----
# 1. Navigate to Desktop and create project folder
    cd ~/Desktop                       # Go to Desktop
    mkdir -p ROADMAP_GEN_AI            # Create project folder if it doesn't exist
    cd ROADMAP_GEN_AI                  # Enter project folder

# 2. Create isolated conda environment inside project
    conda create -p ./env python=3.10 -y  # Create conda env in ./env with Python 3.10 (-y skips confirmation prompt)

# 3. Activate the environment
    conda activate ./env               # Activate newly created environment

# 4. Add environment folder to .gitignore to prevent committing env files
    echo "env/" >> .gitignore         # Append 'env/' folder to .gitignore

# 5. Export current environment packages to environment.yml
    conda env export > environment.yml  # Save dependencies for sharing/recreating

# 6. Initialize Git repository locally
    git init                         # Start a new Git repository in this folder

# 7. Stage all files for the first commit
    git add .                        # Stage all files for commit

# 8. Commit files with a message
    git commit -m "Initial setup with isolated environment"  # Commit with descriptive message

# 9. Link your local repo to GitHub remote repository
# NOTE: Step 9 assumes you already created an empty GitHub repository through GitHub’s website.
#       Replace <your-username> and <repo-name> with your GitHub username and repository name.
    git remote add origin https://github.com/<your-username>/<repo-name>.git

# 10. Push the initial commit to GitHub main branch
    git push -u origin main          # Push commits and set upstream to origin/main


# Summary of Important Commands

| Command                              | Description                          |
|------------------------------------|------------------------------------|
| `conda create -p ./env python=3.12` | Create isolated conda environment   |
| `conda activate ./env`              | Activate the environment             |
| `echo "env/" >> .gitignore`         | Ignore environment folder in Git    |
| `conda env export > environment.yml` | Export environment packages to YAML |
| `git init`                         | Initialize local Git repo            |
| `git add .`                        | Stage all files for commit           |
| `git commit -m "message"`          | Commit staged files                  |
| `git remote add origin <url>`       | Link to remote GitHub repo           |
| `git push -u origin main`           | Push code to GitHub                  |

-----------------------------------------------------------------------------------------