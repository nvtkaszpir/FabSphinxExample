
Documentation
==================================================

Documentation is auto generated with:

- `sphinx-doc`_ with `numpydoc`_ - to parse python scripts
- `pandoc`_ - to convert MarkDown files to reStructuredText format
- `LaTeX`_ - to generate pdf

.. _sphinx-doc: http://sphinx-doc.org/
.. _pandoc: http://pandoc.org/
.. _LaTeX: http://www.latex-project.org/

So you may need additional system packages to be able to generate it.

You can generate documentation issuing:

.. code:: bash

    make apidoc
    make html

Then see ``build/html/index.html`` file in your web browser.

How to write documentation
==================================================

Documentation is written in `reStructuredText`_, so you can read it as plain text as well, you can also convert it to HTML or PDF or whatever. See :doc:`Documentation.sandbox` if you want some examples.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html

Within python documents follow docstring or `numpydoc`_ conventions.

.. _numpydoc: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt


