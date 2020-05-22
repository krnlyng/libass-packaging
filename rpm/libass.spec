Name:		libass
Version:	0.14.0
Release:	1%{?dist}
Summary:	libass is a portable subtitle renderer for the ASS/SSA (Advanced Substation Alpha/Substation Alpha) subtitle format.

License:	ISC
URL:		https://github.com/libass/libass
Source0:	${name}-${version}.tar.bz2

BuildRequires: automake
BuildRequires: libtool
BuildRequires: fribidi-devel

%package devel
Summary: libass development files
%description devel
libass development files

%description
libass is a portable subtitle renderer for the ASS/SSA (Advanced Substation Alpha/Substation Alpha) subtitle format.

%prep
%autosetup -p1 -n ${name}-${version}/upstream

%build
./autogen.sh --prefix=/usr
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libass.so.9
%{_libdir}/libass.so.9.0.2

%files devel
%defattr(-,root,root,-)
%{_libdir}/libass.so
%{_libdir}/libass.la
%{_libdir}/libass.a
%{_libdir}/pkgconfig
%{_libdir}/pkgconfig/libass.pc
%{_includedir}/ass/ass.h
%{_includedir}/ass/ass_types.h

