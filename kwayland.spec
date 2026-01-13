%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KWaylandClient
%define devname %mklibname KWaylandClient -d
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} | sed -e 's,/,-,g')

%define major %(echo %{version} |cut -d. -f1-3)

Name: kwayland
Version: 6.5.5
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kwayland/-/archive/%{gitbranch}/kwayland-%{gitbranchd}.tar.bz2#/kwayland-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{major}/kwayland-%{version}.tar.xz
%endif
Summary: Qt-style Client and Server library wrapper for the Wayland libraries
URL: https://invent.kde.org/frameworks/kwayland
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: wayland-tools
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(VulkanHeaders)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6WaylandScannerTools)
BUildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(WaylandProtocols)
BuildRequires: cmake(EGL)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
Requires: %{libname} = %{EVRD}
# Renamed after 6.0, 2025-04-27
%rename plasma6-kwayland

%description
Qt-style Client and Server library wrapper for the Wayland libraries

%package -n %{libname}
Summary: Qt-style Client and Server library wrapper for the Wayland libraries
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Qt-style Client and Server library wrapper for the Wayland libraries

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt-style Client and Server library wrapper for the Wayland libraries

%package doc
Summary: Developer documentation for %{name} in Qt Assistant format
Group: Development/C

%description doc
Developer documentation for %{name} in Qt Assistant format

%files
%{_datadir}/qlogging-categories6/*

%files -n %{devname}
%{_includedir}/KWayland
%{_libdir}/cmake/KWayland
%{_libdir}/pkgconfig/KWaylandClient.pc

%files -n %{libname}
%{_libdir}/libKWaylandClient.so*

%files doc
%{_qtdir}/doc/KWayland.*
