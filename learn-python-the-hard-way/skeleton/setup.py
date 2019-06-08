try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Skeleton desc.',
	'author': 'Júlio Batista',
	'url': 'http://skeleton.uri',
	'download_url': 'http://skeleton.uri',
	'author_email': 'julio.batista@outlook.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Skeleton'
}

setup(**config)