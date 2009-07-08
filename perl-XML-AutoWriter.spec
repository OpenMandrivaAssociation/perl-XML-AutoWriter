%define upstream_name	 XML-AutoWriter
%define upstream_version 0.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Perl module to do DOCTYPE based XML output
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(XML::Parser)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module subclasses XML::ValidWriter and provides automatic start and end 
tag generation, allowing you to emit only the 'important' tags.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
