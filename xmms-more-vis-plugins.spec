%define name xmms-more-vis-plugins
%define version 1.8.0
%define release %mkrel 18

%define plug0 jakdaw-0.0.4
%define plug1 synaesthesia-xmms-0.0.3-rc3
%define plug2 xmms_speakers-2.01
%define plug3 xmms-infinity-0.6.2
%define plug4 bump_scope-0.0.3
%define plug5 JESS-2.9.1
%define plug6 gforce-1.1.6xp3
%define plug7 paranormal-0.2.0
%define plug8 iris-0.12
%define plug9 wmdiscotux-1.3
%define plug10 xmms-nebulus-0.8.0
%define plug11 goom-2k4-0
%define plug12 xmms-vigor-0.1.1

%define major 0
%define libname %mklibname goom2_ %major

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	XMMS - More visualization plugins
Source0:	http://www.jakdaw.ucam.org/xmms/%{plug0}.tar.bz2
Source1:	http://staff.xmms.org/zinx/xmms/%{plug1}.tar.bz2
Source2:	http://home.swipnet.se/~w-92416/plugins/%{plug2}.tar.bz2
Source3:	http://wmdiscotux.stc.cx/%{plug9}.tar.bz2
Source4:	http://prdownloads.sourceforge.net/infinity-plugin/%{plug3}.tar.bz2
Source5:	http://staff.xmms.org/zinx/xmms/%{plug4}.tar.bz2
Source6:	http://arquier.free.fr/%{plug5}.tar.bz2
Source7:	%{plug6}.tar.bz2
Source8:	http://prdownloads.sourceforge.net/paranormal/%{plug7}.tar.bz2
Source9:	http://cdelfosse.free.fr/xmms-iris/%{plug8}.tar.bz2
Source10:	http://nebulus.tuxfamily.org/%{plug10}.tar.bz2
Source11:	http://downloads.sourceforge.net/goom/%{plug11}-src.tar.bz2
Source12:	http://heanet.dl.sourceforge.net/sourceforge/vigor/%{plug12}.tar.bz2
Source100:	ltconfig.bz2
Patch20:	xmms_speakers-2.01.patch
Patch0:		jakdaw-gcc2.96.patch
Patch100:	xmms-nebulus-0.8.0-dont-stop-right-after-start.patch
Patch10:	synaesthesia-xmms-0.0.3-gcc3.4.patch
Patch11:	synaesthesia-xmms-0.0.3-rc3-gcc4_0.patch
Patch40:	bump_scope-0.0.3-gcc3.4.patch

Patch52:	jess-2.9.1-gcc3.4.patch
Patch60:	gforce-fix-compile.patch
Patch61:	gforce-1.1.6xp3.dga.patch
Patch62:	gforce-libsupc++.patch
Patch63:	gforce-1.1.6xp3-dont-segfault-when-toggling-fullscreen-as-nonroot.patch
Patch70:	paranormal-0.2.0-fix-xml-detection.patch
Patch71:	paranormal-0.2.0-gcc3.4.patch
Patch90:	wmdiscotux-1.3.patch
Patch91:	wmdiscotux-1.3.-gcc3.3.patch
Patch92:	wmdiscotux-gcc2.96.patch
License:	GPL
Group:		Sound
URL:		http://www.xmms.org/
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	xmms >= 1.0.0
# (gc) yes the binary of xmms is tested for existence in the configure script
BuildRequires:	SDL-devel
BuildRequires:	libmesaglu-devel
BuildRequires:	libxxf86dga-devel
BuildRequires:	libxpm-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	esound-devel
BuildRequires:	libxml2-devel
BuildRequires:	xmms-devel
BuildRequires:	xmms
BuildRequires:	texinfo
BuildRequires:	automake1.4
BuildRequires:	automake1.7
BuildRequires:	automake1.8
#gw for running aclocal, needed by infinity-plugin
BuildRequires:	glib-gettextize
BuildRequires:  chrpath
Obsoletes:	xmms-goom
ExclusiveArch:	%{ix86} ppc x86_64

