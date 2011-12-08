
Summary: A simple program that emulates the detach feature of screen
Name: dtach
Version: 0.8
Release: %mkrel 3
License: GPL
URL: http://dtach.sourceforge.net
Group:   Terminals
Source: http://prdownloads.sourceforge.net/dtach/dtach-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-root
 
%description
dtach is a program that emulates the detach feature of screen, with
less overhead.  It is designed to be transparent and un-intrusive; it
avoids interpreting the input and output between attached terminals
and the program under its control. Consequently, it works best with
full-screen applications such as emacs.
  
%prep
%setup
 
%build
%configure
make
 
%install
rm -rf $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 755 dtach $RPM_BUILD_ROOT/%{_bindir}/dtach
install -m 644 dtach.1 $RPM_BUILD_ROOT/%{_mandir}/man1/dtach.1

%clean
make clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/dtach
%{_mandir}/*/*



