## WIP


## Version 0.1: start of assignment

* First code.

# Got an error when I tried to run "nox -s test" for a few reasons.

(1) my project names were inconsistant. I changed them all to "ci-exercice-jb8648".

(2)I needed my package to be able to use the /src/unc "path" instead of just src/ to account for the extra directory. I added this code:
[tool.hatch.build.targets.wheel]
packages = ["scr/unc"]

to the .toml file.

(3) I was using the wrong version of Python in my venv. I was using 3.8.8 and the code only works if I have >3.9. I also had to pip install pytest, unscertainties, and typing_extentions

for nox -s docs, I also had to pip install sphinx furo myst_parser.

Once I added all the necessary files and pushed to github, My code was failing my tests with the error "could not find pytest", I fixed a typo in my project.toml file that allowed the optional dependencies to be correctly installed.

fixed a typo in .pre-commit-config.yaml where I had an extra space"

manually fixed ruff issues delta C and an unused import TypeVar
