subarch: i686
version_stamp: 2013.0
target: livecd-stage2
rel_type: hardened
profile: pentoo:pentoo/hardened/linux/x86
snapshot: 20130308
source_subpath: hardened/livecd-stage1-i686-2013.0
portage_overlay: /usr/src/pentoo/portage/trunk
cflags: -Os -march=pentium-m -mtune=nocona -pipe -fomit-frame-pointer -ggdb
cxxflags: -Os -march=pentium-m -mtune=nocona -pipe -fomit-frame-pointer -ggdb

# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
pkgcache_path: /catalyst/tmp/packages/x86-hardened

# This allows the optional directory containing the output packages for kernel
# builds.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# kerncache_path: /tmp/kernel
kerncache_path: /catalyst/kerncache/x86-hardened

livecd/fstype: squashfs
livecd/fsops:  -comp xz -Xbcj x86 -b 1048576 -Xdict-size 1048576 -no-recovery
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/grub-memtest86+-cdtar.tar.bz2
livecd/iso: /catalyst/release/Pentoo_i686/pentoo-i686-2013.0_RC1.1.iso

# A fsscript is simply a shell script that is copied into the chroot of the CD
# after the kernel(s) and any external modules have been compiled and is 
# executed within the chroot.  It can contain any commands that are available
# via the packages installed by our stages or by the packages installed during
# the livecd-stage1 build.  We do not use one for the official release media, so
# there will not be one listed below.  The syntax is simply the full path and
# filename to the shell script that you wish to execute.  The script is copied
# into the chroot by catalyst automatically.
# example:
# livecd/fsscript:
livecd/fsscript: /usr/src/pentoo/livecd/trunk/amd64/specs/2012.0/fsscript-livecd-stage2.sh

# The splash type determines the automatic arguments for the bootloader on
# supported architectures.  The possible options are gensplash and bootsplash.
# example:
# livecd/splash_type: gensplash
# livecd/splash_type: gensplash

# This is where you set the splash theme.  This theme must be present in either
# /etc/splash or /etc/bootsplash, depending on your livecd/splash_type, before
# the kernel has completed building during the livecd-stage2 target.
# example:
# livecd/splash_theme: livecd-2005.0
# livecd/splash_theme: gentoo

# This is a set of arguments that get passed to the bootloader for your CD.  It
# is used on the x86/amd64 release media to enable keymap selection.
# example:
# livecd/bootargs: dokeymap
livecd/bootargs: nodetect aufs max_loop=256 dokeymap

# This is a set of arguments that will be passed to genkernel for all kernels
# defined in this target.  It is useful for passing arguments to genkernel that
# are not otherwise available via the livecd-stage2 spec file.
# example:
# livecd/gk_mainargs: --lvm2 --dmraid
#livecd/gk_mainargs: --no-clean --no-mrproper --unionfs --makeopts=-j5
livecd/gk_mainargs: --disklabel --dmraid --gpg --luks --lvm --compress-initramfs-type=xz

# This option allows you to specify your own linuxrc script for genkernel to use
# when building your CD.  This is not checked for functionality, so it is up to
# you to debug your own script.  We do not use one for the official release
# media, so there will not be one listed below.
# example:
# livecd/linuxrc:
# livecd/linuxrc:

# This option controls quite a bit of catalyst internals and sets up several
# defaults.  Each type behaves slightly differently and is explained below.
# gentoo-release-minimal - This creates an official minimal InstallCD.
# gentoo-release-universal - This creates an official universal InstallCD.
# gentoo-release-livecd - This creates an official LiveCD environment.
# gentoo-gamecd - This creates an official Gentoo GameCD.
# generic-livecd - This should be used for all non-official media.
# example:
# livecd/type: gentoo-release-minimal
livecd/type: generic-livecd

# This is for the README.txt on the root of the CD.  For Gentoo releases, we
# use a default README.txt, and this will be used on your CD if you do not
# provide one yourself.  Since we do not use this for the official releases, it
# is left blank below.
# example:
# livecd/readme:
# livecd/readme:

