#!/media/banshe/New Volume/Software_dev_AS/Software_Development_TC_2024/SDEV_220_Python/Module_4/modulo_4/djangotest/bin/python
"""Reloads the given site

Usage:
  pa_reload_webapp.py <domain>

Options:
  <domain>              Domain name, eg www.mydomain.com
"""

from docopt import docopt

from pythonanywhere_core.webapp import Webapp
from snakesay import snakesay


def main(domain_name):
    webapp = Webapp(domain_name)
    webapp.reload()
    print(snakesay(
        f"{domain_name} has been reloaded"
    ))


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments['<domain>'])
