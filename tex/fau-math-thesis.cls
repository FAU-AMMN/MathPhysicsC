% ########################################################################################
% Class specification
% ----------------------------------------------------------------------------------------
\newcommand{\classname}{fau-math-thesis}
\newcommand{\fileversion}{1.1}
\newcommand{\filedate}{2020/10/02}
\newcommand{\cfileauthor}{Tim C.O. Roith}
\def\baseclass{scrbook}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{\classname}[\filedate\space Latex class for a FAU math thesis 
							provided by Tim C.O. Roith, v\fileversion.]
% ########################################################################################
% Options and bools
% ----------------------------------------------------------------------------------------
% Here we declare the options passed to the classed and define bools which are mostly 
% used further below
% ----------------------------------------------------------------------------------------
\usepackage{xkeyval} % Should be loaded here in case we want to define xkey Options
% ----------------------------------------------------------------------------------------
% Bibliography
% the options are currently very limited, user can either specify the 
% the bib stuff himself by using the default option or use the spec from the bib section 
% down below.
% ----------------------------------------------------------------------------------------
\def\bibstyle{\biblstyle@default}
\DeclareOptionX{bibstyle}{\def\bibstyle{\csname biblstyle@#1\endcsname}}
% ----------------------------------------------------------------------------------------
% Options for the page layout within KOMA
\newif\ifFAU@setBCOR\FAU@setBCORfalse
\newif\ifFAU@setDIV\FAU@setDIVfalse
\newif\ifFAU@setSided\FAU@setSidedfalse
% Binding offset
\DeclareOptionX{BCOR}{
	\FAU@setBCORtrue
	\PassOptionsToClass{\CurrentOption}{\baseclass}
}%
% DIV calculation
\DeclareOptionX{DIV}{
	\FAU@setDIVtrue
	\PassOptionsToClass{\CurrentOption}{\baseclass}
}%
% two or onesided definition
\DeclareOptionX{oneside}{
	\FAU@setSidedtrue
	\PassOptionsToClass{\CurrentOption}{\baseclass}
}%
\DeclareOptionX{twoside}{
	\FAU@setSidedtrue
	\PassOptionsToClass{\CurrentOption}{\baseclass}
}%
% ----------------------------------------------------------------------------------------
% If the page layout is not set by options and the PDF or print option is set we now 
% specify the page layout by means of the KOMA script.
% ----------------------------------------------------------------------------------------
\newif\ifTH@PDF\TH@PDFfalse % PDF Option, a document for PDF viewers
\newif\ifFAU@print\FAU@printfalse % print Option, a document for pinting
% ----------------------------------------------------------------------------------------
\DeclareOptionX{PDF}{\TH@PDFtrue}
\DeclareOptionX{setPDF}{
	\TH@PDFtrue
	% DIV SETTING
	\ifFAU@setDIV % it has already been set
		\ClassWarningNoLine{\classname}{The Option DIV has already been set. The 
		PDF option will not reset this value. If you want to use the default settings
		of PDF do not specify a DIV value.}
	\else
		\PassOptionsToClass{DIV=classic}{\baseclass}
	\fi
	% BINDING
	\ifFAU@setBCOR % it has already been set
		\ClassWarningNoLine{\classname}{The Option BCOR has already been set. The 
		PDF option will not reset this value. If you want to use the default settings
		of PDF do not specify a BCOR value.}
	\else
		\PassOptionsToClass{BCOR=0mm}{\baseclass}
	\fi
	% TWO-ONESIDED
	\ifFAU@setSided % it has already been set, probably output something
		\ClassWarningNoLine{\classname}{The Option side has already been set. The 
		PDF option will not reset this value. If you want to use the default settings
		of PDF do not specify a side value.}	
	\else
		\PassOptionsToClass{oneside}{\baseclass}
	\fi
}
% ----------------------------------------------------------------------------------------
\DeclareOptionX{print}{\FAU@printtrue}
\DeclareOptionX{setprint}{
	\FAU@printtrue
	% DIV SETTING
	\ifFAU@setDIV % it has already been set
	\ClassWarningNoLine{\classname}{The Option DIV has already been set. The 
	print option will not reset this value. If you want to use the default settings
	of PDF do not specify a DIV value.}
	\else
		\PassOptionsToClass{DIV=classic}{\baseclass}
	\fi
	% BINDING
	\ifFAU@setBCOR % it has already been set
	\else
		\ClassWarningNoLine{\classname}{The Option BCOR has not been set yet! The 
		print option will set it to BCOR=5mm. You should actually set this value yourself!}
		\PassOptionsToClass{BCOR=15mm}{\baseclass}
	\fi
	% TWO-ONESIDED
	\ifFAU@setSided % it has already been set, probably output something
	\ClassWarningNoLine{\classname}{The Option side has already been set. The 
	print option will not reset this value. If you want to use the default settings
	of PDF do not specify a side value.}	
	\else
		\PassOptionsToClass{twoside}{\baseclass}
	\fi		
}
% ----------------------------------------------------------------------------------------
\DeclareOptionX{showframe}{\PassOptionsToPackage{showframe}{geometry}}
% ----------------------------------------------------------------------------------------
% We might need these values for internal use, so let's consider them

% ----------------------------------------------------------------------------------------
% This passes all the options not considered so far to \baseclass
\DeclareOptionX*{\PassOptionsToClass{\CurrentOption}{\baseclass}}
\ProcessOptionsX
% ----------------------------------------------------------------------------------------
% We can now load our baseclass
\LoadClass{\baseclass}
\usepackage{scrhack}
% ########################################################################################
%
%
%
%
%
% ########################################################################################
\usepackage{graphicx}
% ########################################################################################
%
%
%
%
%
% ########################################################################################
% Colors
% ----------------------------------------------------------------------------------------
% Here we define the basic structure for using consistent colors in our document. The idea 
% is to define key values with respective commands, i.e. \titlecolor that can be used 
% througout the document. The command \colors will set the colors, it is used in the file
% fau-colors.sty where additional colors are defined.
% ----------------------------------------------------------------------------------------
\usepackage{xcolor}
%
\define@key{color}{colmain}{\def\colmain{#1}}
\define@key{color}{colmainlight}{\def\colmainlight{#1}}
\define@key{color}{colmainllight}{\def\colmainllight{#1}}
\define@key{color}{colmainlllight}{\def\colmainlllight{#1}}
\define@key{color}{colcomp}{\def\colcomp{#1}}
\setkeys{color}{colmain = black, colmainlight = white, colmainllight = white,%
				colmainlllight = white, colcomp=black}{}
%
\def\colors#1{
\setkeys{color}{#1}
\hypersetup{
		urlcolor=\colmain,
		citecolor=\colcomp,
		linkcolor=\colmain}
}
% ########################################################################################
%
%
%
%
%
% ########################################################################################
% Datetime commands
% ----------------------------------------------------------------------------------------
\usepackage[ngerman]{babel}
\usepackage{datetime2}
% ----------------------------------------------------------------------------------------
% Define the typical german style, ex: 02.Mai 2019
% ----------------------------------------------------------------------------------------
\DTMnewdatestyle{gerDatestyleA}{%
	\renewcommand{\DTMdisplaydate}[4]{\number##3.\DTMgermanmonthname{##2} \number##1 }%
	\renewcommand{\DTMDisplaydate}{\DTMdisplaydate}%
}
% Command for \today in the respective style
\newcommand{\gertoday}{\DTMsetdatestyle{gerDatestyleA}\today}
% ########################################################################################
%
%
%
%
%
% ########################################################################################
% Titelpage
% ----------------------------------------------------------------------------------------
% Some macros
\def\subdate#1{\gdef\@subdate{#1}}
\subdate{\gertoday} % The default value for the date is today in german style
\gdef\department#1{\gdef\@department{#1}} % Degree Program
\def\semester#1{\gdef\@semester{#1}} % for the degree you want to obtain
\def\keywords#1{\gdef\@keywords{#1}}
%--------------------------------------------------------------------------
\renewcommand{\maketitle}{
\begin{titlepage}
\thispagestyle{empty}
%\textsf{
\begin{center}
\vspace*{1cm}
{\Huge \textbf{\@title}} \\
\vspace{2cm}
{\LARGE\textbf{\@semester}}\\[5mm]
\vfill
{\LARGE\textbf{\@author}}\\
{\Large\@department}
\vfill
{\normalsize Version vom \textbf{\@subdate}}
\normalsize
\end{center}
%
\vfill%
%
\begin{minipage}{0.36\textwidth}
\vspace*{10mm}
\includegraphics[width=\textwidth]{atelier/logo/FAU_nat}
\end{minipage}
\hfill
\begin{minipage}{0.3\textwidth}
\includegraphics[width=\textwidth]{atelier/logo/DepMathLogo} \vspace{3mm}
\end{minipage}
%}
\end{titlepage}
}
% ########################################################################################
% Dedication
% ----------------------------------------------------------------------------------------
\newcommand{\dedicationtext}[1]{
\newcommand{\printdedication}{
\begin{titlepage}
\begin{center}
#1
\end{center}
\end{titlepage}
}
}
% ----------------------------------------------------------------------------------------
% Acknowledgement
% ----------------------------------------------------------------------------------------
\newcommand{\acknowledgementtext}[1]{
\newcommand{\printacknowledgement}{
\begin{center}
\textbf{\Large Acknowledgement}
\end{center}
#1
}
}
% ########################################################################################
%
%
%
%
%
% ########################################################################################
% Probably minitocs are cool, we'll see
% ----------------------------------------------------------------------------------------
%\usepackage[nohints,tight]{minitoc} 
%\setcounter{minitocdepth}{2} 
%% The level that gets a number:
%\setcounter{secnumdepth}{2}
%% The level that shows up in the ToC:
%\setcounter{tocdepth}{2}
%
%
%\renewcommand{\chapterheadstartvskip}{\vspace*{40pt}}
%\renewcommand{\chapterheadendvskip}{\vspace{30pt}}
% ########################################################################################
%
%
%
%
%
% ########################################################################################
% Bibliography
% ----------------------------------------------------------------------------------------
\usepackage{csquotes}
% ----------------------------------------------------------------------------------------
\def\biblstyle@default{}
% ----------------------------------------------------------------------------------------
\def\biblstyle@styleA{
	\usepackage[style=numeric-comp,%
			defernumbers=true,
			useprefix=true,%
			giveninits=true,%
			hyperref=true,%
			uniquename=init,%
			sorting = none,
			sortcites=false,% sort citations when multiple entries are passed to one cite command
			doi=true,%
			isbn=false,%
			url=false,%
			backend=biber %
	]{biblatex}
}
\def\biblstyle@styleB{
	\usepackage[style=alphabetic,%
		defernumbers=true,
		useprefix=true,%
		giveninits=true,%
		hyperref=true,%
		uniquename=init,%
		sorting = none,
		sortcites=false,% sort citations when multiple entries are passed to one cite command
		doi=true,%
		isbn=false,%
		url=false,%
		backend=biber %
		]{biblatex}	
}
\bibstyle
% url breaks
\setcounter{biburllcpenalty}{7000}
\setcounter{biburlucpenalty}{8000}
% ########################################################################################
%
%
%
%
%
% ########################################################################################
% Thorems, definitions, etc.
% ----------------------------------------------------------------------------------------
\usepackage{amsmath, amssymb, amsthm}
% ########################################################################################
%
%
%
%
%
% ########################################################################################
% Hyperref stuff
% ----------------------------------------------------------------------------------------
\usepackage{hyperref}
\hypersetup{
	colorlinks = true,
    final=true,
    plainpages=false,
    pdfstartview=FitV,
    pdftoolbar=true,
    pdfmenubar=true,
    pdfencoding=auto, % Allows symbols in toc and content oveview
    psdextra, % same as above
    bookmarksopen=true,
    bookmarksnumbered=true,
    breaklinks=true,
    linktocpage=true
}
\def\setpdfinfo{
	\hypersetup{pdfinfo={
		Title={\@title},
		Author={\@author},
		% Subject={\@thesistype},
		Keywords={\@keywords}}}
}
% ########################################################################################
% Misc
% ----------------------------------------------------------------------------------------
% Don't break enumeration (etc.) across pages in an ugly manner
\clubpenalty=10000
\widowpenalty=10000
% ########################################################################################
%
%
%
%
%
% ########################################################################################
% We use KOMA options instead of the geometry package. It is just loaded for the 
% showframe option. 
% ----------------------------------------------------------------------------------------
\usepackage[pass]{geometry} % This is just loaded for showframe
% ########################################################################################
%
%
%
%
%
% ########################################################################################
% Command for producing the declaration
% ----------------------------------------------------------------------------------------
\newenvironment{declaration}
% before environment
{\cleardoublepage
\settowidth{\dotspace}{\@author and \dateAndLoc}
\setlength{\dotspace}{\dimexpr(\textwidth - \dotspace - 2cm)\relax}
\if@twocolumn\onecolumn\fi
\begin{center} 
\textbf{\Large Erkl\"arung}
\end{center}
\thispagestyle{empty}}{\clearpage}
%
\def\dateAndLoc{Erlangen, den \gertoday}
\newlength{\dotspace}
% ----------------------------------------------------------------------------------------
% the predefind text from the examinatioons office
% ----------------------------------------------------------------------------------------	
\def\declarationGer{ 
\begin{declaration}
Hiermit versichere ich, dass ich die vorliegende Arbeit selbstst\"andig verfasst
und keine anderen als die angegebenen Quellen und Hilfsmittel benutzt habe,
dass alle Stellen der Arbeit, die w\"ortlich oder sinngem\"aß aus anderen Quellen
\"ubernommen wurden, als solche kenntlich gemacht sind und dass die Arbeit in
gleicher oder \"ahnlicher Form noch keiner Pr\"ufungsbeh\"orde vorgelegt wurde.\\[1cm]
% signature line
\noindent\dateAndLoc\hspace{\dotspace}\dotfill\\[2pt]
\strut\hfill\@author\hspace{1cm}	
\end{declaration}}
% ########################################################################################