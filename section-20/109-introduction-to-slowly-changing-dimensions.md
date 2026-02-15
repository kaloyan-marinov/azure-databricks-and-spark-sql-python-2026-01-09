# 109-introduction-to-slowly-changing-dimensions.md

## Dimensions

<u>Dimensions</u> are descriptive attributes
that give context to your quantitative facts.

For example, this is a <u>dimension table</u>:

| id | name    |
| -- | ------- |
| 10 | America |
| 20 | Europe  |
| 30 | Asia    |
| 40 | Oceania |
| 50 | Africa  |

- We don't expect dimensions to change frequently.

- But, when they do,
  we need to have a technique in place to handle that.

## Slowly Changing Dimensions

Slowly Changing Dimensions (SCDs) are techniques
that manage how dimension data changes over time.

As an example,
let's say we need to make the following change to the above-mentioned dimension table:

| id        | name       |
| --------- | ---------- |
| <b>10</b> | <b>USA</b> |

## SCD Type 1

Simply overwrite the value:

| id        | name       |
| --------- | ---------- |
| <b>10</b> | <b>USA</b> |
| 20        | Europe     |
| 30        | Asia       |
| 40        | Oceania    |
| 50        | Africa     |

- no history is retained

- this is only really useful
  when historical data isn't required

## SCD Type 2

You need to have additional columns in your dimension table:

| id | name    | effective_date | end_date |
| -- | ------- | -------------- | -------- |
| 10 | America | 2026-01-01     | NULL     |
| 20 | Europe  | 2026-01-01     | NULL     |
| 30 | Asia    | 2026-01-01     | NULL     |
| 40 | Oceania | 2026-01-01     | NULL     |
| 50 | Africa  | 2026-01-01     | NULL     |

The `effective_date` is when the row was added to the dimension table.

The `end_date` indicates if the row is current/"active".

As an example,
let's say we need to make the above-mentioned change on 2026-01-18,
we would
first de-activate the existing record with `id = 10` by setting its `end_date`,
and then insert the new record:

| id        | name       | effective_date    | end_date          |
| --------- | ---------- | ----------------- | ----------------- |
| 10        | America    | 2026-01-01        | <b>2026-01-18</b> |
| <b>10</b> | <b>USA</b> | <b>2026-01-18</b> | <b>NULL</b>       |
| 20        | Europe     | 2026-01-01        | NULL              |
| 30        | Asia       | 2026-01-01        | NULL              |
| 40        | Oceania    | 2026-01-01        | NULL              |
| 50        | Africa     | 2026-01-01        | NULL              |

With SCD Type 2,
the full history is preserved.

In the vast majority of cases when history preservation is needed,
then SCD Type 2 is used.

## SCD Type 3

Create a `previous_name` attribute:

| id        | current_name       | <b>previous_name</b> |
| --------- | ------------------ | -------------------- |
| <b>10</b> | <b>USA</b>         | America              |
| 20        | Europe             | NULL                 |
| 30        | Asia               | NULL                 |
| 40        | Oceania            | NULL                 |
| 50        | Africa             | NULL                 |

With SCD Type 3,
you really only retain the history
for the current and the preceding values.
So it's not really that helpful.

It really isn't as effective as SCD Type 2.

# Other SCD techniques

For example,
you can keep all of the historical values in a separate table.

But, by far, the most commonly implemented type is SCD Type 2.
