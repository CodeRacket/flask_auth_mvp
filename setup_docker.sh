# Docker installation script for APt package manager tested on a Debian system 
# If your running a different version of Debian then consult the docker installation manual for your distro and package manager.

# Remove old packages if any
sudo apt remove docker-compose docker docker.io containerd runc

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update


# Install Docker + Compose plugin
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


# Setup user group with permissions

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
echo "To test the user group permissions you just need to execute: docker run hello-world"
echo "the Group is all setup. P.S look into docker & firewalls!"

# resources:
# https://docs.docker.com/engine/install/debian/#install-using-the-repository
