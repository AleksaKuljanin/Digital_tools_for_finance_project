# tex live image as base
FROM texlive/texlive:latest

# Set the working directory
WORKDIR /reports

RUN tlmgr update --self && tlmgr install \
    latexmk \
    biber \
    xetex \
    latex

# Compile tex document
CMD ["latexmk", "-pdf", "output-directory=/Momentum_Strategies/reports/output/", "Momentum_Strategies/reports/main.tex"]