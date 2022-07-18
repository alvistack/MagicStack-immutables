%global debug_package %{nil}

Name: python-immutables
Epoch: 100
Version: 0.16
Release: 1%{?dist}
Summary: Immutable Collections
License: Apache-2.0
URL: https://github.com/MagicStack/immutables/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
An immutable mapping type for Python.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-immutables
Summary: Immutable Collections
Requires: python3
Requires: python3-typing-extensions >= 3.7.4.3
Provides: python3-immutables = %{epoch}:%{version}-%{release}
Provides: python3dist(immutables) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-immutables = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(immutables) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-immutables = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(immutables) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-immutables
An immutable mapping type for Python.

%files -n python%{python3_version_nodots}-immutables
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-immutables
Summary: Immutable Collections
Requires: python3
Requires: python3-typing-extensions >= 3.7.4.3
Provides: python3-immutables = %{epoch}:%{version}-%{release}
Provides: python3dist(immutables) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-immutables = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(immutables) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-immutables = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(immutables) = %{epoch}:%{version}-%{release}

%description -n python3-immutables
An immutable mapping type for Python.

%files -n python3-immutables
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
