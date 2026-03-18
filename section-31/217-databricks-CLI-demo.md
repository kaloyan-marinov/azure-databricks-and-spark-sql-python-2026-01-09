# 217-databricks-CLI-demo.md



## Sources

- https://docs.databricks.com/aws/en/dev-tools/cli/commands



## Example

To create a «cluster», you can issue the following command:

```json
// cluster_definition.json
{
    "cluster_name": "[created-via-CLI] Standard_F4 Single-Node Cluster",
    "spark_version": "17.3.x-scala2.13",
    "node_type_id": "Standard_F4",
    "autotermination_minutes": 10,
    "data_security_mode": "DATA_SECURITY_MODE_AUTO",
    "runtime_engine": "STANDARD",
    "kind": "CLASSIC_PREVIEW",
    "is_single_node": true
}
```

```shell
# Log in to a Databricks workspace or account by issuing
# ```
# databricks auth login HOST [flags]
# ```

databricks clusters create \
    --json @cluster_definition.json
```



## Last but not least

This was just a short demonstration,
but the CLI can be used for a lot more.

It can be used to issue:

- «compute cluster» commands

- «Databricks workspace» commands

- «jobs» commands and so much more.



The REST API, SDKs, and the CLI are tools
that you can use to automate and standardize the deployment of Databricks assets.
That makes them essential for CI/CD.
