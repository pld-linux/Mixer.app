Summary:	A Window Maker dock app with mixer
Summary(pl):	Dokuj±ca aplikacja Window Makera z mikserem
Name:		Mixer.app
Version:	1.4.0
Release:	1
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
License:	GPL
Source0:	http://www.student.hk-r.se/~pt96pli/mixer/%{name}-%{version}.tar.gz
URL:		http://www.student.hk-r.se/~pt96pli/mixer/
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

%description
Mixer.app is a audio mixer utility. It is designed to be docked in
Window Maker. This utility has three volume controllers that can be
configured to handle any sound source, the default sources are
master-, cd- and pcm-volume. Sound sources can easily be muted and
there is also wheel mouse support.

%description -l pl
Mixer.app to program kontroluj±cy mikser audio. Jest zaprojektowany by
dokowaæ siê w Window Makerze. Ten program ma trzy kontrolery
g³o¶no¶ci, które mog± byæ skonfigurowane tak, by mog³y zarz±dzaæ
dowolnym ¼ród³em d¼wiêku.

%prep
%setup  -q

%build
xmkmf -a
make	PREFIX=%{_prefix}/GNUstep/Apps/Mixer.app \
	CXXDEBUGFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates" \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}/GNUstep/Apps/Mixer.app

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_prefix}/GNUstep/Apps/Mixer.app
%attr(755,root,root) %{_prefix}/GNUstep/Apps/Mixer.app/*
