from azure.mgmt.resource import ResourceManagementClient


credential = "some cred"
subID = "some sub ID"

client = ResourceManagementClient(credential, subID)

client.resource_groups.create_or_update(
    resource_group_name = "someresourcegroup",
    parameters = {
        "location": "eastus"
    }
)