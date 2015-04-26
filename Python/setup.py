import setuptools

setuptools.setup(
        name = "pybookeeping",
        version = 0.0,
        url = "https://github.com/rash805115/bookeeping.frontend/tree/master/Python",
        author = "Rahul Chaudhary",
        author_email = "rahul300chaudhary400@gmail.com",
        description = "Python flavored API to assist developing the frontend for BooKeeping project.",
        install_requires = ["boto == 2.37.0", "requests == 2.6.0"],
        packages = setuptools.find_packages()
)