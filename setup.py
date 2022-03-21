from setuptools import setup

setup(name='takeover',
      version='0.3',
      description='Takeover-alert',
      url='https://github.com/VikzSharma/takeover-alert',
      author='vikzsharma',
      license='MIT',
      scripts=['takeover.py'],
      install_requires=[
          'requests',
          'urllib3',
          'python-decouple',
      ],
      entry_points={
          'console_scripts': ['takeover=takeover:main'],
      },
      zip_safe=False)
