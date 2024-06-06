# Ansible Basic Architecture

Ansible started by managing servers before expanding its ability to manage networking equipment. Ansible modules support a wide range of vendors, device types, and actions, so you can manage your entire network with a single automation tool.

With Ansible you can:

- Work without installing an agent on managed hosts.
- Automate repetitive tasks to speed up routine network changes.
- Perform changes using Python modules that run on the control.
- Communicate securely with network hardware over SSH or HTTPS.
- Benefit from the community and vendor-generated sample playbooks and roles.

## Ansible Component

This Section introduces basic Ansible concepts and guides you through your first Ansible commands, playbooks and inventory entries. These concepts are common to all uses of Ansible, including network automation. You need to understand them to use Ansible for network automation.

- Control node.  The Ansible server from which the control tasks take place. You can use any computer that has Python installed on it as a control node. However, you cannot use a Windows machine as a control node but on WSL (Windows Sub System for Linux) can install Ansible.
- Manage node. The network devices (and/or servers) you manage with Ansible.
- Inventory - inventory file. This file describes hosts, groups of hosts, and variables. Your inventory can specify information like IP address for each managed node.
- Playbook - script file. Ordered lists of tasks can include variables written in YAML and are easy to read, write, share and understand.
- Play - script (set of tasks). Associates tasks with hosts for which these tasks
- Task - task. Calls the module with the specified parameters and variables
- Module. Implements certain functions. Each module has a particular use, from administering users on a specific type of database to managing VLAN interfaces on a specific type of network device.
