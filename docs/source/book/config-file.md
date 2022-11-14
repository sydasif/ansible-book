# Ansible Configuration

Ansible settings can be changed in the configuration file. Ansible supports several sources for configuring its behavior including command line option; any command-line option will override any configuration setting. The Ansible configuration file can be stored in different locations (Ansible will process the below list and use the first file found, all other settings are ignored.). See [precedence rules](https://docs.ansible.com/ansible/latest/reference_appendices/general_precedence.html#controlling-how-ansible-behaves-precedence-rules) for more information.

- ANSIBLE_CONFIG environment variable
- ansible.cfg in the current directory
- ~/.ansible.cfg in the user's home directory
- /etc/ansible/ansible.cfg default location

Ansible looks for the configuration file in the specified order and uses the first one it finds. But user can change many parameters in the configuration file. A complete list of parameters and their descriptions can be found in the [documentation](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings). In the current directory, create the following ansible.cfg configuration file:

```console
[defaults]
inventory = ./hosts
remote_user = admin
ask_pass = True
```

Parameter settings in the configuration file:

- [defaults] - This configuration section describes the general default settings.
- inventory = ./hosts - The inventory allows you to specify the location of the inventory file.
- remote_user = cisco - The user Ansible will connect to managed node.
- ask_pass = True - this option is the same as the --ask-pass option on the command line.

Now we have set parameters in our configuration file, so we need to amend the variable in the inventory file as below:

```ini
[router:vars]
ansible_network_os=ios
ansible_connection=network_cli
```

When we use the ansible --version command, it will show the exact location of the configuration file, which by default is in /etc/ansible/ansible.cfg, first line shows the location of Ansible configuration file.

```console
$ ansible --version
ansible 2.9.27
  config file = /home/syed/ansible.cfg
  configured module search path = ['/home/syed/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/syed/.local/lib/python3.10/site-packages/ansible
  executable location = /home/syed/.local/bin/ansible
  python version = 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0]
```

Fortunately, we can overrides both default Ansible configuration file and inventory file for each project, since each project may have its own configuration parameters and a different list of devices to be managed remotely. It is therefore recommended to create a folder with its own configuration and inventory file for each project.

At this stage, if we run our previous ad-hoc command the result will be the same except for asking for the password.

## Gathering Facts

Ansible By default collects facts about devices; these facts are information about the hosts Ansible connects to and can be used as variables in playbooks/templates.

By default, facts are collected by the setup module. This module is automatically triggered by playbooks when run, to gather useful variables about remote hosts that can be used in playbooks.

The setup module is not suitable for network equipment, so the collection of facts must be disabled. This can be done in the Ansible configuration file or in the playbook. Disabling fact gathering in the configuration file:

`gathering = explicit`

## Host Key Checking

The host key checking parameter in the configuration file is responsible for checking keys when connecting via SSH. If you specify `host_key_checking = False`, keys checking will be disabled. This is useful when the Ansible control node needs to connect with a large number of devices for the first time.

Ansible configuration file can be check with the below commands.

```console
ansible-config view
ansible-config dump --only-changed
```
