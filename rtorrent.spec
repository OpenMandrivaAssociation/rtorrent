%define	libtorrentver	0.13.7

Name:		rtorrent
Version:	0.9.8
Release:	2
Epoch:		1
Summary:	Curses based BitTorrent client
License:	GPLv2+
Group:		Networking/File transfer
URL:		https://rakshasa.github.io/rtorrent/
Patch0:		rtorrent-0.9.8_color.patch
Source0:	http://rtorrent.net/downloads/%name-%{version}.tar.gz

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
autoreconf -fiv
export CPPFLAGS=-I%{_includedir}/ncursesw
export LIBS="-lpthread -lxmlrpc -lxmlrpc_util"

%configure --with-xmlrpc-c
%make_build


%install 
%makeinstall_std


%files
%doc README AUTHORS doc/rtorrent.rc
%{_bindir}/rtorrent
