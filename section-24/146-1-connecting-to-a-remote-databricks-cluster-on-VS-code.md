# 146-connecting-to-a-remote-databricks-cluster-on-VS-code.md

The purpose of this lecture is
to demonstrate how you can connect your Databricks Cluster remotely
using VS Code.

In VS Code,
an essential component to be able to connect to a remote Databricks Cluster
is the Databricks extension for VS Code.

- create a Databricks Cluster
  and
  take note of its `Databricks Runtime Version`

- in the side-bar panel, click on the icon for the Databricks extension

- click on `Create configuration`

  - specify the Databricks Host
    (e.g. https://adb-7405612818031955.15.azuredatabricks.net )

  - select one of the various authentication methods:
    OAuth (Recommended), Azure CLI, Personal Access Token, ...

    if you select OAuth,
    you will be asked to enter a name for the new profile;
    you _can_ give the profile the same name as the workspace
    (but note that the names _don't have to_ be the same)

    once you do that,
    you should have a connection established

- before we can connect to a cluster,
  we need to set up a Python virtual environment

  - the Python version should be
    the same as
    the one that is included in the cluster's `Databricks Runtime Version`

  - we also need to install <u>Databricks Connect</u>
    and
    that needs to be the same version as the `Databricks Runtime Version`

    - context: https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect/

    - Databricks Connect is a client library for the Databricks Runtime
      that allows you
      to connect to Azure Databricks compute
      from
        IDEs such as Visual Studio Code, PyCharm, and IntelliJ IDEA,
        notebooks
        and any custom application,
      to enable new interactive user experiences
      based on your Azure Databricks Lakehouse.

    - Databricks Connect is available for the following languages:
      Python,
      R,
      Scala

    - What can I do with Databricks Connect?

      ...
      write code using Spark APIs
      and
      run them remotely on Azure Databricks compute instead of in the local Spark session.

      - enables developers
        to develop and debug their code on Databricks compute
        using any IDE's native running and debugging functionality

      - ...