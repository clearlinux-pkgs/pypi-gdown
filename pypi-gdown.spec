#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v19
# autospec commit: a62a849262cd
#
Name     : pypi-gdown
Version  : 5.2.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/09/6a/37e6b70c5bda3161e40265861e63b64a86bfc6ca6a8f1c35328a675c84fd/gdown-5.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/09/6a/37e6b70c5bda3161e40265861e63b64a86bfc6ca6a8f1c35328a675c84fd/gdown-5.2.0.tar.gz
Summary  : Google Drive Public File/Folder Downloader
Group    : Development/Tools
License  : MIT
Requires: pypi-gdown-bin = %{version}-%{release}
Requires: pypi-gdown-license = %{version}-%{release}
Requires: pypi-gdown-python = %{version}-%{release}
Requires: pypi-gdown-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_fancy_pypi_readme)
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<div align="center">
<h1>gdown</h1>
<p><b>Google Drive Public File Downloader when Curl/Wget Fails</b></p>
<img src="https://github.com/wkentaro/gdown/raw/main/.readme/cli.png" width="80%">
<img src="https://github.com/wkentaro/gdown/raw/main/.readme/python.png" width="80%">
<br>
<br>
</div>

%package bin
Summary: bin components for the pypi-gdown package.
Group: Binaries
Requires: pypi-gdown-license = %{version}-%{release}

%description bin
bin components for the pypi-gdown package.


%package license
Summary: license components for the pypi-gdown package.
Group: Default

%description license
license components for the pypi-gdown package.


%package python
Summary: python components for the pypi-gdown package.
Group: Default
Requires: pypi-gdown-python3 = %{version}-%{release}

%description python
python components for the pypi-gdown package.


%package python3
Summary: python3 components for the pypi-gdown package.
Group: Default
Requires: python3-core
Provides: pypi(gdown)
Requires: pypi(beautifulsoup4)
Requires: pypi(filelock)
Requires: pypi(requests)
Requires: pypi(tqdm)

%description python3
python3 components for the pypi-gdown package.


%prep
%setup -q -n gdown-5.2.0
cd %{_builddir}/gdown-5.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726084972
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-gdown
cp %{_builddir}/gdown-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gdown/1af331e9d49309059899727e141686f036bcff5c || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gdown

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-gdown/1af331e9d49309059899727e141686f036bcff5c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
