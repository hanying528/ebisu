
## Dev Setup

```bash
# clone the repo
git clone https://github.com/hanying528/ebisu.git

# create a py39 conda environment
conda create -n ebisu python=3.9
conda activate ebisu

# pip install backend in editable mode
cd src/backend
pip install -e .
```

## Database Setup

```bash
# create a sqlite database with necessary tables
cd src/backend/data
python create_db.py
```