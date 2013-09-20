Realtime Kernel Quick Configuration Guide
=========================================

Ubuntu
------

### Download the latest Real-Time patch and corresponding kernel version

    wget http://www.kernel.org/pub/linux/kernel/projects/rt/patch-2.6.29.6-rt23.bz2
    wget http://www.kernel.org/pub/linux/kernel/v2.6/linux-2.6.29.6.tar

### Unpack the kernel source and apply the real-time patch

    cd /usr/src
    sudo tar xjvf ~/linux-2.6.29.6.tar.bz2
    cd linux-2.6.29.5/
    sudo sh -c 'bzcat ~/patch-2.6.29.6-rt22.bz2 | patch -p1'

### Configure the kernel with essential real-time settings

    Processor type and features --->
        Preemption Mode (Complete Preemption (Real-Time))
        Timer frequency (1000 HZ)
          
### Build the kernel

    sudo fakeroot make-kpkg --initrd kernel_image kernel_headers

### Install the kernel and reboot

Use "dpkg -i" to install the new header and kernel packages located in /usr/src/
