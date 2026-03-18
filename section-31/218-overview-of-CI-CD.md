# 218-overview-of-CI-CD.md



## Introduction

«CI/CD» stands for one of these things:

- Continuous Integration and Continuous Delivery

- Continuous Integration and Continuous Deployment



Sometimes, those terms are used interchangeably.
But they actually mean different things.

- with Continuous Delivery:

  your (code or schema) changes are validated, built, and released into a lower «environment»;

  when they are ready to go to «production»,
  someone will still need to approve that promotion - 
  that is a manual step

- with Continuous Deployment:

  once all of your changes pass all of the relevant checks, they are immediately pushed into «production» (jobs or «environments»)
  without human intervention


## Environments

The process of building "data solutions" takes place across different «environemnts».


- «development» environment

   - try out new logic

   - run our pipelines on sample datasets (or on limited datasets)

   - iterate quickly until things look stable;
     then, promote the changes into a ...

- «testing» [or, more precisely, «user acceptance testing» (UAT)] environment 

   - run the pipelines on more realistic datasets (or on larger datasets)

   - validate accuracy, performance, and data quality

   - catch issues before the next step

   - if everything "checks out", the changes are deployed into a ...

- «production» environment

   - where real business decisions depend on the results



Those «environments» might be separate «Databricks workspaces»,
or - in some instances - separate areas within a single «Databricks workspace».
(Either way, the goal is the same -
namely, to move changes forward safely
without disrupting what is already running in «production».)



## What is «CI/CD»?

CI/CD is a framework/practice
for automating and standardizing that journey of code changes/enhancements
from «development» through to «production».

The benefit is that:

- it eliminates reliance on manual steps and risky deployments;

- every change is validated, packaged, and deployed
  in an automated and repeatable way

---

Commonly, CI/CD is depicted as an "infinity loop":

- whose left side focuses on creating and validating changes
  (=: continuous integration)

- whose right side focuses on deploying changes and operating them in «production»
  (=: continuous delivery or continuous deployment)

---

Let us a walk through each stage.

1. plan

   agree on the requirements,
   whether that's a new data «pipeline», a «schema» update, or an optimization

   set the scope and success criteria <u>before</u> any code is written

2. code/implement

   within a version control system,
   write transformations, orchestrations, and infrastructure definitions

3. build

   produce artifacts that can run consistently across «environments»

   (in the context of data engineering, this often mean
   packaging files, notebooks, jobs and cluster configurations)

4. test

   check whether:
   
   (a) the pipeline runs without crashing

   <u>AND</u>

   (b) the data output is correct
       (by performing data-validation checks
       to catch issues before the next step)

5. release

   create a stable version of the code or artifacts
   that can be promoted across «environments»
     
   Every release is reproducible,
   so rollbacks are straightforward if needed.

6. deploy

   move the release into a higher «environments»
   (whether that is «development», «testing», or «production»)

   this should be automated

7. operate

   run pipelines run every day
   
   monitor jobs
   
   manage costs
   
   handle schema changes carefully
   to avoid breaking downstream systems

8. monitor

   track pipeline health (like runtimes and failures) 
   
   track data health (such as freshness, completeness, and quality)

   > monitoring provides the feedback that drives the next cycle in the "infinity loop",
   > which starts with a «plan» stage



## Summary

CI/CD ensures that changes can move <u>quickly</u> and <u>safely</u> from «development» to «production»,
providing the business/company with <u>reliable</u> data <u>without slowing down delivery</u>.
