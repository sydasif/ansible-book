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

## Ansible Ad-hoc Command

An Ansible Ad-hoc command uses the /usr/bin/ansible command-line tool to automate a single task on one or more managed nodes. Ad-hoc commands are quick and easy, but they are not reusable.

To run an Ad-hoc command or Ansible playbook it is mandatory to establish a manual SSH connection to the managed nodes to confirm your credentials and retrieve its configuration. This manual connection also establishes the authenticity of the network device, adding its RSA key fingerprint to your list of known hosts.

Instead of manually connecting and running a command on the network device, you can retrieve its configuration with a single, stripped-down Ansible command as below:

```json
$ ansible all -i 9.9.9.100, -c network_cli -u admin -k -m ping -e ansible_network_os=ios
SSH password:
9.9.9.100 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

The flags in this command set seven values:

- the host group(s) to which the command should apply (in this case, all)
- the inventory (-i, the device or devices to target - without the trailing comma -i points to an inventory file)
- the connection method (-c, the method for connecting and executing ansible)
- the user (-u, the username for the SSH connection)
- the SSH connection method (-k, please prompt for the password)
- the module (-m, the ansible module to run)
- an extra variable ( -e, in this case, setting the network OS value)

## Ansible modules

A large number of modules are also installed alongside the installation of Ansible. Modules are responsible for the actions that Ansible executes on managed nodes. Furthermore, each module is responsible for a specific task. Modules can be run individually, in ad-hoc commands, or assembled into a particular job (play) and then into a playbook.

For example, we have already executed ad-hoc commands using the ios_command module and passed an argument.

`ansible 9.9.9.101 -m ios_command -a "commands='sh ip int br'"`

Ansible modules are generally idempotent. This means that the module can be executed as many times as desired, but the module will only make changes if the system is not in the desired state.

## Ansible Raw module

The raw module is the module that doesn’t translate our commands (not going through the module subsystem), Ansible purely transfer our commands on remote devices via SSH. A common case is installing python on a system without python installed by default or devices such as routers that do not have any Python installed. The raw module is mainly used for monitoring and troubleshooting.

```json
$ ansible all -i 9.9.9.100, -u admin -m raw -a "sh ver" -k                                              ─╯
SSH password:
9.9.9.100 | CHANGED | rc=0 >>
Cisco IOS Software, vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(CML_NIGHTLY_20180619)FLO_DSGS7, EARLY DEPLOYMENT DEVELOPMENT BUILD, synced to  V152_6_0_81_E
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Tue 19-Jun-18 06:06 by mmen


ROM: Bootstrap program is IOSv

SW1 uptime is 28 minutes
System returned to ROM by reload
System image file is "flash0:/vios_l2-adventerprisek9-m"
Last reload reason: Unknown reason



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco IOSv () processor (revision 1.0) with 574709K/209920K bytes of memory.
Processor board ID 9S6WO17B82L
1 Virtual Ethernet interface
16 Gigabit Ethernet interfaces
DRAM configuration is 72 bits wide with parity disabled.
256K bytes of non-volatile configuration memory.
2097152K bytes of ATA System CompactFlash 0 (Read/Write)
0K bytes of ATA CompactFlash 1 (Read/Write)
0K bytes of ATA CompactFlash 2 (Read/Write)
0K bytes of ATA CompactFlash 3 (Read/Write)

Configuration register is 0x101

**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************Shared connection to 9.9.9.100 closed.
```

We probably don’t want to see every line of the output from “show version” command. So we can use grep, to filter, the name of the device and also the version.

```json
$ ansible all -i 9.9.9.100, -u admin -m raw -a "sh ver" -k | grep "CHANGED\|Version"                    ─╯
SSH password:
9.9.9.100 | CHANGED | rc=0 >>
Cisco IOS Software, vios_l2 Software (vios_l2-ADVENTERPRISEK9-M), Version 15.2(CML_NIGHTLY_20180619)FLO_DSGS7, EARLY DEPLOYMENT DEVELOPMENT BUILD, synced to  V152_6_0_81_E
```

One more example:

```json
 ansible all -i 9.9.9.101,9.9.9.102 -u admin -m raw -a "sh ip int bri | ex unass" -k                   ─╯
SSH password:
9.9.9.101 | CHANGED | rc=0 >>

Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            9.9.9.101       YES NVRAM  up                    up
Shared connection to 9.9.9.101 closed.

9.9.9.102 | CHANGED | rc=0 >>

Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            9.9.9.102       YES NVRAM  up                    up
Shared connection to 9.9.9.102 closed.
```

More practical examples are below:

```console
ansible all -m raw -u admin -a “show running-config | include username” -k
ansible all -m raw -u admin -a “show ip interface brief” -k
ansible all -m raw -u admin -a “show ip interface brief | exclude unass” -k
ansible all -m raw -u admin -a “show arp” -k
ansible all -m raw -u admin -a “show mac address-table | include ” -k
```
