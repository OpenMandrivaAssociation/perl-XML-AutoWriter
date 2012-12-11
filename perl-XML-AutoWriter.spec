%define upstream_name	 XML-AutoWriter
%define upstream_version 0.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl module to do DOCTYPE based XML output
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
This module subclasses XML::ValidWriter and provides automatic start and end 
tag generation, allowing you to emit only the 'important' tags.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod -x $(find -type f)
sed -i 's/\r//' CHANGES

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check 
make test

%install
%makeinstall_std

%files
%doc CHANGES 
%{_mandir}/*/*
%{perl_vendorlib}/XML/

%changelog
* Wed Jul 08 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.0
+ Revision: 393405
- update to 0.4
- using %%perl_convert_version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.39-3mdv2008.0
+ Revision: 23553
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.39-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Tue Jan 17 2006 Michael Scherer <misc@mandriva.org> 0.39-1mdk
- New release 0.39
- use mkrel
- add a real description ( why no one noticed before )
- fix rpmlint warning and policy violation

* Tue Aug 23 2005 Michael Scherer <misc@mandriva.org> 0.38-2mdk
- Birthday rebuild

* Fri Aug 06 2004 Michael Scherer <misc@mandrake.org> 0.38-1mdk
- First package for Mandrakelinux

