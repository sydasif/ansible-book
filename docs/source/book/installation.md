# Ansible Installation

Ansible handles communication between control nodes and managed nodes through multiple protocols:

- network_cli by SSH
- netconf by SSH
- httpapi by HTTP/HTTPS

Ansible can be installed on most Unix/Linux systems, with the only dependency being Python3.5 or higher. Currently, the Windows operating system is not officially supported as the control machine.

For installation, you can use the Ansible [website](https://docs.ansible.com/ansible/2.9/installation_guide/index.html), which supports various kinds of platforms. We will be installing Ansible on the WSL (Ubuntu) machine.

```console
sudo apt update
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get install ansible
```

Ansible is updated once every six months, so it's best to install it in a virtual environment.

```console
sudo apt install virtualenv
virtualenv ansible-lab
source ansible-lab/bin/activate
pip install ansible==2.9.27
```

Stop the virtual environment with the `deactivate` command.

Install Ansible using your preferred method. See [Installing Ansible](https://docs.ansible.com/ansible/2.9/installation_guide/intro_installation.html#installation-guide). Now we can check our managed node with the Ad-hoc command.
