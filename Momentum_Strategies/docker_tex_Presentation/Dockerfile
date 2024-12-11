# tex live image as base
FROM texlive/texlive:latest

# Set the working directory
WORKDIR /Momentum_Strategies/reports

RUN tlmgr update --self && tlmgr install \
    latexmk \
    biber \
    xetex \
    latex

# Compile tex document
CMD ["latexmk", "-pdf", "output-directory=/output/", "/Tex/Presentation.tex"]