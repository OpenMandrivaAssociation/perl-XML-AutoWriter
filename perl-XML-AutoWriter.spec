%define upstream_name	 XML-AutoWriter
%define upstream_version 0.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module to do DOCTYPE based XML output

License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		XML-AutoWriter-0.4-fix_module_install_obsolete_keyword.patch

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
This module subclasses XML::ValidWriter and provides automatic start and end 
tag generation, allowing you to emit only the 'important' tags.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -b .modinst
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

