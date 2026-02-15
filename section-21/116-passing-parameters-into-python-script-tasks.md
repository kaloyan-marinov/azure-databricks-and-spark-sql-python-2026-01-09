# 116-passing-parameters-into-python-script-tasks.md

It is possible to pass parameters into Python Script Tasks.

That is done by providing values
(which can be literal values or dynamic values).
For example:
```json
["John", "{{worspace.id}}"]
```

The script reads them in by utilizing `sys.argv`,
where `sys` is a module from the Python Standard Library.
