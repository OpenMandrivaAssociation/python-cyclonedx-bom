Name:		python-cyclonedx-bom
Version:	7.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/cyclonedx-bom/cyclonedx_bom-%{version}.tar.gz
Summary:	CycloneDX Software Bill of Materials (SBOM) generator for Python projects and environments
URL:		https://pypi.org/project/cyclonedx-bom/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
CycloneDX Software Bill of Materials (SBOM) generator for Python projects and environments

%files
%{_bindir}/cyclonedx-py
%{py_sitedir}/cyclonedx_py
%{py_sitedir}/cyclonedx_bom-*.*-info
