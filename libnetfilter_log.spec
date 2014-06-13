%define major 1
%define libname %mklibname netfilter_log %{major}
%define libnamedevel %mklibname netfilter_log -d

Summary:	Netfilter userspace packet logging library
Name:		libnetfilter_log
Version:	1.0.1
Release:	6
Group:		System/Libraries
License:	GPL
URL:		http://www.netfilter.org/projects/libnetfilter_log/index.html
Source0:	http://www.netfilter.org/projects/libnetfilter_log/files/libnetfilter_log-%{version}.tar.bz2
Source1:	http://www.netfilter.org/projects/libnetfilter_log/files/libnetfilter_log-%{version}.tar.bz2.sig
Patch0:		libnetfilter_log-1.0.1-linkage_fix.diff
BuildRequires:	pkgconfig(libnfnetlink) >= 0.0.41
BuildRequires:	autoconf automake libtool

%description
libnetfilter_log is a userspace library providing interface to packets that
have been logged by the kernel packet filter. It is is part of a system that
deprecates the old syslog/dmesg based packet logging. This library has been
previously known as libnfnetlink_log.

%package -n %{libname}
Summary:	Netfilter userspace packet logging library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	netfilter_log = %{version}-%{release}

%description -n %{libname}
libnetfilter_log is a userspace library providing interface to packets that
have been logged by the kernel packet filter. It is is part of a system that
deprecates the old syslog/dmesg based packet logging. This library has been
previously known as libnfnetlink_log.

%package -n %{libnamedevel}
Summary:        Development files for %{name}
Group:          System/Libraries
Provides:	netfilter_log-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{libnamedevel}
This package contains the development files for %{name}.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%{_includedir}/libnetfilter_log
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnetfilter_log.pc



%changelog
* Mon Apr 16 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1
+ Revision: 791245
- import libnetfilter_log


* Mon Apr 16 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1
- initial Mandriva package
