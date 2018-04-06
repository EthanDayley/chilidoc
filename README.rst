ChiliDoc
=========

This package is designed to provide an AsciiDoc-like markdown language
which can be compiled to "pure" html.

**Please note that this project is in pre-alpha and is not currently functioning.**


:Authors:
    Ethan Dayley
:Version:
    1.0.0

Installation
------------

Install with pip: `pip install chilidoc`

Usage
------

::
    Import chilidoc
    converter = HtmlConverter(your_chilidoc_string)
    html = converter.convert()

