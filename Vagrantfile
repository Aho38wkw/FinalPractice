Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64"
    config.vm.network "private_network", type: "static", ip: "192.168.33.10"
    # Configura las claves SSH para Vagrant
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
  end
  