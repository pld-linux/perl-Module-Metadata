#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Metadata
%include	/usr/lib/rpm/macros.perl
Summary:	Module::Metadata - Gather package and POD information from perl module files
Name:		perl-Module-Metadata
Version:	1.000004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3011f1b7f2f7b5462760df89aefc7035
URL:		http://search.cpan.org/dist/Module-Metadata/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-version >= 0.87
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gather package and POD information from perl module files.

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
%{perl_vendorlib}/Module/*.pm
%{_mandir}/man3/Module::Metadata.3pm*
