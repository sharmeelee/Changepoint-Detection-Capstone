from setuptools import setup 
setup( 
	name='Changepoint-Detection-Capstone', 
	version='1.0', 
	description='A program that recommends movies.', 
	author=['Priyanka Bijlani', 'Sharmeelee Bijlani', 'Dhruv Arora', 'Lakshmi Venkatasubramanian', 'Divya Pandey'], 
	packages=['Changepoint-Detection-Capstone'], #same as name 
	install_requires=['numpy', 'pandas', 'kats', 'matplotlib', 'scipy', 'sklearn'] #external packages as dependencies 
)