%description
More visualization plugins, from the best ones found on the home page of xmms
(http://www.xmms.org).

This package provides the following plugins:
- Jakdaw's plugin (blur oscilloscope),
- Infinity (interactive blur light effects),
- Synaesthesia (blur spots),
- wmdiscotux (tux moving on the music),
- Bump scope (bump version of the blur scope),
- G-Force (similar to Winamp Geiss),
- Jess (blur and deformation oscilloscope),
- Paranormal (pseudo-programmable audio visualization library, based
  (conceptually) on Winamp's AVS plugin),
- Iris OpenGL spectrum analyzer,
- Nebulus demo-like effects,
- Goom (multiple visual effects).

%package unsafe
Summary: XMMS - More visualization plugins (unsafe ones, often segfault...)
Group: Sound

%description unsafe
More visualization plugins. These ones are a bit dangerous and often cause
XMMS to segfault. Use at your own risk.

It provides the following plugins:
- xmms speakers.

%package -n %libname
Group: System/Libraries
Summary: Shared library part of the Goom visualization plugin

%description -n %libname
What a GOOM! version 2. This is a visualization plugin for xmms and
other media players.

%package -n %libname-devel
Group: Development/C
Summary: Development files of the Goom visualization plugin
Requires: %libname = %version
Provides: libgoom2-devel = %version-%release

%description -n %libname-devel
What a GOOM! version 2. This is a visualization plugin for xmms and
other media players. 

Install this if you want to embed the GOOM! in your own programs.

%prep
%setup -q -c
%setup -q -c -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12
%patch0
%patch10
%patch11 -b .gcc4_0
%patch20
%patch40 
%patch52
%patch60
%patch61
%patch62
%patch63 -p1
%patch70
%patch71
%patch90
%patch91
%patch92
%patch100 -p0
#wmdiscotux doesn't know lib64
perl -pi -e "s^/lib^/%_lib^g" %plug9/Makefile

# remove nasty no-newline-at-end-of-line, it bothers gcc-2.96
find . -name "*.h"   -exec perl -pi -e '$_.="\n" if eof' {} \;
# have ltconfig-1.3.5 so that libtool will manager to create a .so even if some XFree extensions are not available as .so
bzcat %{SOURCE100} > %{plug7}/ltconfig
# mkdirhier is just mkdir -p, but it's in XFree86, and I don't want to BuildRequires XFree86 for this nonsense
perl -pi -e 's/mkdirhier/mkdir -p/' gforce*/Makefile*

%build
cd %{plug0}
rm -f configure
aclocal-1.7
autoconf
automake-1.7 -a
%configure2_5x
%make
cd ..

cd %{plug9}
%make
cd ..

cd goom2k4-0
%configure2_5x
%make
#gw prevent relinking
perl -pi -e "s!relink_command.*!!" src/libxmmsgoom2.la
cd ..

for i in %{plug1} %{plug4} %{plug5}
do
  cd $i
  %configure
  %make
  cd ..
done

cd %{plug2}
rm -f configure
aclocal-1.4
autoconf
automake-1.4
%configure2_5x --libdir=%{_libdir}/xmms/Visualization
%make
cd ..
 
cd %{plug3}
rm -f config.cache
aclocal-1.8
automake-1.8
autoconf
%configure2_5x \
%ifarch ppc
  --disable-mmx
%endif
#gw cflags problem
%make CC="gcc -I."
cd ..

%ifnarch x86_64
cd %{plug6}
rm -f configure
aclocal-1.4
autoheader
automake-1.4
autoconf
%configure2_5x
make
cd ..
%endif

cd  %{plug7}
rm -f configure
aclocal-1.4
libtoolize --copy --force
automake-1.4
autoconf
%configure2_5x
%make
cd ..

cd  %{plug12}
rm -f configure
aclocal-1.8
libtoolize --copy --force
automake-1.8
autoconf
%configure2_5x
%make
cd ..

for i in %{plug8} %{plug10}
do
  cd $i
  %configure2_5x
  %make
  cd ..
done

%install
rm -rf $RPM_BUILD_ROOT doc/vigor infinity.lang
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

cd goom2k4-0
%makeinstall_std
chrpath -d %buildroot/%_libdir/xmms/Visualization/libxmmsgoom2.so
#gw let's not ship this
rm -f %buildroot%_bindir/goom2
cd ..

for i in %{plug0} %{plug1} %{plug2} %{plug4} %{plug5} %{plug7} %{plug8} %{plug10} %{plug12}
do
  cd $i
  %makeinstall libdir=$RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization
  cd ..
done

%ifnarch x86_64
cd %{plug6}
%makeinstall libdir=$RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization
cd ..
%endif

cd %{plug3}
%makeinstall libdir=$RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization
mkdir %buildroot/%_datadir/xmms/
mv %buildroot/%_datadir/infinite_states %buildroot/%_datadir/xmms/
cd ..

install -m 755 %{plug9}/libwmdiscotux.so $RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization

install -m 755 %{plug5}/.libs/* $RPM_BUILD_ROOT%{_libdir}/xmms/Visualization

# setup various docs
mkdir -p doc/jakdaw
cp %{plug0}/{AUTHORS,NEWS,COPYING,README,ChangeLog,INSTALL} doc/jakdaw
mkdir -p doc/synaesthesia
cp %{plug1}/{AUTHORS,NEWS,COPYING,README,ChangeLog,INSTALL} doc/synaesthesia 
mkdir -p doc-unsafe/xmms_speakers 
cp %{plug2}/{AUTHORS,BUGS,COPYING,ChangeLog,README,README.themes} doc-unsafe/xmms_speakers
mkdir -p doc/infinity
cp %{plug3}/{AUTHORS,REPORT-BUGS,COPYING,TODO,ChangeLog,NEWS,README,HISTORY} doc/infinity
mkdir -p doc/bump_scope
cp %{plug4}/{AUTHORS,COPYING,NEWS,ChangeLog,README,INSTALL} doc/bump_scope
mkdir -p doc/jess
cp %{plug5}/{AUTHORS,COPYING,ChangeLog,INSTALL,NEWS,README} doc/jess
mkdir -p doc/gforce
%ifnarch x86_64
cp %{plug6}/{AUTHORS,INSTALL,COPYING,ChangeLog,NEWS,README,README.2.0,TODO} doc/gforce
cp -r %{plug6}/docs doc/gforce
%endif
mkdir -p doc/paranormal
cp %{plug7}/{AUTHORS,COPYING,ChangeLog,INSTALL,README,TODO} doc/paranormal
mkdir -p doc/iris
cp  %{plug8}/{AUTHORS,TODO,COPYING,ChangeLog,NEWS,INSTALL,README} doc/iris
mkdir -p doc/wmdiscotux
cp %{plug9}/{COPYING,README} doc/wmdiscotux
mkdir -p doc/nebulus
cp %{plug10}/{AUTHORS,COPYING,ChangeLog,INSTALL,README} doc/nebulus
#mkdir -p doc/goom
#mv %{plug11}/{AUTHORS,KNOWNBUGS,BENCHMARKS,COPYING,ChangeLog,NEWS,INSTALL,README} doc/goom
mkdir -p doc/vigor
cp %{plug12}/{README,AUTHORS,COPYING,ChangeLog,HACKING,INSTALL,NEWS} doc/vigor

rm -f $RPM_BUILD_ROOT/%{_bindir}/{gforce,paranormal,pndoc}
rm -f $RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization/*a
rm -f $RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization/libjess.lai
rm -f $RPM_BUILD_ROOT/%{_libdir}/xmms/Visualization/*.o

%find_lang infinity
%find_lang xmms-nebulus
cat xmms-nebulus.lang >> infinity.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -f infinity.lang
%defattr(-,root,root)
%doc doc/*
%{_libdir}/xmms/Visualization/*
%{_datadir}/xmms/infinite_states
%{_datadir}/xmms-vigor
%ifnarch x86_64
%{_datadir}/gforce
%endif
%exclude %{_libdir}/xmms/Visualization/libxmms_speakers*

%files unsafe
%defattr(-,root,root)
%doc doc-unsafe/*
%{_libdir}/xmms/Visualization/libxmms_speakers*

%files -n %libname
%defattr(-,root,root)
%_libdir/libgoom2.so.*

%files -n %libname-devel
%defattr(-,root,root)
%_libdir/libgoom2.so
%_libdir/libgoom2.la
%_includedir/goom/
%_libdir/pkgconfig/libgoom2.pc


