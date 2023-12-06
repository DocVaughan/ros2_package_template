***NOTE:*** Please delete this file prior to the first commit of this package. 
If you do not have, or plan to have, Python modules, please also delete the 
folder.

This folder should contain the core (custom) Python modules that are part of 
the project. To import from Python files in this folder you can use 

    import {{ cookiecutter.project_name | snakecase }}.module_to_import

or

    from {{ cookiecutter.project_name | snakecase }}.module_to_import import <class, function, etc>

where `module_to_import` is the name of the Python file that you'd like to 
import or import from.