https://python-poetry.org/

Linux, MacOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -

PoewrSHELL
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

poetry init
poetry new name_project
poetry install    (аналог pip install -r requirements.txt)
poetry add name   (аналог pip install name)
poetry remove name
poetry update name
poetry show



curl -Ls https://astral.sh/uv/install.sh | sh