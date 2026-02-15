# 146-4-continue-where-146-1-left-off.md

- before we can connect to a cluster,
  we need to set up a Python virtual environment

  - ...

  - we also need to install <u>Databricks Connect</u>
    and
    that needs to be the same version as the `Databricks Runtime Version`

  - ...

  - activate the Python virtual environment
    and
    install the correct version of `databricks-connect` therein

- in the Databricks extension,
  click on `Select a cluster`

- create a notebook called `notebook.ipynb`
  and
  select the kernel, which `databricks-connect` was installed in

  ```ipython
  # In Databricks, notebooks can be of the `.dbc` extension or the `.ipynb` extension.
  #
  # `.ipynb` is Jupyter notebook format with explicit cells and kernels.
  # VS Code has built-in support for such notebooks,
  # which enables it to parse such files and run cells interactively.
  #
  # In VS Code, `.dbc` is not supported the same way.
  # `.dbc.` is a Databricks Export Archive Format, meant for Databricks only,
  # so VS Code cannot execute it natively.
  #
  # That's this is created as an `.ipynb` file.
  # And that's what we should do for all of our notebooks,
  # b/c that's also supported in Databricks.

  df = spark.read.table("population_metrics.default.countries_consolidated")

  # Recall that
  # `df.display()` is Databricks-only
  # so, instead of that, call the following:
  df.show()
  ```

- running the cell will open a pop-up window
  telling you to install the `ipykernel` package

<br />
<hr />
<br />

The Databricks extension makes it possible for you

- to interact with your clusters,
  e.g. you can stop/terminate a cluster

- connect to various different clusters;
  the only thing we need to do is
  ensure
  (a) we've got the appropriate Python virtual environment activated
  and
  (b) the appropriate `databricks-connect` version is installed [in that virtual environment]
