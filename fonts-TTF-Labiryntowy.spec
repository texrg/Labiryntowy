Summary:	Labyrinth alphabet font
Summary(pl.UTF-8):	Font alfabetu labiryntowego
Name:		fonts-TTF-Labiryntowy
Version:	1.52
Release:	1
License:	freeware
Group:		Fonts
Source0:	https://github.com/texrg/Labiryntowy/archive/1.5.tar.gz
# Source0-md5:	b99609f88d8fe8e192e261d258523f43
URL:		http://alfabetozdobny.appspot.com/?str=labiryntowy
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Requires:	fontconfig >= 1:2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
Font Labiryntowy was created as a practical realization of the
labyrinth alphabet idea. This font contains over 300 ligatures and
most of the characters needed to write the titles, names and
monograms.

%description -l pl.UTF-8
Font Labiryntowy_pl powstaÅ‚ jako praktyczna realizacja idei alfabetu
labiryntowego. Font ten zawiera ponad 300 ligatur i wiÄ™kszoÅ›Ä‡ znakÃ³w
potrzebnych do wykonania tytuÅ‚Ã³w, imion i monogramÃ³w.

%prep
%setup -q -n Labiryntowy-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_ttffontsdir}

cp -p *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc opis.pdf
%{_ttffontsdir}/Labiryntowy_pl.ttf

