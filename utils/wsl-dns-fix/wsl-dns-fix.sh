#!/usr/bin/zsh

sudo echo "nameserver 8.8.8.8" >> /etc/resolv.conf

sudo apt-get --download-only --reinstall install resolvconf
sudo dpkg --purge --force-depends resolvconf
sudo apt-get install resolvconf
