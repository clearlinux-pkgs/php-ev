#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-ev
Version  : 1.1.5
Release  : 74
URL      : https://pecl.php.net/get/ev-1.1.5.tgz
Source0  : https://pecl.php.net/get/ev-1.1.5.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause PHP-3.01
Requires: php-ev-lib = %{version}-%{release}
Requires: php-ev-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

%package lib
Summary: lib components for the php-ev package.
Group: Libraries
Requires: php-ev-license = %{version}-%{release}

%description lib
lib components for the php-ev package.


%package license
Summary: license components for the php-ev package.
Group: Default

%description license
license components for the php-ev package.


%prep
%setup -q -n ev-1.1.5
cd %{_builddir}/ev-1.1.5
pushd ..
cp -a ev-1.1.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-ev
cp %{_builddir}/ev-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-ev/3ceae864520a5a1090f70804809d06df611778ea || :
cp %{_builddir}/ev-%{version}/libev/LICENSE %{buildroot}/usr/share/package-licenses/php-ev/10e633ee2e9f8a961554d0d579f03a1d0755ff3b || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/ev.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-ev/10e633ee2e9f8a961554d0d579f03a1d0755ff3b
/usr/share/package-licenses/php-ev/3ceae864520a5a1090f70804809d06df611778ea
