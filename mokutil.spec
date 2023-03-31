Summary:	Utility for managing SecureBoot/MOK keys
Name:		mokutil
Version:	0.6.0
Release:	2
Group:		System/Kernel and hardware
License:	BSD
URL:		https://github.com/lcp/mokutil
Source0:	https://github.com/lcp/mokutil/archive/%{name}-%{version}.tar.gz
Patch1:		0001-Show-usage-instead-of-aborting-on-bad-flags.patch
Patch2:		0002-mokutil-bugfix-del-unused-opt-s.patch
Patch3:		0003-Fix-leak-of-list-in-delete_data_from_req_var.patch
Patch4:		0004-Fix-leak-of-fd-in-mok_get_variable.patch
BuildRequires:	pkgconfig(efivar) >= 0.12
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libkeyutils)
BuildRequires:	gnu-efi
BuildRequires:	pkgconfig(bash-completion)

%description
Utility for managing the "Machine's Owner Keys" list.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/mokutil
%doc %{_mandir}/man1/*
%{_datadir}/bash-completion/completions/mokutil
