#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Metadata
Summary:	Module::Metadata - gather package and POD information from Perl module files
Summary(pl.UTF-8):	Module::Metadata - zbieranie informacji o pakietach i POD z plików modułów Perla
Name:		perl-Module-Metadata
# NOTE: 1.000036 in perl-modules 5.30
Version:	1.000037
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6928e97831255ec3c99271a598523ea9
URL:		https://metacpan.org/release/Module-Metadata
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-version >= 0.87
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gather package and POD information from Perl module files.

%description -l pl.UTF-8
Module::Metadata - zbieranie informacji o pakietach i POD z plików
modułów Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/Metadata.pm
%{_mandir}/man3/Module::Metadata.3pm*
