from setuptools import setup
version = '0.0.1'
setup(name = 'QuantLib',
      version = version,
      description = 'QuantLib Python bindings',
      packages = [],
      data_files = [('', ['Release/__init__.py']),
	                ('', ['Release/QuantLib.py']),
	                ('', ['Release/_QuantLib.pyd'])],
      install_requires =  [],
      zip_safe = False
)
