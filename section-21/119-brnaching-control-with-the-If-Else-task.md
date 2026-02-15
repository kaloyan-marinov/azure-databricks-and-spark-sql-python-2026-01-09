# 119-brnaching-control-with-the-If-Else-task.md



Open an existing `Job` or create a new one.

Click on `Add task`.

Specify `Type` as `If/else condition`.



A realistic scenario is as follows:

- you have an upstream `Task`,
  which a downstream `Task` with a type of `If/else condition` is dependent on

- the upstream `Task` calls `dbutils.jobs.taskValues.set`
  and
  assigns a value,
  which is utilized to specify the condition within the downstream `Task`
  (e.g. via `{{tasks.task_branching_control.values.<the-key-which-was-specified-in-the-set-call>}}`)



Furthermore, the condition can be based on parameters defined in a `Job`.
(e.g. via `{{job.parameters.<the-key-for-the-Job-parameter>`).



To be clear, the condition can be based on

- dynamic-value references

- job parameters

- task parameters
  (recall: `dbutils.widgets.get`)

- literal values

- task values
  (recall: `dbutils.jobs.taskValues.get`)