# This is for the CD's message of the day.  It is not required for official
# release media, as catalyst builds a default motd when the livecd/type is set
# to one of the gentoo-* options.  This setting overrides the default motd even
# on official media.  Since we do not use this for the official releases, it is
# left blank below.
# example:
# livecd/motd:
# livecd/motd:

# This is for blacklisting modules from being hotplugged that are known to cause
# problems.  Putting a module name here will keep it from being auto-loaded,
# even if ti is detected by hotplug.
# example:
# livecd/modblacklist: 8139cp
livecd/modblacklist: arusb_lnx rt2870sta rt3070sta prism54 r8187 pcspkr nouveau ieee1394 ar9170usb

# This is for adding init scripts to runlevels.  The syntax for the init script
# is the script name, followed by a pipe, followed by the runlevel in which you
# want the script to run.  It looks like spind|default and is space delimited.
# We do not use this on the official media, as catalyst sets up the runlevels
# correctly for us.  Since we do not use this, it is left blank below.
# This option will automatically create missing runlevels
# example:
# livecd/rcadd:
livecd/rcadd: autoconfig|default acpid|default bluetooth|default consolekit|default gpm|default dbus|default

# This is for removing init script from runlevels.  It is executed after the
# defaults shipped with catalyst, so it is possible to remove the defaults using
# this option.  It can follow the same syntax as livcd/rcadd, or you can leave
# the runlevel off to remove the script from any runlevels detected.  We do not
# use this on the official media, so it is left blank.
# example:
# livecd/rcdel:
livecd/rcdel: keymaps|boot netmount|default mdraid|boot

# This overlay is dropped onto the CD filesystem and is outside any loop which
# has been configured.  This is typically used for adding the documentation,
# distfiles, snapshots, and stages to the official media.  These files will not 
# be available if docache is enabled, as they are outside the loop.
# example:
# livecd/overlay: /tmp/overlay-minimal
livecd/overlay: /usr/src/pentoo/livecd/trunk/isoroot

# This overlay is dropped onto the filesystem within the loop.  This can be used
# for such things as updating configuration files or adding anything else you
# would want within your CD filesystem.  Files added here are available when
# docache is used.  We do not use this on the official media, so we will leave
# it blank below.
# example:
# livecd/root_overlay:
livecd/root_overlay: /usr/src/pentoo/livecd/trunk/root_overlay

# This is used by catalyst to copy the specified file to /etc/X11/xinit/xinitrc
# and is used by the livecd/type gentoo-gamecd and generic-livecd.  While the
# file will still be copied for any livecd/type, catalyst will only create the
# necessary /etc/startx for those types, so X will not be automatically started.
# This is useful also for setting up X on a CD where you do not wish X to start
# automatically.  We do not use this on the release media, so it is left blank.
# example:
# livecd/xinitrc:
# livecd/xinitrc:

# This is used by catalyst to determine which display manager you wish to
# become the default.  This is used on the official Gentoo LiveCD and is valid
# for any livecd/type.
# example:
# livecd/xdm: gdm
# livecd/xdm:

# This is used by catalyst to determine which X session should be started by
# default by the display manager.  This is used on the official Gentoo LiveCD
# and is valid for any livecd/type.
# example:
# livecd/xsession: gnome
# livecd/xsession:

# This option is used to create non-root users on your CD.  It takes a space
# separated list of user names.  These users will be added to the following
# groups: users,wheel,audio,games,cdrom,usb
# If this is specified in your spec file, then the first user is also the user
# used to start X. Since this is not used on the release media, it is blank.
# example:
# livecd/users:
# livecd/users:

# This option sets the volume ID of the CD created.
# example:
livecd/volid: Pentoo Linux 2013.0 i686 RC1.1

# This option is used to specify the number of kernels to build and also the
# labels that will be used by the CD bootloader to refer to each kernel image.
# example:
# boot/kernel: gentoo
boot/kernel: pentoo

boot/kernel/pentoo/sources: pentoo-sources

# This option is the full path and filename to a kernel .config file that is
# used by genkernel to compile the kernel this label applies to.
# example:
# boot/kernel/gentoo/config: /tmp/2.6.11-smp.config
boot/kernel/pentoo/config: /usr/src/pentoo/livecd/trunk/x86/kernel/config-latest

