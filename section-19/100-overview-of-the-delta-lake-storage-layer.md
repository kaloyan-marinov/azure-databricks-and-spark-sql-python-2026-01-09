# 100-overview-of-the-delta-lake-storage-layer.md

## Introduction

The focus of this section of the course is on the `DELTA LAKE` storage layer.

Even though we've used it (in earlier sections of the course),
now we're going to
do a deep dive
and
really understand
how `DELTA LAKE` underpins the Databricks Data Lakehouse.

## Recall: ACID guarantees

(a) Atomicity 

<u>TODO (2026/01/18, 13:57 CET): the following statement is sloppy/inaccurate & needs to be corrected</u>
Each statement in a transaction (to read, write, update or delete data)
is treated as a single unit.
Either the entire statement is executed,
or none of it is executed.

(This property prevents data loss and corruption from occurring.)

(b) Consistency

Ensures that transactions only makes changes to tables in predefined, predictable ways.

(c) Isolation

<u>TODO (2026/01/18, 13:57 CET): the following statement is sloppy and too verbose & needs to be improved</u>
When multiple users are reading from and/or writing to the same table all at once,
isolation of their transactions ensures that
concurrent transactions don't interfere with or affect one another.

(d) Durability

Ensures that changes to your data made by successfully executed transactions
will be saved, even in the event of system failure.



## Comparison among Data Warehouses, Data Lakes, Data Lakehouses

You can think of a «Data Lakehouse» as
- a «Data Lake»
- but with that extra ACID compliance and reliability that «Data Warehouses» bring.

Q: So where does that extra compliance come from?

A: It comes from the `DELTA LAKE` storage format.

<br />
<br />
<br />

We have made those comparions earlier in the course.

Just as a reminder.

|                | Pro                               | Con                             |
| -------------- | --------------------------------- | ------------------------------- |
| Data Warehouse | excel at handling structured data | expensive to scale <br /> (to handle big data) |
|                | ACID transaction guarantees       | can only handle structured data  <br /> (and don't support ML or "modern-analytics" workloads) |
| Data Lake      | much cheaper                      | lack of ACID transaction guarantees [see (DL1)]|
|                | rely on distributed storage <br/> which allows them to scale to handle big data (petabytes) |  z |
|                | can handle all sorts of data <br /> structured, semi-structured, and unstructured |  z |
|                | support ML or "modern-analytics" workloads |  z |
| Data Lakehouse | y |  z |

<br />
<br />
<br />

(DL1)

  - so updating or deleting a single record requires
    an overwrite of the entire dataset,
    which can get really inefficient

  - Have you ever needed to fix just 1 row in a 1-TB `PARQUET` file?
    To do that in a Data Lake, you'd have to re-write the entire dataset,
    which is painful and expensive.

<br />
<br />
<br />

As simply as I can explain it:

- imagine you have a «Data Lake»

- if you store data in `CSV` or `PARQUET` form,
  it's still a «Data Lake»

- but, as soon as you store data using the `DELTA LAKE` storage layer,
  it's elevated itself to become a «Data Lakehouse»



## `DELTA LAKE`

It is an open-source software that
- extends `PARQUET` files
- with a file-based <u>transaction log</u>

The <u>transaction log</u> is a metadata layer (on top of the `PARQUET` file format),
which makes it possible:
- to track which files are part of different table versions
- to offer rich management features
- to ensure ACID-compliant transactions

---

This is the optimized storage layer
that provides the foundation for storing data and tables
in the Databricks Data Lakehouse platform.

---

The many benefits of `DELTA LAKE` are as follows:

- ACID transactions

- scalable metadata

  allows it to handle PBs of data

- time travel

  allows you to access previous versions of your data

- open source

  benefits from community-driven innovation,
  full transparency,
  and broad ecosystem integration (without vendor lock-in)

- supports batch and streaming workloads

- schema evolution and enforcement

  you can handle changes to the structure of your data

- audit history

- Data Manipulation Language (DML) operations

  allows you to update, delete, and merge datasets,
  which is simply not possible on other file formats (e.g. `CSV` or `PARQUET`)

In the upcoming lectures of this course section,
I'll give you hands-on demonstrations of these benefits.
