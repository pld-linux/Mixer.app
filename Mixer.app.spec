Summary:	A Window Maker dock app with mixer
Name:		Mixer.app
Version:	1.4
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source0:	http://www.student.hk-r.se/~pt96pli/mixer/%{name}-%{version}.tar.gz
URL:		http://www.student.hk-r.se/~pt96pli/mixer/
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
Mixer.app is a audio mixer utility. It is designed to be docked in Window
Maker. This utility has three volume controllers that can be configured to
handle any sound source, the default sources are master-, cd- and
pcm-volume. Sound sources can easily be muted and there is also wheel mouse
support.

%prep
%setup  -q

%build
(autoheader/autoconf/automake)
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT/usr/info/*.info* \
	$RPM_BUILD_ROOT/usr/man/man*/* \
	README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%changelog
