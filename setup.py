from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='kevin george',
    author_email='kevingeorge2015@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","langchain_community","altair"],
    packages=find_packages()
)