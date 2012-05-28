#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Metadata
%include	/usr/lib/rpm/macros.perl
Summary:	Module::Metadata - gather package and POD information from Perl module files
Summary(pl.UTF-8):	Module::Metadata - zbieranie informacji o pakietach i POD z plików modułów Perla
Name:		perl-Module-Metadata
Version:	1.000009
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9669dd618585de6832368043bc8c59b5
URL:		http://search.cpan.org/dist/Module-Metadata/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
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
%doc Changes
%{perl_vendorlib}/Module/Metadata.pm
%{_mandir}/man3/Module::Metadata.3pm*
