%global tl_name eqnnumwarn
%global tl_revision 75878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Modifies the amsmath equation environments to warn for a displaced equation n...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eqnnumwarn
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnnumwarn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnnumwarn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Sometimes an equation is too long that an equation number will be
typeset below the equation itself, but yet not long enough to yield an
overfull \hbox warning. The eqnnumwarn package modifies the standard
amsmath numbered equation environments to throw a warning whenever this
occurs.

