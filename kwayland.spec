%define major 5
%define libname %mklibname KF5WaylandClient %{major}
%define devname %mklibname KF5WaylandClient -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwayland
Version: 5.0.95
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
Summary: KDE Library for working with the Wayland display server
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Wayland)
BuildRequires: cmake(Qt5)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
KDE Library for working with the Wayland display server

%package -n %{libname}
Summary: KDE Library for working with the Wayland display server
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Library for working with the Wayland display server

%package -n %{devname}
Summary: Development files for the KDE Plasma 5 Wayland library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Plasma 5 Wayland library

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
