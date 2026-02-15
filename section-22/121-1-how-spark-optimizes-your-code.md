# 121-1-how-spark-optimizes-your-code.md

(a) Build-in, automatic optimizations
    (= Spark optimizes your code under the hood)

(b) Hands-on tuning techniques



In this lecture, we'll:

- take a look at (a)

- give a high-level explanation of
  what's involved in executing a Spark application
  and
  the automatic query optimizations that take place



When you submit your PySpark script to a Databricks cluster,
the `Driver Process` launches a `Spark Application`
and
immediately creates one `Job` for each <u>action call</u>.

Each `Job` is then divided into `Stages`,
which group together the operations that can run without <u>re-shuffuling</u> data.

Every `Stage` spins up multiple `Task`s - one per <u>data partition</u> -
that execute in parallel across your worker nodes.

[see 121-2-.jpeg]



This hiererachical model of `Job`s, `Stage`s, and `Task`s
is
what lets Spark distribute work efficiently.
