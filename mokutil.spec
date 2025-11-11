Summary:	Utility for managing SecureBoot/MOK keys
Name:		mokutil
Version:	0.7.2
Release:	1
Group:		System/Kernel and hardware
License:	GPL-3.0-only
URL:		https://github.com/lcp/mokutil
Source0:	https://github.com/lcp/mokutil/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnu-efi
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	pkgconfig(efivar) >= 31
BuildRequires:	pkgconfig(libkeyutils)
BuildRequires:	pkgconfig(libxcrypt)
BuildRequires:	pkgconfig(openssl)

%description
%{name} is a utility to manage machine owner keys (MOK) stored
in the database of shim.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%doc README
%license COPYING
%{_bindir}/mokutil
%{_datadir}/bash-completion/completions/mokutil
%{_mandir}/man1/*
