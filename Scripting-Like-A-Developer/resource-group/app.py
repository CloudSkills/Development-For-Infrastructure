from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential

import sys


def main():
    create_resource_group(subID)

def create_resource_group(subID):
    credential = AzureCliCredential()

    client = ResourceManagementClient(credential, subID)

    client.resource_groups.create_or_update(
        resource_group_name = name,
        parameters = {
            "location": location
        }
    )

subID = sys.argv[1]
name = sys.argv[2]
location = sys.argv[3]

if __name__ == '__main__':
    main()