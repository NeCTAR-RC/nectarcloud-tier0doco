# Availability Zones

The Nectar Cloud is organised in Availability Zones, that are hosted by the
nodes participating institutions. In many cloud usage scenarios you won't need
to worry about these: the Nectar software will select a suitable Availability
Zone for you when you launch your VM. In certain other scenarios, however, you
have to select the AZ that is right for your purpose.

## How to select an Availability Zone at launch

You can select a specific Avalability Zone for your VM at Launch time in the
Launch Dialog's Availability Zone. The default option is "(Any availability
zone)" If you leave this selected Nectar will find a suitable AZ for you.
![Screenshot of Launch Dialog AZ Tab][Launch Dialog AZ Tab]

## Scenarios

If your VM uses **persistent volume storage**, your VM and your storage must
be in compatible Availability Zones. You can find more information about
storage [here] [Cloud Storage]

In some scenarios you can use **institutionally licensed software**, in which
case you may need to select the appropriate Availability Zone

Some participating institutions offer **private availability zones**, for which
you may be eligible. You will have to contact your Node's local support.

[Launch Dialog AZ Tab]: images/launch_dialog_az_tab.png
[Cloud Storage]: introduction_to_cloud_storage.md
