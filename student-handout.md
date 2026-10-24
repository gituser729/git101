# Git 101: Student Handout

## The idea in one minute

Git keeps a history of changes to a project. GitHub hosts Git projects online and provides tools for people to collaborate. In this workshop, use GitHub in a web browser and try a short Python exercise. No prior coding experience is needed.

## Key terms

| Term | Plain-language meaning |
| --- | --- |
| **Repository (repo)** | A project space containing files and their change history. |
| **Commit** | A named checkpoint recording a set of changes. |
| **Branch** | A separate line of work for developing a change without immediately changing the main version. |
| **Pull request (PR)** | A proposal to bring branch changes into another branch, with a place for review and discussion. |
| **Merge** | Combining approved changes into the destination branch. |
| **Merge conflict** | Overlapping changes that need to be reconciled before combining them. |

## Your hands-on checklist

Before editing, sign in to GitHub and open the repository link from your instructor. Follow the instructor's workflow: use your own branch if you have write access to the class repository, or make a fork and work in a branch there. Do not make exercise changes directly on the shared `main` branch. If you use a fork, make sure you are viewing your fork before creating your branch and file.

For the Python activity, you need a local copy of the script and access to Python 3. GitHub's browser editor can display or edit the script but cannot run it. Your instructor may provide a prepared environment. Otherwise, install [Python 3](https://www.python.org/downloads/), which includes IDLE on the standard Windows installer, and download the script from the repository. In IDLE, open the downloaded file with **File > Open**, run it with **Run > Run Module** (or F5), edit the sample values, save, and run it again. If using Visual Studio Code instead, install Python 3 and the Microsoft Python extension, open the downloaded file, and use **Run Python File**. Visual Studio Code is optional. The Python changes are local practice and do not need to be submitted unless your instructor asks.

### 1. Explore

- Open the class repository.
- Find `business-case/README.md`.
- Find the individual proposal format in `submissions/README.md`.
- Look at the commit history, if available.

### 2. Create and commit your recommendation

- In the repository you are contributing from (your fork or the class repository), use the branch selector to create a branch from `main`. Name it something like `recommendation-your-github-username`.
- In the repository or your fork, choose **Add file > Create new file**. Enter `submissions/your-github-username.md` as the file name, replacing the example with your GitHub username.
- Use the structure in `submissions/README.md` to recommend a target customer, state an assumption, and propose a low-cost launch test.
- In the commit form, choose to commit to your branch, not `main`, and use a short, meaningful description.

### 3. Try the Python market-test exercise

- Open `business-case/pilot_check.py` in GitHub, select **Raw** or **Download**, and save the file to your computer. Open that local copy in your Python environment.
- Run the script once and note the signup conversion rate and recommendation.
- Change the sample number of email signups or the target conversion rate, then run it again.
- Find the variables, calculation, and `if` statement. Discuss how changing an assumption changes the recommendation.

The numbers are made-up classroom examples, not real market research.

### 4. Open a pull request

- Open a pull request proposing your new submission file for the class repository's `main` branch. If you worked in a fork, set the class repository as the pull request's destination.
- Explain the business reason for your suggestions in the pull request.

### 5. Review a partner's proposal

- Open the pull request assigned by your instructor, read the proposed changes, and leave one constructive question or suggestion. You may need to sign in to comment.
- Discuss whether the proposal is clear and consistent with the case.

### 6. Observe the merge

- Follow the facilitator's instructions to merge an approved change.
- Look at the updated file and its history.

## Remember

**Edit → commit → propose → review → merge**

Git is the version-control system. GitHub is one platform for hosting Git projects and collaborating on them. Commits and pull requests make changes easier for a team to understand and discuss; they do not replace good judgment or business review.
