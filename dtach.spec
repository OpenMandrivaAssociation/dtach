
Summary: A simple program that emulates the detach feature of screen
Name: dtach
Version: 0.8
Release: 4
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
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/dtach
%{_mandir}/*/*





%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-3mdv2011.0
+ Revision: 617905
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.8-2mdv2010.0
+ Revision: 428392
- rebuild

* Mon Sep 01 2008 Gaëtan Lehmann <glehmann@mandriva.org> 0.8-1mdv2009.0
+ Revision: 278370
- update to new version 0.8

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.7-2mdv2009.0
+ Revision: 220204
- rebuild
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Gaëtan Lehmann <glehmann@mandriva.org>
    - rebuild


* Mon Mar 05 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.7-2mdv2007.0
+ Revision: 132760
- Fix group

* Tue Jan 02 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.7-1mdv2007.1
+ Revision: 103473
- Import dtach

