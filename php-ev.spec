#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-ev
Version  : 1.1.5
Release  : 33
URL      : https://pecl.php.net/get/ev-1.1.5.tgz
Source0  : https://pecl.php.net/get/ev-1.1.5.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause PHP-3.01
Requires: php-ev-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

%package lib
Summary: lib components for the php-ev package.
Group: Libraries

%description lib
lib components for the php-ev package.


%prep
%setup -q -n ev-1.1.5
cd %{_builddir}/ev-1.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/ev.so
