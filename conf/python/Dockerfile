FROM python:2.7

RUN apt-get install -y gcc g++ make python python-pip python-dev\
 python-virtualenv libjpeg-dev libz-dev libfreetype6-dev liblcms-dev\
 libxml2-dev libxslt-dev ocaml-nox git-core python-imaging python-lxml\
 texlive-latex-recommended ploticus dvipng imagemagick pdftk

# Install mwlib & mwlib.rl
RUN pip install -i http://pypi.pediapress.com/simple/ mwlib
RUN pip install -i http://pypi.pediapress.com/simple/ mwlib.rl
