Summary:	Userspace driver for IB over Intel SCIF devices
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla IB po urządzeniach Intel SCIF
Name:		libibverbs-driver-ibscif
Version:	1.0.0
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/libibscif/libibscif-%{version}.tar.gz
# Source0-md5:	d9acbd3e62568beb3202e0c8c0a3fd6c
URL:		http://openib.org/
BuildRequires:	libibverbs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
libibscif is a userspace driver for InfiniBand over Intel SCIF.

%description -l pl.UTF-8
libibscif to sterownik przestrzeni użytkownika dla InfiniBand po
urządzeniach Intel SCIF.

%package static
Summary:	Static version of ibscif driver
Summary(pl.UTF-8):	Statyczna wersja sterownika ibscif
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of ibscif driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika ibscif, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libibscif-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rdmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libibscif.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libibscif-rdmav2.so
%{_sysconfdir}/libibverbs.d/ibscif.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libibscif.a
