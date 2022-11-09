# What is Ansible?

Ansible is a configuration management system that automates and simplifies the configuration, maintenance, and deployment of servers and software, and orchestrates more advanced IT tasks such as continuous deployments or zero downtime rolling updates. Ansible started as an open-source project, now owned by RedHat.

At the moment, there are several configuration management systems. However, Ansible is the most used to work with network equipment. This is because Ansible does not require the installation of an agent on managed hosts. This is especially true for devices that allow you to work with them only through the CLI.

- Ansible is an open-source, similar to Chef, Puppet, and Salt.
- Ansible lets you control and configure nodes from a single machine.

In addition, Ansible is actively developing toward support for network equipment, and new features and modules for working with network equipment are constantly appearing in it. Ansible Network modules extend network administrators’ benefits of simple, powerful and agentless automation.

Ansible Network modules can configure your network, test and validate existing network state, and discover and correct network configuration drift.

Some network equipment supports other configuration management systems (allows you to install an agent). One of the great benefits of Ansible is that it's easy to get started with, here are examples of tasks that Ansible can do:

- SSH connection to devices
- Parallel connection to devices
- Run the configuration task
- Sending commands to devices

The modules and what Ansible refers to as the playbooks are similar between server modules and network modules, with some differences.
