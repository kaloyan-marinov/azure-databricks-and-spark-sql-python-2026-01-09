# 115-passing-task-values-between-notebook-tasks.md



```python
# In the NB executed by the task called `task_01_notebook`.

dbutils.jobs.taskValues.set(
    key='my-key',
    value=17,
)
```

The value cannot exceed 48 KiB & must be JSON-serializable.

```python
# In the NB executed by the task called `task_02_notebook`.
dbutils.jobs.taskValues.get(
    taskKey='task_01_notebook',
    key='my-key',
    default=42,
    debugValue=-42,
)
```
