#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ladspa_sdk
Version  : 1.16
Release  : 4
URL      : http://www.ladspa.org/download/ladspa_sdk_1.16.tgz
Source0  : http://www.ladspa.org/download/ladspa_sdk_1.16.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: ladspa_sdk-bin = %{version}-%{release}
Requires: ladspa_sdk-lib = %{version}-%{release}
Requires: ladspa_sdk-license = %{version}-%{release}
BuildRequires : pkgconfig(sndfile)

%description
LADSPA SDK
----------
The API itself can be be found in src/ladspa.h. The rest of this
package is a software development kit to make the API even easier to
work with.

%package bin
Summary: bin components for the ladspa_sdk package.
Group: Binaries
Requires: ladspa_sdk-license = %{version}-%{release}

%description bin
bin components for the ladspa_sdk package.


%package dev
Summary: dev components for the ladspa_sdk package.
Group: Development
Requires: ladspa_sdk-lib = %{version}-%{release}
Requires: ladspa_sdk-bin = %{version}-%{release}
Provides: ladspa_sdk-devel = %{version}-%{release}
Requires: ladspa_sdk = %{version}-%{release}

%description dev
dev components for the ladspa_sdk package.


%package lib
Summary: lib components for the ladspa_sdk package.
Group: Libraries
Requires: ladspa_sdk-license = %{version}-%{release}

%description lib
lib components for the ladspa_sdk package.


%package license
Summary: license components for the ladspa_sdk package.
Group: Default

%description license
license components for the ladspa_sdk package.


%prep
%setup -q -n ladspa_sdk_1.16
cd %{_builddir}/ladspa_sdk_1.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631119256
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
pushd src
make  PLUGINDIR=\\\"/usr/lib64/ladspa\\\" targets
popd


%install
export SOURCE_DATE_EPOCH=1631119256
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ladspa_sdk
cp %{_builddir}/ladspa_sdk_1.16/doc/COPYING %{buildroot}/usr/share/package-licenses/ladspa_sdk/4b97edd37482e476fac4a5e2db6c85b799ecaa82
cp %{_builddir}/ladspa_sdk_1.16/doc/license.html %{buildroot}/usr/share/package-licenses/ladspa_sdk/366969844ff94dcd0577c7df1b40f10d7b967556
pushd src
%make_install INSTALL_PLUGINS_DIR=%{buildroot}/usr/lib64/ladspa INSTALL_INCLUDE_DIR=%{buildroot}/usr/include INSTALL_BINARY_DIR=%{buildroot}/usr/bin
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/analyseplugin
/usr/bin/applyplugin
/usr/bin/listplugins

%files dev
%defattr(-,root,root,-)
/usr/include/ladspa.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/ladspa/amp.so
/usr/lib64/ladspa/delay.so
/usr/lib64/ladspa/filter.so
/usr/lib64/ladspa/noise.so
/usr/lib64/ladspa/sine.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ladspa_sdk/366969844ff94dcd0577c7df1b40f10d7b967556
/usr/share/package-licenses/ladspa_sdk/4b97edd37482e476fac4a5e2db6c85b799ecaa82
