#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network and are slow)

%define		githash	9878a30
%define		rel		1
Summary:	bi-directional git to bzr bridge: never fear bzr again
Name:		git-bzr
Version:	0.1
Release:	1.%{githash}.%{rel}
License:	BSD-like
Group:		Development/Languages
# SF URL: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:	https://github.com/termie/git-bzr-ng/archive/%{githash}/%{name}-g%{githash}.tar.gz
# Source0-md5:	4aae9976cda23959355da8945a88670a
URL:		https://github.com/termie/git-bzr-ng
BuildRequires:	rpm-pythonprov
Requires:	bzr-fastimport >= 0.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git-bzr-ng is a bidirectional bridge between git and bzr that lets you
stop worrying which version control the code you love is using -- as
long as they are using git or bzr ;) (hg coming soon?).

Easy to use and cleanly written (I hope (send patches!)). Check out
the examples below for basic usage.

%prep
%setup -qc
mv git-bzr-ng-*/* .

%build
%{?with_tests:./run_tests.sh}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/git-bzr
