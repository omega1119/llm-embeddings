from setuptools import setup, find_packages

setup(
    name='pdfchat',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'PyMuPDF',
        'faiss-cpu',
        'numpy',
        'python-dotenv',
        'langchain',
        'langchain-openai',
        'langchain-community',
        'tqdm'
    ],
)
