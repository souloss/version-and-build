import os, ssl, platform

__version__ =  '0.1.0'
__project_name__ = 'version-and-build demo'

def get_build_version():
    filename = os.path.join(os.path.dirname(__file__), 'BUILD_GITSHA')
    if not os.path.exists(filename):
        return 'unknown'
    with open(filename) as fh:
        return fh.read().strip()

def get_build_repo():
    filename = os.path.join(os.path.dirname(__file__), 'BUILD_GITREPO')
    if not os.path.exists(filename):
        return 'unknown'
    with open(filename) as fh:
        repolist = [ tuple(i.split()) for i in fh.read().strip().split('\n') ]
        return repolist

def get_build_date():
    filename = os.path.join(os.path.dirname(__file__), 'BUILD_DATE')
    if not os.path.exists(filename):
        return 'unknown'
    with open(filename) as fh:
        return fh.read().strip()

def get_last_commit_date():
    filename = os.path.join(os.path.dirname(__file__), 'BUILD_LASTCOMMITDATE')
    if not os.path.exists(filename):
        return 'unknown'
    with open(filename) as fh:
        return fh.read().strip()

def get_version_info(dictize=True):
    result = {
        f"{__project_name__} version":__version__,
        platform.python_implementation():platform.python_version(),
        "OpenSSL version":ssl.OPENSSL_VERSION,
        "Build date":get_build_date(),
        "Last commit date":get_last_commit_date(),
        "Build version":get_build_version(),
        "Build repo":get_build_repo()
    }
    if dictize:
        return result
    else:
        return "\n".join([f"{k}:{v}" for k,v in result.items()])

get_version_info()