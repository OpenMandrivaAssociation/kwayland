%define major 5
%define libname %mklibname KF5WaylandClient %{major}
%define devname %mklibname KF5WaylandClient -d
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwayland
Version: 5.2.95
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Library for working with the Wayland display server
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: wayland-tools
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
KDE Library for working with the Wayland display server.

%package -n %{libname}
Summary: KDE Library for working with the Wayland display server
Group: System/Libraries

%description -n %{libname}
KDE Library for working with the Wayland display server.

%package -n %{devname}
Summary: Development files for the KDE Plasma 5 Wayland library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Plasma 5 Wayland library.

%prep
%setup -qn %{name}-%{plasmaver}
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{plasmaver}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
