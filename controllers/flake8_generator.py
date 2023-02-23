import os


class FlakeControl:
    def control():
        #Fonction de creation du rapport flake8
        if os.name == "posix":
            os.system(
                "python -m flake8 .. --format=html --htmldir=flake-report --max-line-length=119")
        else:
            os.system(
                "python -m flake8 .. --format=html --htmldir=flake-report --max-line-length=119")
