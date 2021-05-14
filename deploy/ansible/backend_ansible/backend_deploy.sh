#!/usr/bin/env bash

. ../unimelb-comp90024-2021-grp-29-openrc.sh; ansible-playbook backend_ansible.yaml -i ./host_vars/address.ini
