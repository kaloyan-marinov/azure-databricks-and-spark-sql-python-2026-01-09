# 141-local-development-overview.md



Instead of writing everything directly in the Databricks Workspace's web UI,
you can treat your codebase more like a normal software project.

- [you create a Git repository]

- you write code in your local Integrated Development Environment (IDE)



https://learn.microsoft.com/en-us/azure/databricks/dev-tools/

> Databricks provides an ecosystem of tools to help you
> develop applications and solutions that integrate with Azure Databricks
> and
> programmatically manage Databricks resources and data.

> [Each tool serves a slightly different purpose.]



For example,
you can work locally with the help of the Databricks extension for VS Code:

- via the Databricks extension (which is, obviously, on your local machine),
  set up a connection to your remote Databricks Workspace

- write code on your local machine
  (outside of the Databricks Workspace)

- run the code on the remote compute cluster,
  which is configured via the Databricks extension,
  and
  see the results on your local machine
