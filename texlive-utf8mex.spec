%global tl_name utf8mex
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Tools to produce formats that read Polish language input
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/polish/utf8mex
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/utf8mex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/utf8mex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides files for building formats to read input in Polish
encodings.

