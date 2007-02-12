Summary:	A Window Maker dock app with mixer
Summary(pl.UTF-8):   Dokująca aplikacja Window Makera z mikserem
Name:		Mixer.app
Version:	1.4.0
Release:	1
Group:		X11/Window Managers/Tools
License:	GPL
Source0:	http://www.student.hk-r.se/~pt96pli/mixer/%{name}-%{version}.tar.gz
# Source0-md5:	d4d646f8939288a6bc92bb85f6b098c0
URL:		http://www.student.hk-r.se/~pt96pli/mixer/
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Mixer.app is a audio mixer utility. It is designed to be docked in
Window Maker. This utility has three volume controllers that can be
configured to handle any sound source, the default sources are
master-, cd- and pcm-volume. Sound sources can easily be muted and
there is also wheel mouse support.

%description -l pl.UTF-8
Mixer.app to program kontrolujący mikser audio. Jest zaprojektowany by
dokować się w Window Makerze. Ten program ma trzy kontrolery
głośności, które mogą być skonfigurowane tak, by mogły zarządzać
dowolnym źródłem dźwięku.

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


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_prefix}/GNUstep/Apps/Mixer.app
%attr(755,root,root) %{_prefix}/GNUstep/Apps/Mixer.app/*
