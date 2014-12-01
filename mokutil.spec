Name:           mokutil
Version:        0.3.0
Release:        2
Summary:        Utility for managing SecureBoot/MOK keys
Group:          System/Kernel and hardware
License:        BSD
URL:            https://github.com/lcp/mokutil
Source0:        https://github.com/lcp/mokutil/archive/%{version}.tar.gz
Patch0:         mokutil-0.3.0-buffer-overflow.patch
Patch1:         mokutil-0.3.0-32bit-signed-comparison.patch

BuildRequires: pkgconfig(efivar) >= 0.12
BuildRequires: openssl-devel

%description
Utility for managing the "Machine's Owner Keys" list.

%prep
%setup -q
%apply_patches

%build
./autogen.sh
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=%{_prefix} LIBDIR=%{_libdir} DESTDIR=%{buildroot} install

%files
/usr/bin/mokutil
/usr/share/man/man1/mokutil.1.xz
