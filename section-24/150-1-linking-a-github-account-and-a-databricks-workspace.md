# 150-1-linking-a-github-account-and-a-databricks-workspace.md

This lecture shows how to link a GitHub account to a Databricks Workspace.

That enables Databricks Job tasks
to access assets (= scripts and/or notebooks) that are available in GitHub repositories.



- click on your user icon on the top right

- click on `Settings`

- click on `Linked accounts`

- click on `Add Git credential`

- select either `Link Git account` or `Personal access token`

  - selecting the first option
    will redirect you to a (GitHub) page,
    which you can use to `Authorize Databricks` in your GitHub account

  - then, under `Linked accounts`,
    click on `Configure in GitHub`;

    sign in to your GitHub account;

    install https://github.com/apps/databricks on your personal GitHub account,
    for either `All repositories` or `Only select repositories`,
    with these permissions: `Read access to metadata` and `Read and write access to code and workflows`
