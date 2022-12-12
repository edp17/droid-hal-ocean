# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device ocean
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty G7 Power

%define installable_zip 1

%define enable_kernel_update 1

%define additional_ha_groups \
system\
%{nil}

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define droid_target_aarch64 1

#decomission sys-fs-pstore.service
%define makefstab_skip_entries /sys/fs/pstore

%define straggler_files \
/cache\
/d\
/product\
/product_services\
/sdcard\
/bugreports\
%{nil}


%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

