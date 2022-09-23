# It should have
# setup.py, setup.cfg,
# setup(
    # name='package_name',
    #version='',
    # description,
    # URL,
    # licence = 'LICENCE.txt',
    # Author,
    # Author_email,
    # packages = ['package1', 'package2'],
    # python_requirements = '>3.5, <4 ',
    # install_requirements = [
    # ],
# ),
# README.rst/README.md, license.txt, MANIFEST.in, <package>, data, tests
# installing local package
# pip install <path to package>

# Publishing a package to Test PyPI
# In addition to the account with Test PyPI, we also need to add an API token to the account.
# We will leave the details of creating an account and adding an API token to the account
# for you by following the instructions available on the Test PyPI website (https://
# test.pypi.org/).
# To push the package to Test PyPI, we will need the Twine utility. We assume Twine is
# installed using the pip utility. To upload the masifutilv2 package, we will execute the
# following steps
# 1. python setup.py sdist
# 2. twine upload --repository testpypi dist/masifutilv2-0.1.0.tar.gz
#
# Installing the package from PyPI
# pip install --index-url https://test.pypi.org/simple/ --no-deps masifutilv2