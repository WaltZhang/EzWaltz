from setuptools import setup, find_packages

def read():
    with open('README.md') as f:
        return f.read()

setup(
    name='EzWaltz',
    version='0.1.0',
    description='Walt\'s common library for basic usages.',
    author_email='walt.zhangwenguang@gmail.com',
    packages=find_packages(),
    scripts=['mail/ssl_email.py', 'logger/builder.py', 'logger/handlers.py'],
    zip_safe=False
)
