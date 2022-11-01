---

title: "Revert to an older version of a Conda environment"

---
From within the desired [[Virtual Environment]] run the commands below
```bash
conda list --revisions  # List the history of each change to the current environment 
conda install --revision 2  # Restore environment to a previous revision
```
This will introduce a **new** revision that rollsback to the installed revision. See [Sriram Jaju's Blog](https://www.shriramjaju.page/2018-05-30-2-minute-recipe-how-to-rollback-your-conda-environment/) and the [Conda Install Documentation](https://docs.conda.io/projects/conda/en/latest/commands/install.html) for more details.