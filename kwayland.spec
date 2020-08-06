%define major 5
%define libname %mklibname KF5WaylandClient %{major}
%define devname %mklibname KF5WaylandClient -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
# (tpg) 2019-08-20
# Called function is not the same type as the call!
#  tail call void @wl_event_queue_destroy(%struct.org_kde_kwin_appmenu_manager* nonnull %4) #26, !dbg !81688
# in function _ZN8KWayland6Client14WaylandPointerI14wl_event_queueXadL_Z22wl_event_queue_destroyEEED2Ev
# LLVM ERROR: Broken function found, compilation aborted!
# clang-9: error: linker command failed with exit code 1 (use -v to see invocation)
%define _disable_lto 1

Summary: KDE Library for working with the Wayland display server
Name: kwayland
Version: 5.73.0
Release: 1
License: GPL
Group: System/Libraries
Url: http://kde.org/
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(wayland-client) >= 1.8.1
BuildRequires: pkgconfig(wayland-scanner) >= 1.8.1
BuildRequires: pkgconfig(wayland-server) >= 1.8.1
BuildRequires: pkgconfig(wayland-protocols) >= 1.15
BuildRequires: wayland-tools >= 1.8.1
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5WaylandClient)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: qt5-qtwayland
# For building QCH docs
BuildRequires:  doxygen
BuildRequires:  qt5-assistant
Requires: qt5-qtwayland
Requires: %{_lib}qt5-output-driver-eglfs
Requires: %{libname} = %{EVRD}

%description
KDE Library for working with the Wayland display server.

%package -n %{libname}
Summary: KDE Library for working with the Wayland display server
Group: System/Libraries

%description -n %{libname}
KDE Library for working with the Wayland display server.

%package -n %{devname}
Summary: Development files for the KDE Frameworks Wayland library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks Wayland library.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories5/kwayland.categories
%{_libdir}/libexec/org-kde-kf5-kwayland-testserver
%{_datadir}/qlogging-categories5/kwayland.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
