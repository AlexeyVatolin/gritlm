"""
Note:
   VERSION needs to be formatted following the MAJOR.MINOR.PATCH convention
   (we need to follow this convention to be able to retrieve versioned scripts)
Inspired by: https://github.com/huggingface/datasets/blob/main/setup.py
To create the package for pypi.
0. Prerequisites:
   - Dependencies:
     - twine: "pip install twine"
     - wheel: "pip install wheel"
   - Create an account in (and join the 'datasets' project):
     - PyPI: https://pypi.org/
     - Test PyPI: https://test.pypi.org/
1. Change the version in:
   - gritlm/__init__.py
   - setup.py
2. Commit these changes: "git commit -m 'Release: VERSION'"
3. Add a tag in git to mark the release: "git tag VERSION -m 'Add tag VERSION for pypi'"
   Push the tag to remote: git push --tags origin main
4. Build both the sources and the wheel. Do not change anything in setup.py between
   creating the wheel and the source distribution (obviously).
   First, delete any "build" directory that may exist from previous builds.
   For the wheel, run: "python setup.py bdist_wheel" in the top level directory.
   (this will build a wheel for the python version you use to build it).
   For the sources, run: "python setup.py sdist"
   You should now have a /dist directory with both .whl and .tar.gz source versions.
5. OPTIONAL: Check that everything looks correct by uploading the package to the pypi test server:
   twine upload dist/* -r pypitest --repository-url=https://test.pypi.org/legacy/
   Check that you can install it in a virtualenv/notebook by running:
   pip install huggingface_hub fsspec aiohttp
   pip install -U tqdm
   pip install -i https://testpypi.python.org/pypi datasets
6. Upload the final version to actual pypi:
   twine upload dist/* -r pypi
7. Fill release notes in the tag in github once everything is looking hunky-dory.
8. Change the version in __init__.py and setup.py to X.X.X+1.dev0 (e.g. VERSION=1.18.3 -> 1.18.4.dev0).
   Then push the change with a message 'set dev version'
"""
from setuptools import find_packages, setup

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='gritlm',
    version='1.0.2',
    description='GritLM',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="text generation, text embeddings, instruction tuning",
    license="Apache",
    author='Niklas Muennighoff',
    author_email='n.muennighoff@gmail.com',
    project_urls={
        "Huggingface Organization": "https://huggingface.co/gritlm",
        "Source Code": "https://github.com/ContextualAI/gritlm",
    },
    url="https://github.com/ContextualAI/gritlm",
    packages=find_packages(),
    python_requires=">=3.7.0",
    install_requires=[
        'accelerate==0.26.1',
        'transformers==4.37.2',
        'datasets==2.16.1',
        'wandb',
        'mteb==1.4.0'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],    
)
