import os

pwd = 'rex12345'


def umountall():
    umount_sda1 = 'umount /dev/sda1'
    umount_sda2 = 'umount /dev/sda5'
    umount_sda3 = 'umount /dev/sda6'
    os.system('echo %s|sudo -S %s' % (pwd, umount_sda1))
    os.system('echo %s|sudo -S %s' % (pwd, umount_sda2))
    os.system('echo %s|sudo -S %s' % (pwd, umount_sda3))


def mountall():
    mount_sda1 = 'mount /dev/sda1 ~/apps/hd/sda1'
    mount_sda2 = 'mount /dev/sda6 ~/apps/hd/sda6'
    mount_sda3 = 'mount /dev/sda5 ~/apps/hd/sda5'
    os.system('echo %s|sudo -S %s' % (pwd, mount_sda1))
    os.system('echo %s|sudo -S %s' % (pwd, mount_sda2))
    os.system('echo %s|sudo -S %s' % (pwd, mount_sda3))


def shutdown():
    umountall()
    os.system('shutdown now')
