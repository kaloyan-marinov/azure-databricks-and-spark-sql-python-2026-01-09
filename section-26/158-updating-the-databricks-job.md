# 158-updating-the-databricks-job.md

Since our code is now in a GitHub repository,
we need to point the Databricks Job tasks to the relevant notebooks.

We can:

- either:
  specify the `Path` for each task as a `Git provider`

- or:
  create a Databricks Git folder
  (as per `section-24/151-databricks-git-folders.md`)
  and
  point each task in that Databricks Git folder
