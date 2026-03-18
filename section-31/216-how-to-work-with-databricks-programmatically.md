# 216-how-to-work-with-databricks-programmatically.md



## Introduction

Up to now,
we have used only one method of interacting with Databricks -
via its Web User Interface (UI).

In addition to that,
there exist several methods of interacting with Databricks programmatically:

- the Databricks REST API

- the Databricks SDKs

- the Databricks CLI



## Why would one want/need to interact with Databricks programmatically?

Clicking through the UI of Databricks
in order to create «Jobs», create «clusters», or deploy updates
is manual, slow, and error-prone.

Interacting with Databricks programmatically
ensures consistency and lays the groundwork for practices like CI/CD,
which will be covered later on in this section.



## Databricks REST API

It is the most complete and up-to-date interface.

It is the best option when you need
full control
or
access to a feature that isn't supported elsewhere yet.



## Databricks SDKs

Databricks SDKs are available for several programming languages.

These SDKs:

- wrap the REST API

- provide a friendlier, language-native interface

- take care of things like authentication and retries

- let you call methods directly instead of writing raw HTTP requests



## Databricks CLI

The Databricks CLI is a command-line tool.

It:

- is built on top of the APIs

- is ideal for quick administrative tasks in the terminal

- is very commonly used in automation pipelines

- supports «Databricks Asset Bundles»

  (= a Databricks-native tool that allows you to
  define jobs, clusters, and workflows in a configuration file
  and
  then validate and deploy them with a couple of commands)



## Summary

The REST API provides the most complete and direct way to interact with Databricks.

The SDKs build on that
by making the same functionality easier to use with code.

The CLI offers a command-line interface
that is well suited for scripting and automation.
