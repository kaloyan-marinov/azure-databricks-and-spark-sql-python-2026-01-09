# 219-high-level-CI-CD-workflow-on-databricks.md



## Introduction

The previous lecture gave a generic overview of CI/CD at a generic level.

This lecture describes one concrete application of CI/CD to Databricks.



## Continuous Integration

<u>The project assets</u>:

- make up your "data solution"

- include code files, notebooks, Databricks jobs, cluster configurations, and other resources

- are placed under version control



Every new feature is implemented in its own feature branch.
Each feature branch is tested in a «development» «environment»
(e.g. a «development» «Databricks workspace»).



Once the feature branch is ready for review by one or several teammates,
you create a pull request.



## Continuous delivery

When a pull request (whose target branch is `main`) gets completed,
that triggers an automatic deployment of <u>the project code and artifacts</u>
into a dedicated «UAT» «environment».

> This automation cna be achieved
> via tools like «GitHub Actions» or «Azure DevOps pipeline».

End-to-end tests and data validation are run:

- if the results are satisfactory,
  the deployment can be approved and promoted further

  the same process pushes <u>the project code and artifacts</u>
  into the «production» «environment»

- if not,
  the deployment can be rolled back

- (This ensures that
  what reaches «production» has already been reviewed, validated, and approved.)



## Further learning

This section has given an overview CI/CD.

The practical, hands-on implementation of a full CI/CD workflow in Databricks
could easily fill an entire course by itself.

For example, the course called [CI/CD with Databricks Asset Bundles](
    https://www.udemy.com/course/cicd-with-databricks-asset-bundles/
) covers
how to use «Databricks Asset Bundles» and «GitHub actions»
to implement source control, code review, automated testing, and CI/CD for a "data projects".
