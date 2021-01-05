# Using the Python Code

This section creates a resource group using Python and the Azure SDK

## Prerequisites
To use this code, you must have:
1. A code editor or IDE, like VS Code or PyCharm
2. Azure CLI installed and configured. If you need help setting that up, you can find a how-to guide [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

## Packages
The two packages used are:
1. azure-mgmt-resource
2. azure-identity

`azure-mgmt-resource` is used, in this case, to create a resource group. There are plenty of other use-cases for it as well and if you'd like to see more of them, you can check out the `resource_group_operations` found in the SDK documentation [here](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/resources/azure-mgmt-resource/azure/mgmt/resource/resources/v2020_06_01/operations/_resource_groups_operations.py)

`azure-identity` is used to authenticate to Azure from the Python SDK. In this case, you'll be using the Azure CLI credentials on your local computer to authenticate with `azure-identity` 