"TDD in Python with pytest" workshop
====================================

This is a Python package used for the "TDD in Python with pytest"
workshop. The ``master`` branch contains an empty project with no tests.
The ``develop`` branch points to the full project, and each commit is a
step in the workshop. The commit messages are prefixed with either "T"
or "C", to show if that commit adds "Tests" or "Code".

The description of the project is the following:

.. code:: txt

    The goal is to write a class Calc that performs calculations: addition, subtraction,
    multiplication, and division. Addition and multiplication shall accept multiple arguments.
    Division shall return a float and division by zero shall return the string "inf".
    Multiplication by zero must raise a ValueError exception. The class will also provide
    a function to compute the average of an iterable. This function gets two optional upper
    and lower thresholds to remove outliers.

(some of the requirements are silly but they help understanding some TDD
concepts)

    Reformatting requirements to enumerate all requirements for reference in tests
    1. write a class Calc that performs calculations on numbers
        1.1 addition
            1.1.1 accept multiple arguments
        1.2 subtraction
        1.3 multiplication
            1.3.1 accept multiple arguments
            1.3.2 multiplication by zero raises a ValueError exception
        1.4 division
            1.4.1 Return a float (example only, not good design. never return a float or string)
            1.4.2 Division by zero returns the string "inf"(example only, not good design. never return a float or string)
        1.5 Provide a function to compute the average of an iterable
            1.5.1 Gets two optional upper and lower thresholds to remove outliers
            1.5.2 The optional thresholds includes equality (use <= and >=)
            1.5.3 Raise ValueError if the list is empty

Instructions
------------

1. Clone the repository
2. Create a virtual environment: ``python3 -m venv <venvname>``
3. Activate it: ``source <venvname>/bin/activate``
4. Install requirements: ``pip install -r requirements/dev.txt``
5. Edit the ``pytest.ini`` file and add the virtualenvironment to the
   ``norecursedirs`` option

.. code:: ini

    [pytest]
    minversion = 2.0
    norecursedirs = .git .tox requirements* <venvname>
    python_files = test*.py

6. Run ``pytest -svv`` to check that everything has been correctly
   installed. You should get a result like

.. code:: txt

    ==================================== test session starts ====================================
    platform linux -- Python 3.6.6, pytest-3.0.7, py-1.7.0, pluggy-0.4.0 -- <PWD>
    cachedir: .cache
    rootdir: <PWD>, inifile: pytest.ini
    plugins: cov-2.4.0
    collected 0 items

    =============================== no tests ran in 0.01 seconds ================================

Credits
-------

This package was created with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the
`lgiordani/cookiecutter-pypackage <https://github.com/lgiordani/cookiecutter-pypackage>`__
project template.
