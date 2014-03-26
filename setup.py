#!/usr/bin/env python
#
# BitTorrent Tracker using Tornado
#
# @author: DarkArtek <artek@ahsubs.net>
# Created on 12th March 2014
# http://darkartek.github.io/Pytr

from setuptools import setup, find_packages

setup(
    name = "Pytr",
    version = "0.1.7",
    packages = find_packages(),
    install_requires = ['setuptools',
                        'tornado >= 1.2.1',
                        ],
    extras_require = {'test': ['nose']},
    scripts = ['scripts/pytr'],

    # metadata for upload to PyPI
    author = "DarkArtek",
    author_email = "art3k@ahsubs.net",
    description = "A Pure Python BitTorrent Tracker using Tornado",
    license = "http://www.apache.org/licenses/LICENSE-2.0",
    keywords = "bittorrent tracker bencode bdecode scrape ui",
    url = "http://pytr.ahsubs.net",
    zip_safe = True,
    long_description = """Pytr is a simple BitTorrent tracker written using Tornado non-blocking web server. It also features a UI for showing tracker statistics.""",
)