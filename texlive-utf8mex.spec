# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-utf8mex
Version:	20111104
Release:	7
Summary:	TeXLive utf8mex package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utf8mex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/utf8mex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive utf8mex package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 757332
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719865
- texlive-utf8mex
- texlive-utf8mex
- texlive-utf8mex
- texlive-utf8mex