# This option sets genkernel parameters on a per-kernel basis and applies only
# to this kernel label.  This can be used for building options into only a
# single kernel, where compatibility may be an issue.  Since we do not use this
# on the official release media, it is left blank, but it follows the same
# syntax as livecd/gk_mainargs.
# example:
# boot/kernel/gentoo/gk_kernargs:
boot/kernel/pentoo/gk_kernargs: 

# This option sets the USE flags used to build the kernel and also any packages
# which are defined under this kernel label.  These USE flags are additive from
# the default USE for the specified profile.
# example:
# boot/kernel/gentoo/use: pcmcia usb -X
boot/kernel/pentoo/use: X aufs livecd gtk -kde -eds gtk2 cairo pam firefox gpm dvdr oss
cuda opencl mpi wps offensive dwm -doc -examples
wifi injection lzma speed gnuplot python pyx test-programs fwcutter qemu
-quicktime -qt -qt3 qt3support qt4 -webkit -cups -spell lua curl -dso
png jpeg gif dri svg aac nsplugin xrandr consolekit -ffmpeg fontconfig
alsa esd fuse gstreamer jack mp3 vorbis wavpack wma
dvd mpeg ogg rtsp x264 xvid sqlite truetype nss xfce
opengl dbus binary-drivers hal acpi usb subversion libkms
analyzer bluetooth cracking databse exploit forensics mitm proxie
scanner rce footprint forging fuzzers voip wireless -livecd-stage1 symlink

# This option appends an extension to the name of your kernel, as viewed by a
# uname -r/  This also affects any modules built under this kernel label.  This
# is useful for having two kernels using the same sources to keep the modules
# from overwriting each other.  We do not use this on the official media, so it
# is left blank.
# example:
# boot/kernel/gentoo/extraversion:
# boot/kernel/gentoo/extraversion:

# This option is for merging kernel-dependent packages and external modules that
# are configured against this kernel label.
# example:
# boot/kernel/gentoo/packages: pcmcia-cs speedtouch slmodem globespan-adsl hostap-driver hostap-utils ipw2100 ipw2200 fritzcapi fcdsl cryptsetup
#pentoo/pentoo
boot/kernel/pentoo/packages: 
pentoo/pentoo
dev-util/lafilefixer
#I'm currently adding some livecd stage2 packages in from fsscript, it allows significantly more visibility into what is happening and kernel sources need a little tweaking

# This option is only for ppc64 machines.  If used it will create the /etc/yaboot.conf
# entry used for booting a ibm powerpc machine.
# example:
# boot/kernel/gentoo/machine_type: ibm
# boot/kernel/gentoo/machine_type:

# This is a list of packages that will be unmerged after all the kernels have
# been built.  There are no checks on these packages, so be careful what you
# add here.  They can potentially break your CD.
# example:
# livecd/unmerge: acl attr autoconf automake bin86 binutils libtool m4 bison ld.so make perl patch linux-headers man-pages sash bison flex gettext texinfo ccache distcc addpatches man groff lib-compat miscfiles rsync sysklogd bc lcms libmng genkernel diffutils libperl gnuconfig gcc-config gcc bin86 cpio cronbase ed expat grub lilo help2man libtool gentoo-sources
livecd/unmerge: dev-util/lafilefixer x11-drivers/ati-drivers x11-drivers/nvidia-drivers

# This option is used to empty the directories listed.  It is useful for getting
# rid of files that don't belong to a particular package, or removing files from
# a package that you wish to keep, but won't need the full functionality.
# example:
livecd/empty: /var/empty /run/lock /var/log /var/tmp /var/spool /tmp /usr/local/portage/ /var/lib/layman/pentoo /usr/lib/debug

# This option tells catalyst to clean specific files from the filesystem and is
# very usefu in cleaning up stray files in /etc left over after livecd/unmerge.
# example:
livecd/rm: /etc/resolv.conf /usr/share/doc/lib* /usr/share/doc/g* /usr/share/doc/tiff* /usr/share/doc/twisted* /usr/share/doc/ruby* /usr/share/doc/paramiko* /usr/share/doc/perl* /usr/share/doc/pcre*  /usr/share/doc/binutils* /usr/share/doc/ntp* /usr/share/doc/readline*

