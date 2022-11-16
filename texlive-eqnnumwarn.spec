Name:		texlive-eqnnumwarn
Version:	45511
Release:	1
Summary:	Modifies the amsmath equation environments to warn for a displaced equation number
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqnnumwarn
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnnumwarn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnnumwarn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Sometimes an equation is too long that an equation number will
be typeset below the equation itself, but yet not long enough
to yield an "overfull \hbox" warning. The eqnnumwarn package
modifies the standard amsmath numbered equation environments to
throw a warning whenever this occurs.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/eqnnumwarn
%doc %{_texmfdistdir}/doc/latex/eqnnumwarn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
