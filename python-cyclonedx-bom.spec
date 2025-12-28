%define module cyclonedx-bom
%define oname cyclonedx_bom

Name:		python-cyclonedx-bom
Version:	7.2.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/cyclonedx-bom/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	CycloneDX Software Bill of Materials (SBOM) generator for Python projects and environments
URL:		https://pypi.org/project/cyclonedx-bom/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
CycloneDX Software Bill of Materials (SBOM) generator for Python projects and environments

%files
%doc README.md
%license LICENSE
%{_bindir}/cyclonedx-py
%{py_sitedir}/cyclonedx_py
%{py_sitedir}/%{oname}-%{version}.dist-info
