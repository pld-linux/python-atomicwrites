#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Atomic file writes
Summary(pl.UTF-8):	Atomowy zapis plików
Name:		python-atomicwrites
Version:	1.4.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/atomicwrites/
Source0:	https://files.pythonhosted.org/packages/source/a/atomicwrites/atomicwrites-%{version}.tar.gz
# Source0-md5:	9ff8e556d0b4a411d0cebbdb3fb0c70d
URL:		https://github.com/untitaker/python-atomicwrites
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Atomic file writes.

%description -l pl.UTF-8
Atomowy zapis plików.

%package -n python3-atomicwrites
Summary:	Atomic file writes
Summary(pl.UTF-8):	Atomowy zapis plików
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-atomicwrites
Atomic file writes.

%description -n python3-atomicwrites -l pl.UTF-8
Atomowy zapis plików.

%package apidocs
Summary:	API documentation for Python atomicwrites module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona atomicwrites
Group:		Documentation

%description apidocs
API documentation for Python atomicwrites module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona atomicwrites.

%prep
%setup -q -n atomicwrites-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/atomicwrites
%{py_sitescriptdir}/atomicwrites-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-atomicwrites
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/atomicwrites
%{py3_sitescriptdir}/atomicwrites-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
