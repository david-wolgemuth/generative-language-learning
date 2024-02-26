
install:
	# These updates include the creation of a
	# virtual environment using venv
	# and installation of dependencies within that environment.
	# This ensures better isolation and management of dependencies for your project.
    python3 -m venv venv
    . venv/bin/activate && pip install -r requirements.txt

jupyter:
    jupyter nbconvert --to notebook --execute $< --output jupyter.ipynb

run:
    . venv/bin/activate && python main.py

cd:
    cd /
