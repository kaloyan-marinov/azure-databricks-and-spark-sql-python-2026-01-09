# 120-running-tasks-in-a-loop-with-the-For-Each-task.md



Open an existing `Job` or create a new one.

Click on `Add task`.

Specify `Type` as `For each`.



Such a `Task` runs another nested `Task` over a list that you provide.
The nested `Task` is run once per item from the provided list.



The `Inputs` to a `Task` with type of `For each` can be specified via:

- hardcoded values

- job parameters

- task values
  (recall: `dbutils.jobs.taskValues.set`;
  then: `{{tasks.<the-notebook-task-that-called-set>.values.<the-key-which-was-specified-in-the-set-call>}}`)
