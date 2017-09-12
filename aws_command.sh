#!/usr/bin/env bash
ANSIBLE_CONFIG=~/.ssh/ansible.cfg AWS_TAG_CDV=ENVIRON  AWS_TAG_SERVICE=MongoDB AWS_ACCESS_KEY_ID=XXXXX AWS_SECRET_ACCESS_KEY=XXXXX ansible -i hosts/inventory.py MongoDB -a "$1"
