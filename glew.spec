Summary:	The OpenGL Extension Wrangler Library
Name:		glew
Version:	1.9.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/glew/%{name}-%{version}.tgz
# Source0-md5:	69ce911decef6249d24742497e6ad06a
URL:		http://glew.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
C/C++ extension loading library. GLEW provides efficient run-time
mechanisms for determining which OpenGL extensions are supported on
the target platform. OpenGL core and extension functionality is
exposed in a single header file.

%package devel
Summary:	Header files for glew
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel

%description devel
Header files for glew.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.guess config
%{__make} \
	CC="%{__cc}"		\
	LDFLAGS="%{rpmldflags}"	\
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/GL,%{_pkgconfigdir}}

install bin/* $RPM_BUILD_ROOT%{_bindir}
cp -d lib/* $RPM_BUILD_ROOT%{_libdir}
install include/GL/* $RPM_BUILD_ROOT%{_includedir}/GL
install glew.pc glewmx.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libGLEW*.so.?.?
%attr(755,root,root) %{_libdir}/libGLEW*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLEW*.so
%{_includedir}/GL/*.h
%{_pkgconfigdir}/*.pc

