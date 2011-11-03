# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-utf8mex
Version:	20111103
Release:	1
Summary:	TeXLive utf8mex package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utf8mex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utf8mex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive utf8mex package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/mex/utf8mex/utf8-pl.tex
%{_texmfdistdir}/tex/mex/utf8mex/utf8mex.ini
%{_texmfdistdir}/tex/mex/utf8mex/utf8plsq.tex
%doc %{_texmfdistdir}/doc/mex/utf8mex/Makefile
%doc %{_texmfdistdir}/doc/mex/utf8mex/README
%doc %{_texmfdistdir}/doc/mex/utf8mex/examples/Makefile
%doc %{_texmfdistdir}/doc/mex/utf8mex/examples/catcode.tex
%doc %{_texmfdistdir}/doc/mex/utf8mex/examples/list.tex
%doc %{_texmfdistdir}/doc/mex/utf8mex/examples/tilde.tex
%doc %{_texmfdistdir}/doc/mex/utf8mex/examples/tilde2.tex
%doc %{_texmfdistdir}/doc/mex/utf8mex/test-math.utf8.tex
%doc %{_texmfdistdir}/doc/mex/utf8mex/test.utf8.tex
%doc %{_texmfdistdir}/doc/mex/utf8mex/utf8math.el
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
