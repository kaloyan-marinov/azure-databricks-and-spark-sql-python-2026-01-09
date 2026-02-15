# 143-runtime-compatibility.md



As you know,
Databricks clusters run on a specific <u>Databricks Runtime</u>.

- when you create a cluster in Databricks,
  you choose a Runtime version

- that choice determines the versions of
  Spark, Python, Scala, Java and the extra libraries,
  or the optimizations you get



Recall that,
earlier in the course,
we created a `Job compute` cluster.
It was called `job-380885752234008-run-1003135680009780-classic_job_compute_f4`
and
it was created with
```
Databricks Runtime Version

17.3 LTS (includes Apache Spark 4.0.0, Scala 2.13)
```

[This link](
    https://learn.microsoft.com/en-us/azure/databricks/release-notes/runtime/17.3lts#system-environment
) shows <u>the system environment</u> for that <u>Databricks Runtime</u>.
For your convenience, that link contains the following information:
```
System environment

- Operating System: Ubuntu 24.04.3 LTS
- Java: Zulu17.58+21-CA
- Scala: 2.13.16
- Python: 3.12.3
- R: 4.4.2
- Delta Lake: 4.0.0
```

The lecturer goes on to say:
> So, in my local system,
> I need to ensure I have [those] versions of Java and Python installed.
> ...
> You should make sure
> you have the specific versions installed for your relevant Databricks Runtime.

[
<u>But _why_ do those versions need to be installed on my local system?</u>

<u>_If_ it's really necessary, it should be possible to use this container image: https://hub.docker.com/layers/databricksruntime/standard/17.3-LTS/images/sha256-df4ed0f79b3a5bd866dac7bf552f15b6b92b8fd3e8773252e2dc2597331e6449</u>
]