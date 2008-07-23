%define module	XML-AutoWriter
%define version 0.39
%define release %mkrel 5

Summary:	Perl module to do DOCTYPE based XML output
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel 
BuildRequires:  perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot/
BuildArch:	noarch

%description
This module subclasses XML::ValidWriter and provides automatic start and end 
tag generation, allowing you to emit only the 'important' tags.

%prep
%setup -q -n %{module}-%{version}
chmod -x $(find -type f)
sed -i 's/\r//' CHANGES

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check 
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc CHANGES 
%{_mandir}/*/*
%{perl_vendorlib}/XML/
