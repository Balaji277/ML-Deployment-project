import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "ML-Deployment-project"
AUTHOR_NAME = "Balaji277"
SRC_REPO = "Vision_Models"
AUTHOR_EMAIL = "balajipraneethboga@gmail.com"

setuptools.setup(
    name=f"{REPO_NAME}-{SRC_REPO}",
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="ML Deployment project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
