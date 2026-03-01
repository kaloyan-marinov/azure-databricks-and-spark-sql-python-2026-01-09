# 170-demo-_-giving-the-new-user-access-to-a-databricks-workspace.md

## Observe

(Within the Azure Portal,)
The newly-created Azure User can see the «Databricks workspace».

But if the user tries to click on `Launch Workspace`,
they will get a message saying "... You do not have permissions to access this page."


## Give the new user access to the workspace

- use the first Azure User (mentioned in `section-27/169-creating-a-new-user-on-azure-for-upcoming-demos.md`)
  to sign in to the «Databricks» workspace

- this user MUST have the «workspace admin» role

  - go to `Settings`

  - `Identity and access`

  - `Users`

  - `Add user`

    because we are using «SCIM provisioning»
    (as recommended by Databricks - cf. `section-27/165-2-identities-in-azure-databricks.md`),
    the new Azure User was synchronized to the Databricks Account console
    and,
    consequently, we can find them via the `Add user` dialog window (by simply pasting in their email address)

---

- sign into the Azure Portal
  as the newly-created Azure User's account

- click on `Launch Workspace`

- this time, the «Databricks workspace» will load up
  (indicating/proving that the user has got access to the «Databricks workspace» in question)
