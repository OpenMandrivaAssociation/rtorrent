%define	libtorrentver	0.14.0

Name:		rtorrent
Version:	0.10.0
Release:	1
Summary:	Curses based BitTorrent client
License:	GPLv2+
Group:		Networking/File transfer
URL:		https://rakshasa.github.io/rtorrent/
Patch0:		rtorrent-0.9.8_color.patch
#Source0:	http://rtorrent.net/downloads/%name-%{version}.tar.gz
Source0:  https://github.com/rakshasa/rtorrent/releases/download/v%{version}/rtorrent-%{version}.tar.gz

BuildRequires:	pkgconfig(libtorrent) >= %{libtorrentver}
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(xmlrpc)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(cppunit)

%description
This is a text mode BitTorrent client with a curses interface based on 
libtorrent.

%prep
%autosetup -p1

%build
#autoreconf -fiv
#export CPPFLAGS=-I%{_includedir}/ncursesw
#export LIBS="-lpthread -lxmlrpc -lxmlrpc_util"

%configure \
          --enable-ipv6 \
          --with-xmlrpc-c
%make_build

%install 
%make_install

%files
%doc README AUTHORS doc/rtorrent.rc
%{_bindir}/rtorrent
