# 169-creating-a-new-user-on-azure-for-upcoming-demos.md

## Recall

As a pre-requisite for the remainder of `section-27/`,
you need to:

- have:

  - one Azure account

  - one Azure User within that account

  - one «Databricks workspace» within that Azure account

- be able to sign into the Databricks Account console
  as the above-mentioned Azure User

## Create a new Azure User

In the Azure Portal,
create a new Azure User.

Assign
the `Reader` role for the above-mentioned «Databricks workspace» (or for an encompassing Azure Resource Group)
to the newly-created Azure User.

Q: Why?

A: Because the remainder of `section-27/` will demonstrate
   how to give the newly-created Azure User access to
   - the Databricks account,
   - «Unity Catalog» «securable objects», and
   - «Databricks workspace» «securable objects».
