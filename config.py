# import os
# from dotenv import load_dotenv

# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         f'sqlite:///{os.path.join(basedir, "instance", "site.db")}'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     BOOTSTRAP_SERVE_LOCAL = True

import os
from pathlib import Path

# Get absolute path to instance folder
basedir = Path(__file__).parent
instance_path = basedir / 'instance'
instance_path.mkdir(exist_ok=True)  # Create instance folder if it doesn't exist

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{instance_path / "site.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False