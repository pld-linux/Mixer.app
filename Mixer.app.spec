Summary:	A Window Maker dock app with mixer
Name:		Mixer.app
Version:	1.4.0
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source0:	http://www.student.hk-r.se/~pt96pli/mixer/%{name}-%{version}.tar.gz
URL:		http://www.student.hk-r.se/~pt96pli/mixer/
BuildPrereq:	libstdc++-devel
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Mixer.app is a audio mixer utility. It is designed to be docked in Window
Maker. This utility has three volume controllers that can be configured to
handle any sound source, the default sources are master-, cd- and
pcm-volume. Sound sources can easily be muted and there is also wheel mouse
support.

%prep
%setup  -q

%build
xmkmf -a
make	PREFIX=/usr/X11R6/GNUstep/Apps/Mixer.app \
	CXXDEBUGFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates" \

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=/usr/X11R6/GNUstep/Apps/Mixer.app

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir /usr/X11R6/GNUstep/Apps/Mixer.app
%attr(755,root,root) /usr/X11R6/GNUstep/Apps/Mixer.app/*

%changelog
* Mon May 10 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4.0-1]
- firs release in rpm package.
