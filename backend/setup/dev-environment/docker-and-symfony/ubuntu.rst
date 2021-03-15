.. _setup-dev-env-docker-symfony_ubuntu:

Set up Environment for OroPlatform Based Application on Ubuntu 20.04
====================================================================

This guide demonstrates how to set up :ref:`Docker and Symfony Server development stack <setup-dev-env-docker-symfony>` for Oro applications on Ubuntu 20.04 LTS.

Environment Setup
-----------------

1. Install PHP 7.4 with all required extensions:

   .. code-block:: bash

      sudo apt install software-properties-common
      sudo add-apt-repository -y ppa:ondrej/php
      sudo apt update
      sudo apt -y install php7.4 php7.4-fpm php7.4-cli php7.4-pdo php7.4-mysqlnd php7.4-xml php7.4-soap php7.4-gd php7.4-zip php7.4-intl php7.4-mbstring php7.4-opcache php7.4-curl php7.4-bcmath php7.4-ldap php7.4-pgsql php7.4-dev

2. If you going to use an Enterprise Edition of the application, install and enable the mongodb php extension:

   .. code-block:: bash

      sudo pecl channel-update pecl.php.net
      sudo pecl install mongodb
      sudo echo extension=mongodb.so  | sudo tee -a /etc/php/7.4/fpm/php.ini
      sudo echo extension=mongodb.so  | sudo tee -a /etc/php/7.4/cli/php.ini

3. Install Node.js 12:

   .. code-block:: bash

      sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates
      curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
      sudo apt -y install nodejs

4. Install Docker and Docker Compose:

   .. code-block:: bash

      sudo apt -y install docker.io docker-compose
      sudo usermod -aG docker $(whoami)
      sudo systemctl enable --now docker

5. Install Composer v2:

   .. code-block:: bash

      php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && php composer-setup.php
      php -r "unlink('composer-setup.php');"
      sudo mv composer.phar /usr/bin/composer

6. Install Symfony Server and enable TLS:

   .. code-block:: bash

      sudo apt -y install libnss3-tools
      wget https://get.symfony.com/cli/installer -O - | bash
      echo 'PATH="$HOME/.symfony/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc
      symfony server:ca:install

7. Restart the terminal and web browser to get them ready.

What's Next
-----------

* :ref:`Follow the recommendations <setup-dev-env-docker-symfony-recommendations>`
* :ref:`Install the Oro Application via the Command-Line Interface <setup-dev-env-docker-symfony-install-application>`
