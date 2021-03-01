import os


class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin'
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'Password123'
    UPLOAD_FOLDER = ('uploads')


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False

def get_uploaded_images():
    rootdir = os.getcwd()
    print (rootdir)

    for subdir,dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            print (os.path.join(subdir,file))
            dirs = subdir + os.sep + file

            if dirs.endswith(".jpg", "png"):
                print(dirs)

            