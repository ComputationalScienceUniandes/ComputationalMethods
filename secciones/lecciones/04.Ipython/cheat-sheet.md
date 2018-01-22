# IPython Cheat Sheet

## Revert to older versions of IPython

By reaching v>3.0.0, IPython graduated to become the Jupyter project. This change brings tons of advantages (highly recommended), but backwards-incompatibility. 

In order to make your notebook backward-compatible with older IPython versions:

    ipython nbconvert --to notebook --nbformat 3 <notebook>

    